from django.db import models

# Create your models here.

class Clinic(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    cep = models.IntegerField()
    social_reason = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Clinica'
        verbose_name_plural = 'Clinicas'

    def __str__(self):
        return self.name

