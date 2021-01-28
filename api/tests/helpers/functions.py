"""
Module for test helper functions
"""
from api.models import Company


def create_company(name: str) -> Company:
    company = Company()
    company.name = name
    company.save()
    return company
