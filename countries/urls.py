from django.urls import path

from .views import (
    CountriesView,
    CountriesDatatableView
)

app_name = "countries"

urlpatterns = [
    path('', CountriesView.as_view(), name='index'),
    path('datatable/', CountriesDatatableView.as_view(), name='datatable'),
]
