from django.db import models
from specialties.models import Specialty
from clinics.models import Clinic

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=70)
    crm = models.CharField(max_length=70)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
    
    def __str__(self):
        return self.name
