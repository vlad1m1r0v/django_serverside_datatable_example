from django.urls import path

from .views import (
    CountriesListView,
    CountriesDatatableView,
    CountriesUpdateView,
    countries_delete_view
)

app_name = "countries"

urlpatterns = [
    path('', CountriesListView.as_view(), name='index'),
    path('<int:pk>/update/', CountriesUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', countries_delete_view, name='delete'),
    path('datatable/', CountriesDatatableView.as_view(), name='datatable'),
]
