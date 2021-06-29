from django.contrib import admin
from .models import Vaccine, VaccinationReport, Region
# Register your models here.

admin.site.register([Vaccine, VaccinationReport, Region])