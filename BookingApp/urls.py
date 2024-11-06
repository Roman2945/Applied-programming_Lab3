from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingStatusViewSet, PassengerViewSet, TrainViewSet, TrainStationViewSet, CarriageClassViewSet, \
    SeatViewSet, TrainJourneyViewSet, BookingViewSet, JourneyStationViewSet, BookingReportView


router = DefaultRouter()
router.register(r'booking-status', BookingStatusViewSet)
router.register(r'passengers', PassengerViewSet)
router.register(r'trains', TrainViewSet)
router.register(r'train-stations', TrainStationViewSet)
router.register(r'carriage-classes', CarriageClassViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'train-journeys', TrainJourneyViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'journey-stations', JourneyStationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/booking-report/', BookingReportView.as_view(), name='booking-report'),

]
