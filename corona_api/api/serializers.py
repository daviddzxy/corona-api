from rest_framework import serializers
from rest_framework.serializers import Serializer, IntegerField, CharField, DateTimeField, DateField, FloatField
from . import models


class VaccineSerializer(Serializer):
    id = IntegerField()
    title = CharField()
    manufacturer = CharField()


class RegionSerializer(Serializer):
    id = IntegerField()
    title = CharField()
    code = CharField()
    abbreviation = CharField()


class DistrictSerializer(Serializer):
    id = IntegerField()
    region_id = IntegerField()
    title = CharField()
    code = CharField()


class CitySerializer(Serializer):
    id = IntegerField()
    district_id = IntegerField()
    title = CharField()
    code = CharField()


class HospitalSerializer(Serializer):
    id = IntegerField()
    city_id = IntegerField()
    title = CharField()
    code = CharField()


class AgTestsReportSerializer(Serializer):
    id = IntegerField()
    district_id = IntegerField()
    positivity_rate = FloatField()
    positives_count = IntegerField()
    negatives_count = IntegerField()
    positives_sum = IntegerField()
    negatives_sum = IntegerField()
    updated_at = DateTimeField('%Y-%m-%d %H:%M:%S')
    published_on = DateField()


class HospitalStaffReportSerializer(serializers.Serializer):
    id = IntegerField()
    hospital_id = IntegerField()
    out_of_work_ratio_doctor = FloatField()
    out_of_work_ratio_nurse = FloatField()
    out_of_work_ratio_other = FloatField()
    reported_at = DateTimeField('%Y-%m-%d %H:%M:%S')
    updated_at = DateTimeField('%Y-%m-%d %H:%M:%S')
    published_on = DateField()


class BedsReportSerializer(serializers.Serializer):
    id = IntegerField()
    hospital_id = IntegerField()
    capacity_all = IntegerField()
    free_all = IntegerField()
    capacity_covid = IntegerField()
    occupied_jis_covid = IntegerField()
    occupied_oaim_covid = IntegerField()
    occupied_o2_covid = IntegerField()
    occupied_other_covid = IntegerField()
    reported_at = DateTimeField('%Y-%m-%d %H:%M:%S')
    updated_at = DateTimeField('%Y-%m-%d %H:%M:%S')
    published_on = DateField()


class PatientsReportSerializer(serializers.Serializer):
    id = IntegerField()
    hospital_id = IntegerField()
    ventilated_covid = IntegerField()
    non_covid = IntegerField()
    confirmed_covid = IntegerField()
    suspected_covid = IntegerField()
    reported_at = DateTimeField('%Y-%m-%d %H:%M:%S')
    updated_at = DateTimeField('%Y-%m-%d %H:%M:%S')
    published_on = DateField()


class VaccinationReportSerializer(serializers.Serializer):
    id = CharField()
    region_id = IntegerField()
    vaccine_id = IntegerField()
    dose1_count = IntegerField()
    dose2_count = IntegerField()
    updated_at = DateTimeField('%Y-%m-%d %H:%M:%S')
    published_on = DateField()

