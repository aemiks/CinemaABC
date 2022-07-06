from django.db import models
from datetime import datetime as dt
from django.core.validators import FileExtensionValidator


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
    poster = models.ImageField(upload_to=upload_directory, blank= True, null=True,
                                validators=[FileExtensionValidator(allowed_extensions=['jpg','png'])]
                                )

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
        return self.seat_number


