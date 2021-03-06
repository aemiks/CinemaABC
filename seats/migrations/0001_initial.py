# Generated by Django 4.0.6 on 2022-07-04 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='ScreeningDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screening_day', models.DateTimeField()),
                ('screening_hour', models.CharField(max_length=5)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dates', to='seats.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=3)),
                ('seat_empty', models.BooleanField(default=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='seats.movie')),
                ('screening_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='seats.screeningdate')),
            ],
        ),
    ]
