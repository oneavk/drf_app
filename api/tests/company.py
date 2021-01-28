from rest_framework import status
from rest_framework.test import APITestCase
from api.models.company import Company

company_list = [
    {"id": 1, "name": "first company"}
]


class CompanyTestCase(APITestCase):
    def setUp(self) -> None:
        company = Company()
        company.name = company_list[0]['name']
        company.save()

    def test_list(self) -> None:
        response = self.client.get('/api/companies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, company_list)

    def test_retrieve(self) -> None:
        response = self.client.get('/api/companies/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, company_list[0])
