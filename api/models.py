from django.db import models


class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    code = models.CharField(max_length=5)
    abbreviation = models.CharField(max_length=2)


class Vaccine(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)


class VaccinationReport(models.Model):
    id = models.IntegerField(primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    dose1_count = models.IntegerField()
    dose2_count = models.IntegerField()
    updated_at = models.DateTimeField()
    published_on = models.DateTimeField()
