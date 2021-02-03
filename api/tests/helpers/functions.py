"""
Module for test helper functions
"""
from api.models import Company, Employee
from django.contrib.auth.models import User


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
