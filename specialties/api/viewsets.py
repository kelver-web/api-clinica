from rest_framework.viewsets import ModelViewSet
from specialties.models import Specialty
from .serializers import SpecialtySerializer


class SpecialtyViewSet(ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
