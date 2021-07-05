from django.urls import path
from . import views

urlpatterns = [
    path('vaccines/', views.VaccineListView.as_view()),
    path('regions/', views.RegionListView.as_view()),
    path('hospitals/', views.HospitalListView.as_view()),
    path('districts/', views.DistrictListView.as_view()),
    path('cities/', views.CityListView.as_view()),
    path('agtestreports/', views.AgTestsReportView.as_view()),
    path('bedsreports/', views.BedsReportView.as_view()),
    path('hospitalstaffreports/', views.HospitalStaffReportView.as_view()),
    path('patientsreports/', views.PatientsReportView.as_view()),
    path('vaccinationreports/', views.VaccinationReportView.as_view()),
    path('vaccines/<int:pk>/vaccination-reports', views.VaccineVaccinationReport.as_view())
]