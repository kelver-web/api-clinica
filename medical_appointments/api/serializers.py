from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from medical_appointments.models import MedicalAppointment
#from patients.api.serializers import PatientSerializer
#from doctors.api.serializers import DoctorSerializer


class MedicalAppointmentSerializer(ModelSerializer):
    doctor = SerializerMethodField()
    patient = SerializerMethodField()

    class Meta:
        model = MedicalAppointment
        fields = ('id', 'medical_appointment', 'doctor', 'patient', 'data',
                  'description', 'status')

    def get_doctor(self, obj):
        return f'{obj.doctor}'

    def get_patient(self, obj):
        return f'{obj.patient}'
