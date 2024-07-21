from import_export import fields, resources 
from import_export.widgets import ForeignKeyWidget
from .models import States, Places

class PlacesResource(resources.ModelResource):
    state = fields.Field(
        column_name='state',
        attribute='state',
        widget=ForeignKeyWidget(States, field='states')
    )
    class Meta:
        model = Places
    