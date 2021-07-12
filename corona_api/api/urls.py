from django.urls import path
from . import views

urlpatterns = [
    path('vaccines/', views.VaccineListView.as_view()),
    path('regions/', views.RegionListView.as_view()),
    path('hospitals/', views.HospitalListView.as_view()),
    path('districts/', views.DistrictListView.as_view()),
    path('cities/', views.CityListView.as_view()),
    path('ag-test-reports/', views.AgTestsReportView.as_view()),
    path('beds-reports/', views.BedsReportView.as_view()),
    path('hospital-staff-reports/', views.HospitalStaffReportView.as_view()),
    path('patients-reports/', views.PatientsReportView.as_view()),
    path('vaccination-reports/', views.VaccinationReportView.as_view())
]
