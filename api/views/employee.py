from rest_framework.viewsets import ModelViewSet
from api.serializers.employee import EmployeeSerializer
from api.models import Employee


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
