from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    population = models.BigIntegerField()
    area = models.IntegerField()
    gdp = models.BigIntegerField()

    def __str__(self):
        return self.name