from rest_framework.serializers import ModelSerializer
from api.models.company import Company


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']
