from rest_framework import serializers
import models


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vaccine
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = '__all__'


class AgTestsReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AgTestsReport
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hospital
        fields = '__all__'


class HospitalStaffReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HospitalStaffReport
        fields = '__all__'


class BedsReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BedsReport
        fields = '__all__'


class PatientsReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PatientsReport
        fields = '__all__'


class VaccinationReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VaccinationReport
        fields = '__all__'
