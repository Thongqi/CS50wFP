from import_export import resources 
from .models import States, Places

class PlacesResource(resources.ModelResource):
    class Meta:
        model = Places