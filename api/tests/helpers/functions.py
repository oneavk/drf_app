"""
Module for test helper functions
"""
from api.models import Company, Employee
from django.contrib.auth.models import User, Permission
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.exceptions import AuthenticationFailed


def create_company(name: str) -> Company:
    company = Company()
    company.name = name
    company.save()
    return company


def create_employee(last_name: str, first_name: str, middle_name: str, company: Company) -> Employee:
    employee = Employee()
    employee.last_name = last_name
    employee.first_name = first_name
    employee.middle_name = middle_name
    employee.company = company
    employee.save()
    return employee


def create_user(username: str = 'user', password: str = 'password') -> User:
    user = User()
    user.username = username
    user.set_password(password)
    user.save()
    return user


def get_auth(client: APIClient, permissions: list = None) -> None:
    username = 'username'
    password = 'password'
    auth_data = {'username': username, 'password': password}

    user = create_user(username, password)
    if permissions is not None:
        for codename in permissions:
            permission = Permission.objects.filter(codename=codename).first()
            user.user_permissions.add(permission)

    response = client.post('/api/auth/', auth_data)

    if response.status_code != status.HTTP_200_OK:
        raise AuthenticationFailed

    client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.json()['access'])
