"""
Module for test helper functions
"""
from api.models import Company, Employee


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
