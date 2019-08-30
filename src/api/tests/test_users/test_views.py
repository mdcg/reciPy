from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import hashlib

from api.seeds.users_seeds import UserFactory


class AuthenticationViewsAPITestCase(APITestCase):
    def setUp(self):
        self.super_secret_password = hashlib.sha256().hexdigest()
        self.user = UserFactory(password=self.super_secret_password)

    def test_signin_views_success(self):
        url = reverse('signin')
        data = {
            'username': self.user.username,
            'password': self.super_secret_password,
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
