from rest_framework.viewsets import ModelViewSet
from medical_appointments.models import MedicalAppointment
from .serializers import MedicalAppointmentSerializer


class MedicalAppointmentsViewSet(ModelViewSet):
    queryset = MedicalAppointment.objects.all()
    serializer_class = MedicalAppointmentSerializer
    


    def list(self, request, *args, **kwargs):  # Sobrescrevendo o metodo list
        return super(MedicalAppointmentsViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(MedicalAppointmentsViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(MedicalAppointmentsViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(MedicalAppointmentsViewSet, self).destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(MedicalAppointmentsViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        pass
