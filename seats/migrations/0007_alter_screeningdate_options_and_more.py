# Generated by Django 4.0.6 on 2022-07-10 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seats', '0006_seat_screening_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='screeningdate',
            options={'ordering': ['screening_day']},
        ),
        migrations.AlterField(
            model_name='screeningdate',
            name='cinema_hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dates', to='seats.cinemahall'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='cinema_hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='seats.cinemahall'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='screening_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='seats.screeningdate'),
        ),
    ]
