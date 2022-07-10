from django.db import models
from datetime import datetime as dt
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


def upload_directory(instance, filename):
    """function to define where we want to upload an original image file
    Returns:
        uploads the file into the movieposters folder and subfolders with the current upload date
    """
    _now = dt.now()
    return 'movieposters/{year}/{month_date}/{filename}'.format(
        filename=filename, year=_now.strftime('%Y'), month_date=_now.strftime('%m%d')
    )


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    duration = models.PositiveIntegerField(default=0)
    poster = models.ImageField(upload_to=upload_directory, blank=True, null=True,
                               validators=[FileExtensionValidator(
                                   allowed_extensions=['jpg', 'png'])]
                               )

    def __str__(self):
        return self.title


class CinemaHall(models.Model):
    hall_name = models.CharField(max_length=15, blank=True, null=True)
    row_length = models.PositiveSmallIntegerField(default=0)
    seats_length = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.hall_name


class ScreeningDate(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="dates")
    cinema_hall = models.ForeignKey(
        CinemaHall, on_delete=models.CASCADE, related_name="dates", blank=True, null=True)
    screening_day = models.DateField()
    screening_hour = models.CharField(max_length=5)

    def __str__(self):
        return str(self.movie.title + ' , ' + str(self.screening_day) + ' , ' + str(self.screening_hour))

    class Meta:
        ordering = ['screening_day']

    # validation to prevent adding past screening date
    def save(self, *args, **kwargs):
        if self.screening_day < timezone.now().date():
            raise ValidationError("The date cannot be in the past!")
        super(ScreeningDate, self).save(*args, **kwargs)


class Seat(models.Model):
    cinema_hall = models.ForeignKey(
        CinemaHall, on_delete=models.CASCADE, related_name="seats", blank=True, null=True)
    screening_date = models.ForeignKey(
        ScreeningDate, on_delete=models.CASCADE, related_name="seats", blank=True, null=True)
    seat_number = models.PositiveSmallIntegerField(default=0)
    seat_sold = models.BooleanField(default=False)

    def __str__(self):
        return str(self.seat_number)
