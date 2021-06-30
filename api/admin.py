from django.contrib import admin
from .models import Vaccine, VaccinationReport, Region

admin.site.register([Vaccine, VaccinationReport, Region])
