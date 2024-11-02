from django.db import models


class BookingStatus(models.Model):
    status_name = models.CharField(max_length=255)

    def __str__(self):
        return self.status_name

    class Meta:
        db_table = 'booking_status'
        verbose_name_plural = 'Booking statuses'


class Booking(models.Model):
    passenger = models.ForeignKey('Passenger', on_delete=models.CASCADE)
    status = models.ForeignKey('BookingStatus', on_delete=models.DO_NOTHING)
    starting_station = models.ForeignKey('TrainStation', on_delete=models.CASCADE)
    ending_station = models.ForeignKey('TrainStation', on_delete=models.CASCADE, related_name='booking_ending_station_set')
    train_journey = models.ForeignKey('TrainJourney', on_delete=models.CASCADE)
    ticket_class = models.ForeignKey('CarriageClass', on_delete=models.DO_NOTHING)
    seat = models.ForeignKey('Seat', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Booking {self.id} for {self.passenger}"

    class Meta:
        db_table = 'booking'
        verbose_name_plural = 'Bookings'


class CarriageClass(models.Model):
    class_name = models.CharField(max_length=50)
    seating_capacity = models.IntegerField()

    def __str__(self):
        return self.class_name

    class Meta:
        db_table = 'carriage_class'
        verbose_name_plural = 'Carriage classes'


class CarriagePrice(models.Model):
    carriage_class = models.ForeignKey(CarriageClass, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Price for {self.carriage_class}: {self.price}"

    class Meta:
        db_table = 'carriage_price'
        verbose_name_plural = 'Carriage prices'


class JourneyCarriage(models.Model):
    journey = models.ForeignKey('TrainJourney', on_delete=models.CASCADE)
    train = models.ForeignKey('Train', on_delete=models.CASCADE)
    carriage_class = models.ForeignKey(CarriageClass, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.carriage_class} on Journey {self.journey}"

    class Meta:
        db_table = 'journey_carriage'
        verbose_name_plural = 'Journey carriages'


class JourneyStation(models.Model):
    id = models.AutoField(primary_key=True)
    journey = models.ForeignKey('TrainJourney', on_delete=models.CASCADE)
    station = models.ForeignKey('TrainStation', on_delete=models.CASCADE)
    stop_order = models.IntegerField(blank=True, null=True)
    arrival_station = models.DateTimeField()
    departure_time = models.DateTimeField()

    def __str__(self):
        return f"Journey {self.journey} at {self.station}"

    class Meta:
        db_table = 'journey_station'
        constraints = [
            models.UniqueConstraint(fields=['journey', 'station'], name='unique_journey_station')
        ]


class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(unique=True, max_length=15)
    email_address = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'passenger'
        verbose_name_plural = 'Passengers'


class Seat(models.Model):
    train = models.ForeignKey('Train', on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    class_type = models.CharField(max_length=20)
    availability_status = models.CharField(max_length=255)

    def __str__(self):
        return f"Seat {self.seat_number} in {self.train}"

    class Meta:
        db_table = 'seat'
        verbose_name_plural = 'Seats'


class Train(models.Model):
    train_number = models.CharField(unique=True, max_length=25)
    train_name = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return self.train_name

    class Meta:
        db_table = 'train'
        verbose_name_plural = 'Trains'


class TrainJourney(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)

    def __str__(self):
        return f"Journey for {self.train}"

    class Meta:
        db_table = 'train_journey'
        verbose_name_plural = 'Train journeys'


class TrainStation(models.Model):
    station_name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.station_name

    class Meta:
        db_table = 'train_station'
        verbose_name_plural = 'Train stations'
