from rest_framework.serializers import ModelSerializer
from api.models import Employee


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'last_name', 'first_name', 'middle_name', 'company']
