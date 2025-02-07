from ajax_datatable import AjaxDatatableView
from django.views.generic import TemplateView

from .models import Country


class CountriesView(TemplateView):
    template_name = 'countries.html'


class CountriesDatatableView(AjaxDatatableView):
    model = Country

    column_defs = [
        {
            'name': 'name',
        },
        {
            'name': 'area',
        },
        {
            'name': 'population',
        },
        {
            'name': 'gdp',
        }
    ]

    def get_initial_queryset(self, request=None):
        return self.model.objects.all()

    def filter_queryset(self, params, qs):
        name = self.request.GET.get('name')
        qs = qs.filter(name__icontains=name)
        return qs
