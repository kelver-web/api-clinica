from django.db import models
from doctors.models import Doctor
from patients.models import Patient
# Create your models here.


class MedicalAppointment(models.Model):

    STATUS = (
        ('realizada', 'Realizada'),
        ('aguardando', 'Aguardando'),
        ('negada', 'Negada')
    )
    id = models.AutoField(primary_key=True)
    medical_appointment = models.CharField(max_length=120)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    data = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
   
    def __str__(self):
        return self.medical_appointment
