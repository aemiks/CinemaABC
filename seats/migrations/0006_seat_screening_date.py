# Generated by Django 4.0.6 on 2022-07-08 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seats', '0005_remove_seat_movie_remove_seat_row_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='screening_date',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='seats.screeningdate'),
        ),
    ]