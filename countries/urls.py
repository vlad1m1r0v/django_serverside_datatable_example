from django.urls import path

from .views import (
    CountriesListView,
    CountriesDatatableView,
    CountriesUpdateView
)

app_name = "countries"

urlpatterns = [
    path('', CountriesListView.as_view(), name='index'),
    path('<int:pk>/update/', CountriesUpdateView.as_view(), name='update'),
    path('datatable/', CountriesDatatableView.as_view(), name='datatable'),
]
