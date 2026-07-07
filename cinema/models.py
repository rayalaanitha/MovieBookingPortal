from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):
    GENRES = [
        ('ACT', 'Action & Adventure'),
        ('SCI', 'Sci-Fi & Fantasy'),
        ('COM', 'Comedy & Drama'),
        ('HOR', 'Horror & Thriller'),
    ]

    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=10, choices=GENRES)
    duration_minutes = models.PositiveIntegerField(default=120)
    release_date = models.DateField()
    poster_url = models.URLField(
        blank=True,
        default="https://via.placeholder.com/300x450"
    )
    description = models.TextField()

    def __str__(self):
        return self.title


class Showtime(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='showtimes'
    )
    show_date = models.DateField()
    show_time = models.TimeField()
    ticket_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=12.00
    )
    screen_number = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['movie', 'show_date', 'show_time', 'screen_number']

    def __str__(self):
        return f"{self.movie.title} - Screen {self.screen_number}"


class SeatBooking(models.Model):
    showtime = models.ForeignKey(
        Showtime,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    seat_numbers = models.CharField(max_length=100)
    total_paid = models.DecimalField(max_digits=8, decimal_places=2)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.seat_numbers}"


class MovieReview(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    reviewer_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating}★ - {self.movie.title}"