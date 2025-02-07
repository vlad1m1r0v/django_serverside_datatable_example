from ajax_datatable import AjaxDatatableView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from .forms import CountryForm
from .models import Country


class CountriesListView(TemplateView):
    template_name = 'list.html'


class CountriesDatatableView(AjaxDatatableView):
    model = Country

    column_defs = [
        {'name': 'id','visible': False},
        {'name': 'name'},
        {'name': 'area'},
        {'name': 'population'},
        {'name': 'gdp'}
    ]

    def get_initial_queryset(self, request=None):
        return self.model.objects.all()

    def filter_queryset(self, params, qs):
        name = self.request.GET.get('name')
        qs = qs.filter(name__icontains=name)
        return qs

class CountriesUpdateView(UpdateView):
    template_name = 'update.html'
    model = Country
    form_class = CountryForm
    success_url = reverse_lazy('countries:index')