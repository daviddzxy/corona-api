from django.contrib import admin
from .models import (Vaccine, VaccinationReport, Region, Hospital, District, City, HospitalStaffReport, PatientsReport,
    BedsReport)

admin.site.register([Vaccine, VaccinationReport, Region, Hospital, District, City, HospitalStaffReport, PatientsReport,
    BedsReport])
