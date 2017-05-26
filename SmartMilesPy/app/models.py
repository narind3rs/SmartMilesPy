"""
Definition of models.
"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

SHORTSTR = 16
LONGSTR = 64

@python_2_unicode_compatible
class Address(models.Model):

	address_line_1 = models.CharField(max_length = LONGSTR)
	address_line_2 = models.CharField(max_length = LONGSTR, blank = True)
	city = models.CharField(max_length = LONGSTR)
	state = models.CharField(max_length = SHORTSTR)
	postal_code = models.CharField(max_length = SHORTSTR, blank = True)
	country = models.CharField(max_length = SHORTSTR)

	def __str__(self):
		return self.address_line_1


	
@python_2_unicode_compatible
class WarrantyAdmin(models.Model):

	name = models.CharField(max_length = LONGSTR)
	dba = models.CharField(max_length = LONGSTR, blank = True)
	contact_name = models.CharField(max_length = LONGSTR, blank = True)
	primary_phone = PhoneNumberField(blank = True, null = True)
	secondary_phone = PhoneNumberField(blank = True, null = True)
	fax = PhoneNumberField(blank = True, null = True)
	#address = models.ForeignKey(Address, related_name='address', null = True)
	address_line_1 = models.CharField(max_length = LONGSTR)
	address_line_2 = models.CharField(max_length = LONGSTR, blank = True)
	city = models.CharField(max_length = LONGSTR)
	state = models.CharField(max_length = SHORTSTR)
	postal_code = models.CharField(max_length = SHORTSTR, blank = True)
	country = models.CharField(max_length = SHORTSTR)

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class PayRate(models.Model):
	HOURLY = 'Per Hour'
	PER_MILE = 'Per Mile'
	OTHER = 'Other'

	RATE_TYPES = (
		(HOURLY, 'Hourly'),
		(PER_MILE, 'Per Mile'),
	    (OTHER, 'Other'))

	pay_rate = models.DecimalField(verbose_name = 'Rate', decimal_places = 2, max_digits = 6)
	type = models.CharField(max_length = 8, choices = RATE_TYPES)

	def __str__(self):
		return "{0} {1}".format(self.pay_rate, self.type)


@python_2_unicode_compatible
class Warranty(models.Model):
	MANUFACTURER = 'MN'
	DEALER = 'DL'
	THIRD_PARTY = 'TP'

	WARR_TYPE_CHOICES = (
		(MANUFACTURER, 'Manufacturer'),
		(DEALER, 'Dealer'),
		(THIRD_PARTY, 'Third Party')
		)

	name = models.CharField(max_length = SHORTSTR, blank = False, default = 'None')
	warranty_type = models.CharField(max_length = 2,
								  choices = WARR_TYPE_CHOICES,
								  blank = True)
	effective_date = models.DateField(blank = True)
	expiration_date = models.DateField(blank = True)
	expiry_odometer = models.CharField(max_length = 8, blank = True)
	notes = models.TextField(blank = True)
	warranty_admin = models.ForeignKey(WarrantyAdmin, related_name='warranty_admin')

	def __str__(self, **kwargs):
		return self.name



@python_2_unicode_compatible
class LicensePlate(models.Model):
	
	state = models.CharField(max_length = SHORTSTR)
	number = models.CharField(max_length = SHORTSTR)
	expiration_date = models.DateField(blank = True, null = True)

	def __str__(self):
		return '{1} - {0}'.format(self.number, self.state)
	

@python_2_unicode_compatible
class Odometer(models.Model):
	MILES = 'miles'
	KMS = 'kms'

	ODO_UNIT_CHOICES = ( (MILES, 'Miles'), (KMS, 'Kilometers') )
	
	units = models.CharField(max_length = SHORTSTR, choices = ODO_UNIT_CHOICES, default = KMS)
	reading = models.IntegerField()
	reading_date = models.DateField(auto_now_add = True)

	def __str__(self):
		return 'Odometer: {0} - {1}'.format(self.reading_date, self.reading)



@python_2_unicode_compatible
class Truck(models.Model):	
	"""
	This class will represent the truck model
	"""
	name = models.CharField(max_length = SHORTSTR)
	make = models.CharField(max_length = SHORTSTR)
	model = models.CharField(max_length = SHORTSTR)
	model_year = models.IntegerField(null = True)
	color = models.CharField(max_length = SHORTSTR, blank = True)
	vin = models.CharField(max_length = SHORTSTR, blank = True)
	purchase_date = models.DateField(blank = True, null = True)
	safety_expiration_date = models.DateField(blank = True, null = True)
	emissions_expiration_date = models.DateField(blank = True, null = True)
	retire_date = models.DateField(blank = True, null = True)
	license_plate = models.ForeignKey(LicensePlate, related_name = 'license_plate')
	warranties = models.ManyToManyField(Warranty)
	odometer = models.ManyToManyField(Odometer)
	notes = models.TextField(blank = True)
		
	def __str__(self):
		return "{}".format(self.name)


@python_2_unicode_compatible
class ContactInfo(models.Model):
	preferred_name = models.CharField(max_length = LONGSTR, blank = True, null = True)
	primary_phone = PhoneNumberField(null = True, unique = True, blank = True)
	seondary_phone = PhoneNumberField(blank = True, null = True)
	#address = models.ForeignKey(Address, related_name = 'contact_address', null = True)
	address_line_1 = models.CharField(max_length = LONGSTR)
	address_line_2 = models.CharField(max_length = LONGSTR, blank = True)
	city = models.CharField(max_length = LONGSTR)
	state = models.CharField(max_length = SHORTSTR)
	postal_code = models.CharField(max_length = SHORTSTR, blank = True)
	country = models.CharField(max_length = SHORTSTR)
	email_address = models.EmailField()

	def __str__(self):
		return '{0} {1}'.format(self.preferred_name, str(self.primary_phone))


@python_2_unicode_compatible
class Contact(models.Model):
	first_name = models.CharField(max_length = LONGSTR)
	last_name = models.CharField(max_length = LONGSTR)
	relationship = models.CharField(max_length = SHORTSTR)	
	contact_info = models.ForeignKey(ContactInfo, related_name = 'contact_info', null = True)
	def __str__(self):
		return "{0} {1}".format(self.first_name, self.last_name)



@python_2_unicode_compatible
class Company(models.Model):
	name = models.CharField(max_length = LONGSTR)
	type = models.CharField(max_length = LONGSTR)
	tax_identifier = models.CharField(max_length = LONGSTR)
	#address = models.ForeignKey(Address, related_name = 'company_address', null = True)
	address_line_1 = models.CharField(max_length = LONGSTR)
	address_line_2 = models.CharField(max_length = LONGSTR, blank = True)
	city = models.CharField(max_length = LONGSTR)
	state = models.CharField(max_length = SHORTSTR)
	postal_code = models.CharField(max_length = SHORTSTR, blank = True)
	country = models.CharField(max_length = SHORTSTR)
	notes = models.TextField(blank = True)

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class DrivingLicense(models.Model):
	number = models.CharField(max_length = SHORTSTR)
	lic_class = models.CharField(max_length = SHORTSTR)
	date_of_birth = models.DateField()
	issue_state = models.CharField(max_length = SHORTSTR)
	issue_date = models.DateField()
	expiration_date = models.DateField()

	def __str__(self):
		return self.number


@python_2_unicode_compatible
class DriverPay(models.Model):
	rate = models.ForeignKey(PayRate, related_name = 'rate')
	start_date = models.DateField(auto_now = False)
	end_date = models.DateField(blank = True, null = True)
	#driver = models.ForeignKey(Driver, related_name='driver')

	def __str__(self):
		return 'Rate as of: {0} at {1}'.format(self.start_date, self.rate)
	

@python_2_unicode_compatible
class Driver(models.Model):
	
	first_name = models.CharField(max_length = LONGSTR)
	middle_name = models.CharField(max_length = LONGSTR, blank = True)
	last_name = models.CharField(max_length = LONGSTR)
	contact_info = models.ForeignKey(ContactInfo, related_name='driver_contact_info')
	#address = models.ForeignKey(Address, related_name='driver_address')
	company = models.ForeignKey(Company, related_name='driver_company')
	driving_license = models.ForeignKey(DrivingLicense, related_name='license')
	emergency_contact = models.ForeignKey(Contact, related_name='emergency_contact', null = True)
	assigned_truck = models.ForeignKey(Truck, related_name='assigned_truck', null = True)
	is_available = models.BooleanField(default = True)
	start_date = models.DateField(auto_now_add = True, blank = True)
	
	pay_rate = models.ForeignKey(DriverPay, related_name = 'driver_pay_rate')
	
	terminate_date = models.DateField(null = True, blank = True)
	employment_reference = models.ForeignKey(Contact, related_name = 'employment_reference', null = True)
	notes = models.TextField(blank = True)

	def __str__(self):
		return "{0} {1} {2}".format(self.first_name, self.middle_name, self.last_name)



@python_2_unicode_compatible
class Waypoint(models.Model):
	
	name = models.CharField(max_length = LONGSTR)
	address_line_1 = models.CharField(max_length = LONGSTR)
	address_line_2 = models.CharField(max_length = LONGSTR, blank = True)
	city = models.CharField(max_length = LONGSTR)
	state = models.CharField(max_length = SHORTSTR)
	postal_code = models.CharField(max_length = SHORTSTR, blank = True)
	country = models.CharField(max_length = SHORTSTR)
	latitude = models.DecimalField(max_digits = 12, decimal_places = 10, blank = True, null = True)
	longitude = models.DecimalField(max_digits = 12, decimal_places = 10, blank = True, null = True)
	notes = models.TextField(blank = True)

	def __str__(self):
		return '{0} {1} {2} {3}'.format(self.name, self.address_line_1, self.city, self.state)


@python_2_unicode_compatible
class Trip(models.Model):

	PLANNED = 1
	IN_PROGRESS = 2
	COMPLETE = 3
	CANCELED = 4

	STATUS_CHOICES = (
		(PLANNED, 'Planned'),
		(IN_PROGRESS, 'In Progress'),
		(COMPLETE, 'Complete'),
		(CANCELED, 'Canceled')
		)

	name = models.CharField(max_length = LONGSTR)
	start_date = models.DateField(auto_now_add = False, blank = True, null = True)
	end_date = models.DateField(auto_now_add = False, blank = True, null = True)
	truck = models.ForeignKey(Truck, related_name = 'truck')
	stops = models.ManyToManyField(Waypoint)
	total_mileage = models.DecimalField(max_digits = 7, decimal_places = 2)
	status = models.IntegerField(choices = STATUS_CHOICES, default = PLANNED)
	notes = models.TextField(blank = True)
	drivers = models.ManyToManyField(Driver)

	def __str__(self):
		return '{0} ({1})'.format(self.name, self.notes)


@python_2_unicode_compatible
class RoadIncident(models.Model):
	trip = models.ForeignKey(Trip, related_name = 'incident_trip')
	description = models.TextField(blank = False)
	incident_date_time = models.DateTimeField(null = True, blank = True)

