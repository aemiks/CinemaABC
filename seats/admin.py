from django.contrib import admin
from .models import Movie, ScreeningDate, Seat, CinemaHall

admin.site.register(Movie)
admin.site.register(CinemaHall)
admin.site.register(ScreeningDate)
admin.site.register(Seat)
