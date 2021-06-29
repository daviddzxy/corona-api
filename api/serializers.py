from rest_framework import serializers
from .models import Vaccine, Region, VaccinationReport


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class VaccinationReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationReport
        fields = '__all__'