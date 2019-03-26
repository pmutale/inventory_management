from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from access_control.models import Employee
from access_control.views import UserCreate


class TestAccessControl(APITestCase):
    def setUp(self):
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        user = get_user_model()
        return user.objects.create_user(
            "test", email="testuser@test.com", password="test"
        )

    def test_list(self):
        request = self.client.get(
            self.client.get("path", None),
            HTTP_AUTHORIZATION="Token {}".format(self.token.key),
        )
        request.user = self.user
        response = self.client.request()
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )

    def test_create_employee(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse("access_control:user_create")
        data = {
            "username": "inventoryUser",
            "password": "test123456789",
            "email": "example@developers.nl",
            "first_name": "Example",
            "last_name": "Test",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().user.username, "inventoryUser")
