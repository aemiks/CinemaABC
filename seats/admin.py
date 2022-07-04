from django.contrib import admin
from .models import Movie, ScreeningDate, Seat

admin.site.register(Movie)
admin.site.register(ScreeningDate)
admin.site.register(Seat)
