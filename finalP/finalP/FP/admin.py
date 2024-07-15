from django.contrib import admin
from .models import States, Places
from mapbox_location_field.admin import MapAdmin
from import_export.admin import ImportExportModelAdmin
from .resource import PlacesResource
# Register your models here.
admin.site.register(States)
admin.site.register(Places, MapAdmin)
class PlacesList(Places):
    class Meta:
        proxy = True

class PlacesAdmin(ImportExportModelAdmin):
    resource_class = PlacesResource

admin.site.register(PlacesList, PlacesAdmin)

