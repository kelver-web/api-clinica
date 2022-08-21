from rest_framework.viewsets import ModelViewSet
from clinics.models import Clinic
from .serializers import ClinicsSerializer


class ClinicsViewSet(ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicsSerializer
