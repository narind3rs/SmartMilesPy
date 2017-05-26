from rest_framework import serializers

from .models import *

class WaypointSerializer(serializers.ModelSerializer):	
	class Meta:
		model = Waypoint
		fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = '__all__'


class PayRateSerializer(serializers.ModelSerializer):
	class Meta:
		model = PayRate
		fields = '__all__'


class WarrantyAdminSerializer(serializers.ModelSerializer):
	class Meta:
		model = WarrantyAdmin
		fields = '__all__'


class WarrantySerializer(serializers.ModelSerializer):
	warranty_admin = WarrantyAdminSerializer()
	class Meta:
		model = Warranty
		fields = '__all__'


class LicensePlateSerializer(serializers.ModelSerializer):
	class Meta:
		model = LicensePlate
		fields = '__all__'


class OdometerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Odometer
		fields = '__all__'

class TruckSerializer(serializers.ModelSerializer):
	
	license_plate = LicensePlateSerializer()
	warranties = WarrantySerializer(many = True)
	odometer = OdometerSerializer(many = True)

	class Meta:
		model = Truck
		fields = '__all__'


class ContactInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ContactInfo
		fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
	contact_info = ContactInfoSerializer()
	class Meta:
		model = Contact
		fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = '__all__'


class DrivingLicenseSerializer(serializers.ModelSerializer):
	class Meta:
		model = DrivingLicense
		fields = '__all__'


class DriverPaySerializer(serializers.ModelSerializer):
	#driver = DriverSerializer()
	class Meta:
		model = DriverPay
		fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
	contact_info	= ContactInfoSerializer()
	company = CompanySerializer()
	driving_license = DrivingLicenseSerializer()
	emergency_contact = ContactSerializer()
	assigned_truck = TruckSerializer()
	pay_rate = DriverPaySerializer()
	employment_reference = ContactSerializer()
	class Meta:
		model = Driver
		fields = '__all__'


class RoadIncidentSerializer(serializers.ModelSerializer):
	class Meta:
		model = RoadIncident
		fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
	stops = WaypointSerializer(many = True)
	drivers = DriverSerializer(many = True)
	class Meta:
		model = Trip
		fields = '__all__'
