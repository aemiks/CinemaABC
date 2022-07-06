from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Movie, ScreeningDate


class MovieListView(ListView):
    model = Movie


def seats_choose(request, id):
    context = {}
    screening_date = ScreeningDate.objects.get(id=id)
    movie = screening_date.movie
    cinema_hall = screening_date.cinema_hall

    rows = [_ for _ in range(1,cinema_hall.row_length+1)]
    seats_length = [_ for _ in range(1,cinema_hall.seats_length+1)]

    context['rows'] = rows
    context['seats_length'] = seats_length
    context['date'] = screening_date
    context['movie'] = movie

    return render(request, 'seat_list.html', context)
