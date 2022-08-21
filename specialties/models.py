from django.db import models

# Create your models here.


class Specialty(models.Model):
    name = models.CharField(max_length=70)

    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.name
