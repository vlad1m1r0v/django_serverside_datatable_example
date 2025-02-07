from django.core.management.base import BaseCommand
from countries.models import Country

class Command(BaseCommand):
    help = "Populate the Country model with sample data"

    def handle(self, *args, **kwargs):
        countries = [
            Country(name="Ukraine", population=41000000, area=603628, gdp=200000000000),
            Country(name="United States", population=331000000, area=9833520, gdp=21400000000000),
            Country(name="Germany", population=83000000, area=357022, gdp=4200000000000),
            Country(name="France", population=67000000, area=551695, gdp=3100000000000),
            Country(name="Italy", population=59000000, area=301340, gdp=2000000000000),
            Country(name="Canada", population=38000000, area=9984670, gdp=1800000000000),
            Country(name="Brazil", population=213000000, area=8515767, gdp=1600000000000),
            Country(name="Japan", population=125000000, area=377975, gdp=5000000000000),
            Country(name="India", population=1390000000, area=3287263, gdp=2870000000000),
            Country(name="China", population=1410000000, area=9596961, gdp=14700000000000),
            Country(name="Australia", population=26000000, area=7692024, gdp=1400000000000),
            Country(name="Spain", population=47000000, area=505990, gdp=1400000000000),
            Country(name="Mexico", population=126000000, area=1964375, gdp=1200000000000),
            Country(name="Argentina", population=45000000, area=2780400, gdp=500000000000),
            Country(name="South Korea", population=52000000, area=100210, gdp=1800000000000),
            Country(name="United Kingdom", population=67000000, area=243610, gdp=2900000000000),
            Country(name="South Africa", population=59000000, area=1219090, gdp=350000000000),
            Country(name="Sweden", population=10300000, area=450295, gdp=540000000000),
            Country(name="Norway", population=5400000, area=323802, gdp=480000000000),
        ]

        Country.objects.bulk_create(countries, ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS("Successfully populated countries"))