from .api import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'waypoints', WaypointViewSet)
router.register(r'trips', TripViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'payrates', PayRateViewSet)
router.register(r'warrantyadmins', WarrantyAdminViewSet)
router.register(r'warranties', WarrantyViewSet)
router.register(r'licenseplates', LicensePlateViewSet)
router.register(r'odometers', OdometerViewSet)
router.register(r'trucks', TruckViewSet)
router.register(r'contactinfos', ContactInfoViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'drivinglicenses', DrivingLicenseViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'driverpays', DriverPayViewSet)
router.register(r'incidents', RoadIncidentViewSet)

urlpatterns = router.urls
