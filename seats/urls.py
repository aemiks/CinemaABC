from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    MovieListView,
    seats_choose,
)

app_name = 'seats'

urlpatterns = [
    path('', MovieListView.as_view(), name="movie-list"),
    path('seats-choose/<int:id>/', seats_choose, name="seats_choose" )
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)