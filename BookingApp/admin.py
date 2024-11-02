from django.contrib import admin
from .models import BookingStatus, Passenger, Train, TrainStation, CarriageClass, Seat, TrainJourney, Booking, \
    JourneyStation


class BookingStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_name')
    search_fields = ('status_name',)


class PassengerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'email_address')
    search_fields = ('first_name', 'last_name', 'phone_number')


class TrainAdmin(admin.ModelAdmin):
    list_display = ('id', 'train_number', 'train_name')
    search_fields = ('train_number', 'train_name')


class TrainStationAdmin(admin.ModelAdmin):
    list_display = ('id', 'station_name')
    search_fields = ('station_name',)


class CarriageClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_name', 'seating_capacity')
    search_fields = ('class_name',)


class SeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'train', 'seat_number', 'class_type', 'availability_status')
    search_fields = ('train', 'seat_number', 'class_type')


class TrainJourneyAdmin(admin.ModelAdmin):
    list_display = ('id', 'train')
    search_fields = ('train',)


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'passenger', 'status', 'starting_station', 'ending_station',
        'train_journey', 'ticket_class', 'seat', 'booking_date', 'amount_paid'
    )
    search_fields = ('passenger', 'status', 'starting_station', 'ending_station')


class JourneyStationAdmin(admin.ModelAdmin):
    list_display = ('id', 'journey', 'station', 'stop_order', 'arrival_station', 'departure_time')
    search_fields = ('journey', 'station')


admin.site.register(BookingStatus, BookingStatusAdmin)
admin.site.register(Passenger, PassengerAdmin)
admin.site.register(Train, TrainAdmin)
admin.site.register(TrainStation, TrainStationAdmin)
admin.site.register(CarriageClass, CarriageClassAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(TrainJourney, TrainJourneyAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(JourneyStation, JourneyStationAdmin)
