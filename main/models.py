from django.db import models
from django.utils import timezone

# Create your models here.


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    center = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Hospitals'

    def __str__(self):
        return f'{self.name}'


class Appointment(models.Model):
    hospital = models.ForeignKey(Hospital, default=1, verbose_name='Hospital', on_delete=models.SET_DEFAULT)
    when = models.DateTimeField(default=timezone.now)

    male = 'M'
    female = 'F'
    GENDER_CHOICES = [
        (male, 'Male'),
        (female, 'Female')]

    patient_code = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    insurance_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField(default='2000-1-20')
    home_address = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    home_number = models.CharField(max_length=20, blank=True)
    work_number = models.CharField(max_length=20, blank=True)
    allergies = models.TextField(max_length=200, blank=True)
    chronic_diseases = models.TextField(max_length=200, blank=True)
    other_medical_info = models.TextField(max_length=200, blank=True)
