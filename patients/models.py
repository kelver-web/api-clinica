from django.db import models

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=7)
    birth_date = models.DateField()
    phone = models.CharField(max_length=11)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return self.name
