from django.shortcuts import render
from django.views.generic import ListView
from .models import Movie, ScreeningDate, Seat
from django.http import HttpResponse
from .filters import MovieFilter
from django.utils import timezone


class MovieListView(ListView):
    """List all movies available  in cinema"""
    model = Movie

    def get_context_data(self, **kwargs):
        """"Changing the context data to apply the filter, and screening date validation
        """
        context = super(MovieListView, self).get_context_data(**kwargs)

        # Film screenings that have taken place already are being removed
        qs = Movie.objects.all()
        for movie in qs:
            if movie.dates:
                dates = ScreeningDate.objects.filter(movie=movie)
                for date in dates:
                    if date.screening_day < timezone.now().date():
                        date.delete()

        context['filter'] = MovieFilter(
            self.request.GET, queryset=Movie.objects.all())
        return context


def seatSelect(request, id):
    """function to display and select seats in the cinema room
    """
    context = {}
    screening_date = ScreeningDate.objects.get(id=id)
    cinema_hall = screening_date.cinema_hall

    # create our own cinema hall with the number of seats and rows (in Model CinemaHall)
    rows = [_ for _ in range(1, cinema_hall.row_length+1)]
    seats_length = [_ for _ in range(1, cinema_hall.seats_length+1)]

    # sending the list of sold seats to template (then js marks them as sold)
    sold_seats = []
    sold = screening_date.seats.all()
    for obj in sold:
        sold_seats.append(obj.seat_number)
    sold_seats = list(map(str, sold_seats))

    context['sold_seats'] = sold_seats
    context['rows'] = rows
    context['seats_length'] = seats_length
    context['date'] = screening_date

    return render(request, 'seat_list.html', context)


def orderSummary(request):
    """simple function to display summary template
    """
    context = {}
    seat_selected = request.GET.getlist('seat_list[]')
    screening_date_id = request.GET.get('screening_date')

    screening_date = ScreeningDate.objects.get(id=screening_date_id)

    context['screening_date'] = screening_date
    context['seat_list'] = seat_selected

    return render(request, 'summary_list.html', context)


def orderComplete(request):
    """function to order seats, and display booking confirmation
    """
    context = {}
    seat_selected = request.GET.getlist('seat_list[]')
    screening_date_id = request.GET.get('screening_date')

    screening_date = ScreeningDate.objects.get(id=screening_date_id)

    context['screening_date'] = screening_date
    context['seat_list'] = seat_selected

    # book seat but first checking if seat isn't already booked(its handle by js, but in a case of front error additional validation in backend)
    if seat_selected:
        for seat_number in seat_selected:
            qs = Seat.objects.filter(
                seat_number=seat_number, screening_date=screening_date)
            if qs.exists():
                return HttpResponse({'ERROR: Something wrong, seats already booked..'})
            else:
                seat = Seat.objects.create(
                    screening_date=screening_date,
                    cinema_hall=screening_date.cinema_hall,
                    seat_number=seat_number,
                    seat_sold=True,
                )
                seat.save()

    return render(request, 'order_complete.html', context)
