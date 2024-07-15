from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("qa/", views.qa, name="qa"),
    path("what-to-wear", views.ui, name="ui"),
    path("language/", TemplateView.as_view(template_name="language.html"), name="language"),
    path("transport/", TemplateView.as_view(template_name="transport.html"), name="transport"),
    path("cash-or-card/", TemplateView.as_view(template_name="cash_or_card.html"), name="cash_or_card"),
    path("what-to-wear/", TemplateView.as_view(template_name="what-to-wear.html"), name="what-to-wear"),
    

    
    # API
    path("places", views.places, name="places"),
]