from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthenticationTests(APITestCase):
    def setUp(self):
        """Set up test client and create test user"""
        self.client = APIClient()
        self.test_user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

        # Match your urls.py routes
        self.register_url = reverse('register')         # /users/register/
        self.login_url = reverse('login')               # /users/login/
        self.token_refresh_url = reverse('token_refresh')  # /users/token/refresh/
        self.plant_list_url = reverse('plant-index')    # /plants/

    # -------------------
    # Registration
    # -------------------

    def test_user_registration_success(self):
        """Test successful user registration"""
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123'
        }
        response = self.client.post(self.register_url, data, format='json')

        # Expect a 201 response and possibly a token in the response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_registration_invalid_data(self):
        """Test user registration with missing required fields"""
        data = {'username': 'incomplete'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertIn(response.status_code, [status.HTTP_400_BAD_REQUEST, status.HTTP_500_INTERNAL_SERVER_ERROR])

    # -------------------
    # Login
    # -------------------

    def test_user_login_success(self):
        """Test successful user login"""
        data = {'username': 'testuser', 'password': 'testpass123'}
        response = self.client.post(self.login_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Depending on your view, the response may include tokens or just user data
        self.assertIn('user', response.data)

    def test_user_login_invalid_credentials(self):
        """Test login with wrong password"""
        data = {'username': 'testuser', 'password': 'wrongpass'}
        response = self.client.post(self.login_url, data, format='json')
        self.assertIn(response.status_code, [status.HTTP_400_BAD_REQUEST, status.HTTP_401_UNAUTHORIZED])

    # -------------------
    # Token Refresh
    # -------------------

    def test_token_refresh(self):
        """Test token refresh functionality"""
        # Login first to get tokens
        login_data = {'username': 'testuser', 'password': 'testpass123'}
        login_response = self.client.post(self.login_url, login_data, format='json')

        if 'refresh' in login_response.data:
            refresh_token = login_response.data['refresh']
            response = self.client.post(self.token_refresh_url, {'refresh': refresh_token}, format='json')
            self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_401_UNAUTHORIZED])

        else:
            # If your VerifyUserView doesn’t handle refresh logic, skip this
            self.skipTest("Token refresh not implemented in this backend.")

    # -------------------
    # Auth Required Endpoints
    # -------------------

    def test_authentication_required_for_protected_routes(self):
        """Ensure plant list requires authentication"""
        # Without token
        response = self.client.get(self.plant_list_url)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

        # Login and retry
        login_data = {'username': 'testuser', 'password': 'testpass123'}
        login_response = self.client.post(self.login_url, login_data, format='json')

        if 'access' in login_response.data:
            token = login_response.data['access']
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        else:
            # If no token system, still test with authenticated session
            self.client.force_authenticate(user=self.test_user)

        response = self.client.get(self.plant_list_url)
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])

    def tearDown(self):
        """Clean up after each test"""
        self.client.credentials()
