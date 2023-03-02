import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate,
APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import UserViewSet
from .models import User
class TestAuthorViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'first_name': 'Ivan',
'birthday_year': 1999}, format='json')
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'first_name': 'Ivan', 'birthday_year': 1999}
                               , format='json')
        admin = User.objects.create_superuser('admin', 'admin@admin.com',
                                          'admin123456')
        force_authenticate(request, admin)
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        user = User.objects.create(first_name='Ivan', birthday_year=1999)
        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)