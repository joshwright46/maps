from users.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from rest_framework import status
from rest_framework.test import APITestCase

class TestUserAuth(APITestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='testpass')

    def test_login_successful(self):
        url = reverse('token_obtain_pair')
        request = {
            "email": "test@example.com",
            "password": "testpass"
        }
        response = self.client.post(url, request, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)

    def test_login_unsuccessful(self):
        url = reverse('token_obtain_pair')
        request = {
            "email": "test@example.com",
            "password": "xxxxxxxxxxxx"
        }
        response = self.client.post(url, request, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class TestUserRegistration(APITestCase):
    def test_user_registration(self):
        url = reverse('register')
        request = {
            'email': 'testuser@example.com',
            'password': 'abc123def456!',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.post(url, request, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email='testuser@example.com').exists())

class PasswordResetRequestViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='old_password')
        self.url = reverse('password-reset')

    def test_password_reset_request(self):
        response = self.client.post(self.url, {'email': 'test@example.com'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PasswordResetConfirmViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='old_password')
        self.token_generator = PasswordResetTokenGenerator()
        self.token = self.token_generator.make_token(self.user)
        self.uid = urlsafe_base64_encode(force_bytes(self.user.pk))  # Ensure this matches how your UID is generated/decoded in your views
        self.url = reverse('password-reset-verify', args=[self.uid, self.token])

    def test_password_reset_confirm(self):
        new_password = 'new_password123'
        response = self.client.post(self.url, {'password': new_password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the password was actually changed
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password(new_password))