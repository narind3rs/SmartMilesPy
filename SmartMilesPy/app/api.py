from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import *
from .models import *

class WaypointViewSet(ModelViewSet):
	queryset = Waypoint.objects.all()
	serializer_class = WaypointSerializer
	permission_classes = (permissions.IsAuthenticated, )


class TripViewSet(ModelViewSet):
	queryset = Trip.objects.all()
	serializer_class = TripSerializer
	permission_classes = (permissions.IsAuthenticated, )


class AddressViewSet(ModelViewSet):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
	permission_class = (permissions.IsAuthenticated, )


class PayRateViewSet(ModelViewSet):
	queryset = PayRate.objects.all()
	serializer_class = PayRateSerializer
	permission_class = (permissions.IsAuthenticated, )


class WarrantyAdminViewSet(ModelViewSet):
	queryset = WarrantyAdmin.objects.all()
	serializer_class = WarrantyAdminSerializer
	permission_class = (permissions.IsAuthenticated, )


class WarrantyViewSet(ModelViewSet):
	queryset = Warranty.objects.all()
	serializer_class = WarrantySerializer
	permission_class = (permissions.IsAuthenticated, )


class LicensePlateViewSet(ModelViewSet):
	queryset = LicensePlate.objects.all()
	serializer_class = LicensePlateSerializer
	permission_class = (permissions.IsAuthenticated, )


class OdometerViewSet(ModelViewSet):
	queryset = Odometer.objects.all()
	serializer_class = OdometerSerializer
	permission_class = (permissions.IsAuthenticated, )


class TruckViewSet(ModelViewSet):
	queryset = Truck.objects.all()
	serializer_class = TruckSerializer
	permission_class = (permissions.IsAuthenticated, )


class ContactInfoViewSet(ModelViewSet):
	queryset = ContactInfo.objects.all()
	serializer_class = ContactInfo
	permission_class = (permissions.IsAuthenticated, )


class ContactViewSet(ModelViewSet):
	queryset = Contact.objects.all()
	serializer_class = Contact
	permission_class = (permissions.IsAuthenticated, )


class CompanyViewSet(ModelViewSet):
	queryset = Company.objects.all()
	serializer_class = Company
	permission_class = (permissions.IsAuthenticated, )


class DrivingLicenseViewSet(ModelViewSet):
	queryset = DrivingLicense.objects.all()
	serializer_class = DrivingLicenseSerializer
	permission_class = (permissions.IsAuthenticated, )


class DriverViewSet(ModelViewSet):
	queryset = Driver.objects.all()
	serializer_class = DriverSerializer
	permission_class = (permissions.IsAuthenticated, )


class DriverPayViewSet(ModelViewSet):
	queryset = DriverPay.objects.all()
	serializer_class = DriverPaySerializer
	permission_class = (permissions.IsAuthenticated, )

class RoadIncidentViewSet(ModelViewSet):
	queryset = RoadIncident.objects.all()
	serializer_class = RoadIncidentSerializer
	permission_class = (permissions.IsAuthenticated, )

