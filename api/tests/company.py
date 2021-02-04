from rest_framework import status
from rest_framework.test import APITestCase
from .helpers.data_structures import company_list
from .helpers.functions import create_company, get_auth
from api.models import Company


class CompanyTestCase(APITestCase):
    def setUp(self) -> None:
        create_company(company_list[0]['name'])

    def test_list(self) -> None:
        get_auth(self.client)
        create_company(company_list[1]['name'])
        response = self.client.get('/api/companies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, company_list)

    def test_retrieve(self) -> None:
        get_auth(self.client)
        response = self.client.get('/api/companies/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, company_list[0])

    def test_create(self) -> None:
        get_auth(self.client)
        response = self.client.post('/api/companies/', company_list[1])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, company_list[1])

        employee = Company.objects.get(pk=response.data['id'])
        self.assertEqual(employee.name, company_list[1]['name'])

    def test_update(self) -> None:
        get_auth(self.client)

        company_data = company_list[0].copy()
        company_data['name'] = 'updated_name'

        response = self.client.put(f'/api/companies/{company_data["id"]}/', company_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        company = Company.objects.get(pk=company_data["id"])
        self.assertEqual(company.name, company_data['name'])

    def test_destroy(self) -> None:
        get_auth(self.client)
        response = self.client.delete(f'/api/companies/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Company.DoesNotExist):
            Company.objects.get(pk=1)

    def test_list_without_auth(self) -> None:
        response = self.client.get('/api/companies/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_without_auth(self) -> None:
        response = self.client.get('/api/companies/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_without_auth(self) -> None:
        response = self.client.post('/api/companies/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_without_auth(self) -> None:
        response = self.client.put('/api/companies/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_destroy_without_auth(self) -> None:
        response = self.client.delete('/api/companies/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
