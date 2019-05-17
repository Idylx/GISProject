from django.contrib.gis import admin
from .models import Restaurant, Grenouillere, Slope, Lift, Parking
# Register your models here.

admin.site.register(Lift, admin.OSMGeoAdmin)
admin.site.register(Restaurant,  admin.OSMGeoAdmin)
admin.site.register(Slope,  admin.OSMGeoAdmin)
admin.site.register(Grenouillere,  admin.OSMGeoAdmin)
admin.site.register(Parking,  admin.OSMGeoAdmin)


