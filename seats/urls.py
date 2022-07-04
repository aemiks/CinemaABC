from django.urls import path
from .views import (
    MovieListView,
)

app_name = 'todo_app'

urlpatterns = [
    path('', MovieListView.as_view(), name="movie-list"),
]