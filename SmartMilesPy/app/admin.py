from django.contrib import admin

from .models import Address, WarrantyAdmin, Warranty, LicensePlate, Truck, DrivingLicense, PayRate, Driver, Contact, ContactInfo, Company, Odometer, Trip, Waypoint, RoadIncident, DriverPay

admin.site.register(Address)
admin.site.register(WarrantyAdmin)
admin.site.register(Warranty)
admin.site.register(LicensePlate)
admin.site.register(Truck)
admin.site.register(DrivingLicense)
admin.site.register(PayRate)
admin.site.register(Contact)
admin.site.register(ContactInfo)
admin.site.register(Driver)
admin.site.register(Company)
admin.site.register(Odometer)
admin.site.register(RoadIncident)
admin.site.register(Waypoint)
admin.site.register(Trip)
admin.site.register(DriverPay)