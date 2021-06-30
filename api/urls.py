from django.urls import path
from .views import VaccineListView, RegionListView, HospitalListView, DistrictListView, CityListView

urlpatterns = [
    path('vaccines/', VaccineListView.as_view()),
    path('regions/', RegionListView.as_view()),
    path('hospitals/', HospitalListView.as_view()),
    path('districts/', DistrictListView.as_view()),
    path('cities/', CityListView.as_view()),

]