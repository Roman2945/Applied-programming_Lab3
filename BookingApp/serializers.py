from rest_framework import serializers
from .models import BookingStatus, Passenger, Train, TrainStation, CarriageClass, Seat, TrainJourney, Booking, \
    JourneyStation


class BookingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingStatus
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'


class TrainStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainStation
        fields = '__all__'


class CarriageClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarriageClass
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class TrainJourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainJourney
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class JourneyStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JourneyStation
        fields = '__all__'
