# Generated by Django 5.1.2 on 2024-11-02 01:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Booking statuses',
                'db_table': 'booking_status',
            },
        ),
        migrations.CreateModel(
            name='CarriageClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=50)),
                ('seating_capacity', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Carriage classes',
                'db_table': 'carriage_class',
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('email_address', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Passengers',
                'db_table': 'passenger',
            },
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_number', models.CharField(max_length=25, unique=True)),
                ('train_name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Trains',
                'db_table': 'train',
            },
        ),
        migrations.CreateModel(
            name='TrainStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Train stations',
                'db_table': 'train_station',
            },
        ),
        migrations.CreateModel(
            name='CarriagePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('carriage_class', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookingApp.carriageclass')),
            ],
            options={
                'verbose_name_plural': 'Carriage prices',
                'db_table': 'carriage_price',
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.IntegerField()),
                ('class_type', models.CharField(max_length=20)),
                ('availability_status', models.CharField(max_length=255)),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookingApp.train')),
            ],
            options={
                'verbose_name_plural': 'Seats',
                'db_table': 'seat',
            },
        ),
        migrations.CreateModel(
            name='TrainJourney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookingApp.train')),
            ],
            options={
                'verbose_name_plural': 'Train journeys',
                'db_table': 'train_journey',
            },
        ),
        migrations.CreateModel(
            name='JourneyCarriage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('carriage_class', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookingApp.carriageclass')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookingApp.train')),
                ('journey', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookingApp.trainjourney')),
            ],
            options={
                'verbose_name_plural': 'Journey carriages',
                'db_table': 'journey_carriage',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(blank=True, null=True)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookingApp.bookingstatus')),
                ('ticket_class', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookingApp.carriageclass')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookingApp.passenger')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookingApp.seat')),
                ('train_journey', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookingApp.trainjourney')),
                ('ending_station', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='booking_ending_station_set', to='BookingApp.trainstation')),
                ('starting_station', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookingApp.trainstation')),
            ],
            options={
                'verbose_name_plural': 'Bookings',
                'db_table': 'booking',
            },
        ),
        migrations.CreateModel(
            name='JourneyStation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stop_order', models.IntegerField(blank=True, null=True)),
                ('arrival_station', models.DateTimeField()),
                ('departure_time', models.DateTimeField()),
                ('journey', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookingApp.trainjourney')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookingApp.trainstation')),
            ],
            options={
                'db_table': 'journey_station',
                'constraints': [models.UniqueConstraint(fields=('journey', 'station'), name='unique_journey_station')],
            },
        ),
    ]
