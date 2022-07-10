from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    MovieListView,
    seatSelect,
    orderSummary,
    orderComplete,
)

app_name = 'seats'

urlpatterns = [
    path('', MovieListView.as_view(), name="movie-list"),
    path('seat-select/<int:id>/', seatSelect, name="seat-select"),
    path('order-summary/', orderSummary, name="order-summary"),
    path('order-complete/', orderComplete, name="order-complete")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
