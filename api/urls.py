from django.urls import path
from .views import VaccineList

urlpatterns = [
    path('vaccines/', VaccineList.as_view())
]