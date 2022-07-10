import django_filters
from .models import Movie, ScreeningDate


class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = ['title', ]
