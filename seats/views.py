from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Movie, ScreeningDate


class MovieListView(ListView):
    model = Movie


def seats_choose(request, id):
    context = {}
    screening_day = ScreeningDate.objects.get(id=id)
    movie = screening_day.movie
    context['date'] = screening_day
    context['movie'] = movie

    return render(request, 'seat_list.html', context)
