from rest_framework import status
from rest_framework.test import APITestCase
from .helpers.functions import create_user


class AuthTestCase(APITestCase):
    def test_auth_api(self) -> None:
        username = 'username'
        password = 'password'
        auth_data = {'username': username, 'password': password}

        create_user(username, password)

        response = self.client.post('/api/auth/', auth_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, 'auth fail')

        response = self.client.post('/api/auth/refresh/', {'refresh': response.json()['refresh']})
        self.assertEqual(response.status_code, status.HTTP_200_OK, 'refresh token fail')
