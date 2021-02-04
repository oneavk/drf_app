from rest_framework import status
from rest_framework.test import APITestCase
from .helpers.functions import create_company, create_employee
from .helpers.data_structures import company_list, employee_list
from api.models import Employee


class EmployeeTestCase(APITestCase):
    def setUp(self) -> None:
        company = create_company(company_list[0]['name'])
        for i in range(len(employee_list)):
            create_employee(
                employee_list[i]['last_name'],
                employee_list[i]['first_name'],
                employee_list[i]['middle_name'],
                company
            )
            employee_list[i]['company'] = company.id

    def test_list(self) -> None:
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, employee_list)

    def test_retrieve(self) -> None:
        response = self.client.get('/api/employees/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, employee_list[0])

    def test_name_prop(self) -> None:
        empl = Employee()
        empl.last_name = 'last'
        empl.first_name = 'first'
        self.assertEqual(empl.name, 'last first')

    def test_list_without_auth(self) -> None:
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_without_auth(self) -> None:
        response = self.client.get('/api/employees/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
