from django.db import models


class Region(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    code = models.CharField(max_length=5)
    abbreviation = models.CharField(max_length=2)


class Vaccine(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)


class VaccinationReport(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
    vaccine_id = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    dose1_count = models.PositiveIntegerField()
    dose2_count = models.PositiveIntegerField()
    updated_at = models.DateTimeField()
    published_on = models.DateField()


class District(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    code = models.CharField(max_length=6)


class City(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    district_id = models.ForeignKey(District, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    code = models.CharField(max_length=12)


class Hospital(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=16)


class HospitalStaffReport(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    hospital_id = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    out_of_work_ratio_doctor = models.FloatField()
    out_of_work_ratio_nurse = models.FloatField()
    out_of_work_ratio_other = models.FloatField()
    reported_at = models.DateTimeField
    updated_at = models.DateTimeField()
    published_on = models.DateField()


class PatientsReport(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    hospital_id = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    ventilated_covid = models.PositiveIntegerField()
    non_covid = models.PositiveIntegerField()
    confirmed_covid = models.PositiveIntegerField()
    suspected_covid = models.PositiveIntegerField()
    reported_at = models.DateTimeField
    updated_at = models.DateTimeField()
    published_on = models.DateField()


class BedsReport(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    hospital_id = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    capacity_all = models.PositiveIntegerField()
    free_all = models.PositiveIntegerField()
    capacity_covid = models.PositiveIntegerField()
    occupied_jis_covid = models.PositiveIntegerField()
    occupied_oaim_covid = models.PositiveIntegerField()
    occupied_o2_covid = models.PositiveIntegerField()
    occupied_other_covid = models.PositiveIntegerField()
    reported_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    published_on = models.DateField()


class AgTestsReport(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    district_id = models.ForeignKey(District, on_delete=models.CASCADE)
    positivity_rate = models.FloatField()
    positives_count = models.PositiveIntegerField()
    negatives_count = models.PositiveIntegerField()
    positives_sum = models.PositiveIntegerField()
    negatives_sum = models.PositiveIntegerField()
    updated_at = models.DateTimeField()
    published_on = models.DateField()
