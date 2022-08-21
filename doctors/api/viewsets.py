from rest_framework.viewsets import ModelViewSet
from doctors.models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
