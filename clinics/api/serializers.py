from dataclasses import field
from rest_framework.serializers import ModelSerializer
from clinics.models import Clinic

class ClinicsSerializer(ModelSerializer):
    class Meta:
        model = Clinic
        fields = ('name', 'address', 'number', 'cep', 'social_reason')
