from rest_framework.viewsets import ModelViewSet
from api.serializers.company import CompanySerializer
from api.models import Company


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
