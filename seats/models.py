from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.title

class ScreeningDate(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="dates")
    screening_day = models.DateField()
    screening_hour = models.CharField(max_length=5)

    def __str__(self):
        return str(self.movie.title + ' , ' + str(self.screening_day) + ' , ' + str(self.screening_hour))

class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="seats")
    screening_date = models.ForeignKey(ScreeningDate,on_delete=models.CASCADE, related_name="seats")
    seat_number = models.CharField(max_length=3)
    seat_empty = models.BooleanField(default=True)

    def __str__(self):
        return str(self.movie.title + ' , ' + str(self.screening_date.screening_day) + ' , ' + str(self.screening_date.screening_hour) + ' , ' + self.seat_number)

