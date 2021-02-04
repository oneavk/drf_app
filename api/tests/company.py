from rest_framework import status
from rest_framework.test import APITestCase
from .helpers.data_structures import company_list
from .helpers.functions import create_company


class CompanyTestCase(APITestCase):
    def setUp(self) -> None:
        create_company(company_list[0]['name'])

    def test_list(self) -> None:
        response = self.client.get('/api/companies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, company_list)

    def test_retrieve(self) -> None:
        response = self.client.get('/api/companies/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, company_list[0])

    def test_list_without_auth(self) -> None:
        response = self.client.get('/api/companies/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_without_auth(self) -> None:
        response = self.client.get('/api/companies/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
