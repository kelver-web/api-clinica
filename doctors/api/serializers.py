from rest_framework.serializers import ModelSerializer
from doctors.models import Doctor
#from clinics.api.serializers import ClinicsSerializer
#from specialties.api.serializers import SpecialtySerializer


class DoctorSerializer(ModelSerializer):
#    clinic = ClinicsSerializer(read_only=True)
#    specialty = SpecialtySerializer(read_only=True)
    
    class Meta:
        model = Doctor
        fields = ('name', 'crm', 'specialty', 'clinic', 'phone')
