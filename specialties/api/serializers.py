from dataclasses import field
from rest_framework.serializers import ModelSerializer
from specialties.models import Specialty


class SpecialtySerializer(ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'
