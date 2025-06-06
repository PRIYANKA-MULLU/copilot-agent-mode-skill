from rest_framework.test import APITestCase
from django.urls import reverse
from .models import User

class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {'name': 'Test User', 'email': 'test@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
