import os
import django
from datetime import date, time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_booking.settings")
django.setup()

from cinema.models import Movie, Showtime

movies = [
    {
        "title": "Chennai Lovestory",
        "genre": "Romance",
        "duration_minutes": 169,
        "release_date": date(2026, 7, 10),
        "poster_url": "https://images.filmibeat.com/webp/280x383/img/popcorn/movie_posters/chennailovestory-20250602192552-23733.jpg",
        "description": "A journey through space and time."
    },
    {
        "title": "Don't Trouble The Trouble",
        "genre": "Drama, Fantasy",
        "duration_minutes": 181,
        "release_date": date(2026, 7, 24),
        "poster_url": "https://images.filmibeat.com/webp/280x383/img/popcorn/movie_posters/donttroublethetrouble-20240319162636-22732.jpg",
        "description": "The Avengers' final battle against Thanos."
    },
    {
        "title": "MAHAKALI",
        "genre": "Superhero movie",
        "duration_minutes": 170,
        "release_date": date(2026, 7, 17),
        "poster_url": "https://images.filmibeat.com/webp/280x383/img/popcorn/movie_posters/mahakali-20251030111838-23222.jpg",
        "description": "Action thriller starring Shah Rukh Khan."
    },
    
    {
        "title": "MYSAA",
        "genre": "Action, Period",
        "duration_minutes": 164,
        "release_date": date(2026, 7, 17),
        "poster_url": "https://images.filmibeat.com/webp/280x383/img/popcorn/movie_posters/mysaa-20250627102941-7342.jpg",
        "description": "Action thriller starring Vijay."
    },
   
]
for m in movies:

    movie, created = Movie.objects.update_or_create(
        title=m["title"],
        defaults=m
    )

    if created:
        print(f"Added: {movie.title}")
    else:
        print(f"Updated: {movie.title}")

    Showtime.objects.get_or_create(
        movie=movie,
        show_date=date.today(),
        show_time=time(16, 0),
        screen_number=1,
        defaults={"ticket_price": 12}
    )

    Showtime.objects.get_or_create(
        movie=movie,
        show_date=date.today(),
        show_time=time(19, 30),
        screen_number=1,
        defaults={"ticket_price": 12}
    )

print("Movies added successfully!")