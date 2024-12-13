from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BookingStatus, Passenger, Train, TrainStation, CarriageClass, Seat, TrainJourney, Booking, JourneyStation
from .serializers import BookingStatusSerializer, PassengerSerializer, TrainSerializer, TrainStationSerializer, CarriageClassSerializer, SeatSerializer, TrainJourneySerializer, BookingSerializer, JourneyStationSerializer
from .repositories import ReportRepository
from rest_framework.permissions import IsAuthenticated


class BookingStatusViewSet(viewsets.ModelViewSet):
    queryset = BookingStatus.objects.all()
    serializer_class = BookingStatusSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer


class TrainStationViewSet(viewsets.ModelViewSet):
    queryset = TrainStation.objects.all()
    serializer_class = TrainStationSerializer


class CarriageClassViewSet(viewsets.ModelViewSet):
    queryset = CarriageClass.objects.all()
    serializer_class = CarriageClassSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class TrainJourneyViewSet(viewsets.ModelViewSet):
    queryset = TrainJourney.objects.all()
    serializer_class = TrainJourneySerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class JourneyStationViewSet(viewsets.ModelViewSet):
    queryset = JourneyStation.objects.all()
    serializer_class = JourneyStationSerializer


class BookingReportView(APIView):
    def get(self, request):
        report_data = ReportRepository.get_booking_summary()
        return Response(report_data)
