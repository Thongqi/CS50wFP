from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("qa/", views.qa, name="qa"),
    path("what-to-wear", views.ui, name="ui"),
    path("language/", TemplateView.as_view(template_name="language.html"), name="language"),
    

    
    # API
    path("places", views.places, name="places"),
]