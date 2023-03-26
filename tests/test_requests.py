import requests
from django.test import TestCase

DOMAIN = 'http://localhost:8000'


class PagesTests(TestCase):
    """Класс с тестами страниц"""
    def test_status_code_index_page(self):
        response = requests.get(DOMAIN)
        self.assertEqual(response.status_code, 200)

    def test_status_code_users_page(self):
        ...

    def test_status_code_login_page(self):
        response = requests.get(DOMAIN + '/login/')
        self.assertEqual(response.status_code, 200)

    def test_status_code_register_page(self):
        response = requests.get(DOMAIN + '/users/create/')
        self.assertEqual(response.status_code, 200)
