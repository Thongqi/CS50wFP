from django.db import models
from mapbox_location_field.models import LocationField
from multiselectfield import MultiSelectField as MSField

class MultiSelectField(MSField):
    """
    Custom Implementation of MultiSelectField to achieve Django 5.0 compatibility

    See: https://github.com/goinnn/django-multiselectfield/issues/141#issuecomment-1911731471
    """

    def _get_flatchoices(self):
        flat_choices = super(models.CharField, self).flatchoices

        class MSFFlatchoices(list):
            # Used to trick django.contrib.admin.utils.display_for_field into not treating the list of values as a
            # dictionary key (which errors out)
            def __bool__(self):
                return False

            __nonzero__ = __bool__

        return MSFFlatchoices(flat_choices)

    flatchoices = property(_get_flatchoices)
# Create your models here.


# Create your models here.
class States(models.Model):
    states = models.CharField(max_length=30)
    recm_days = models.CharField(max_length=30)

    def __str__(self):
        return self.states

class Places(models.Model):
    name = models.CharField(max_length=50)
    location = LocationField()

    OPTIONS = (
        ("Nature", "Nature-Seeker"),
        ("Outdoor", "Outdoor"),
        ("Instagram", "Instagrammable"),
        ("Sporty", "Sporty"),
        ("Culture", "Culture"),
        ("Shopping", "Shopping"),
        ("Beach", "Beach"),
        ("Nightlife", "Nightlife"),
        ("Animal", "Animal"),
        ("Relax", "Relax"),
        ("History", "History"),
        ("Food", "Food"),
    )
    tags = MultiSelectField(choices = OPTIONS, max_length=200)
    must = models.BooleanField(null=True)

    DAYS = (
        ("MON", "Monday"),
        ("TUES", "Tuesday"),
        ("WED","Wednesday"),
        ("THU", "Thursday"),
        ("FRI", "Friday"),
        ("SAT", "Saturday"),
        ("SUN", "Sunday"),
        ("ALL", "Everyday"),
    )
    operating = MultiSelectField(choices = DAYS, max_length=100, blank = True)
    state = models.ForeignKey(States, on_delete=models.CASCADE, null=True)
    remarks = models.TextField(null=True)
    img = models.TextField(null=True)

    def __str__(self):
        return self.name
    
