from decimal import Decimal

from django.db.models import Avg
from django.shortcuts import render, get_object_or_404, redirect

from .models import Movie, Showtime, SeatBooking, MovieReview
from .forms import BookingForm, ReviewForm


# Home Page
def home(request):
    query = request.GET.get("q")
    genre = request.GET.get("genre")

    movies = Movie.objects.annotate(
        average_rating=Avg("reviews__rating")
    )

    if query:
        movies = movies.filter(title__icontains=query)

    if genre:
        movies = movies.filter(genre=genre)

    return render(request, "home.html", {
        "movies": movies,
        "query": query,
        "genre": genre,
        "genres": Movie.GENRES,
    })


# Movie Detail + Reviews
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()

            return redirect("movie_detail", movie_id=movie.id)

    else:
        form = ReviewForm()

    reviews = movie.reviews.all().order_by("-created_at")

    return render(request, "movie_detail.html", {
        "movie": movie,
        "form": form,
        "reviews": reviews,
    })


# Seat Booking
def book_seat(request, showtime_id):
    showtime = get_object_or_404(Showtime, id=showtime_id)

    # Already booked seats
    booked_seats = []

    bookings = SeatBooking.objects.filter(showtime=showtime)

    for booking in bookings:
        booked_seats.extend(
            [seat.strip() for seat in booking.seat_numbers.split(",")]
        )

    if request.method == "POST":

        form = BookingForm(request.POST)

        if form.is_valid():

            seat_numbers = request.POST.get("seat_numbers", "")
            total_paid = request.POST.get("total_paid", "0")

            # No seat selected
            if not seat_numbers:
                return render(request, "booking.html", {
                    "showtime": showtime,
                    "form": form,
                    "booked_seats": booked_seats,
                    "error": "Please select at least one seat."
                })

            selected = [
                seat.strip()
                for seat in seat_numbers.split(",")
            ]

            duplicate = [
                seat
                for seat in selected
                if seat in booked_seats
            ]

            # Seat already booked
            if duplicate:
                return render(request, "booking.html", {
                    "showtime": showtime,
                    "form": form,
                    "booked_seats": booked_seats,
                    "error": f"These seats are already booked: {', '.join(duplicate)}"
                })

            # Save booking
            booking = form.save(commit=False)
            booking.showtime = showtime
            booking.seat_numbers = seat_numbers
            booking.total_paid = Decimal(total_paid)
            booking.save()

            return render(request, "booking_success.html", {
                "booking": booking
            })

    else:
        form = BookingForm()

    return render(request, "booking.html", {
        "showtime": showtime,
        "form": form,
        "booked_seats": booked_seats,
    })