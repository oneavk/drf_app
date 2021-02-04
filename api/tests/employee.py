from rest_framework import status
from rest_framework.test import APITestCase
from .helpers.functions import create_company, create_employee, get_auth
from .helpers.data_structures import company_list, employee_list
from api.models import Employee


class EmployeeTestCase(APITestCase):
    def setUp(self) -> None:
        self.company = create_company(company_list[0]['name'])
        for employee in employee_list:
            employee['company'] = self.company.id

        self.employee = create_employee(
            employee_list[0]['last_name'],
            employee_list[0]['first_name'],
            employee_list[0]['middle_name'],
            self.company
        )

    def test_list(self) -> None:
        get_auth(self.client, ['view_employee'])
        for i in range(1, len(employee_list)):
            create_employee(
                    employee_list[i]['last_name'],
                    employee_list[i]['first_name'],
                    employee_list[i]['middle_name'],
                    self.company
                )
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, employee_list)

    def test_retrieve(self) -> None:
        get_auth(self.client, ['view_employee'])
        response = self.client.get(f'/api/employees/{self.employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, employee_list[0])

    def test_create(self) -> None:
        get_auth(self.client, ['add_employee'])
        response = self.client.post('/api/employees/', employee_list[2])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        employee = Employee.objects.get(pk=response.data['id'])
        self.assertEqual(employee.name, employee_list[2]['name'])

    def test_update(self) -> None:
        get_auth(self.client, ['change_employee'])
        employee_data = employee_list[0].copy()
        employee_data['first_name'] = 'updated_name'

        response = self.client.put(f'/api/employees/{self.employee.id}/', employee_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        employee = Employee.objects.get(pk=self.employee.id)
        self.assertEqual(employee.last_name, employee_data['last_name'])
        self.assertEqual(employee.first_name, employee_data['first_name'])
        self.assertEqual(employee.middle_name, employee_data['middle_name'])

    def test_destroy(self) -> None:
        get_auth(self.client, ['delete_employee'])
        response = self.client.delete(f'/api/employees/{self.employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Employee.DoesNotExist):
            Employee.objects.get(pk=self.employee.id)

    def test_name_prop(self) -> None:
        employee = Employee()
        employee.last_name = 'last'
        employee.first_name = 'first'
        self.assertEqual(employee.name, 'last first')

    def test_list_without_auth(self) -> None:
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_without_auth(self) -> None:
        response = self.client.get('/api/employees/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_without_auth(self) -> None:
        response = self.client.post('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_without_auth(self) -> None:
        response = self.client.put('/api/employees/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_destroy_without_auth(self) -> None:
        response = self.client.delete('/api/employees/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_without_permission(self) -> None:
        get_auth(self.client)
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_without_permission(self) -> None:
        get_auth(self.client)
        response = self.client.get('/api/employees/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_without_permission(self) -> None:
        get_auth(self.client)
        response = self.client.post('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_without_permission(self) -> None:
        get_auth(self.client)
        response = self.client.put('/api/employees/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_destroy_without_permission(self) -> None:
        get_auth(self.client)
        response = self.client.delete('/api/employees/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
