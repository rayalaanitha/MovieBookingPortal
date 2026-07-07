from django.contrib import admin
from .models import Movie, Showtime, SeatBooking, MovieReview

admin.site.register(Movie)
admin.site.register(Showtime)
admin.site.register(SeatBooking)
admin.site.register(MovieReview)