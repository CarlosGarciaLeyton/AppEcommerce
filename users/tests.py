#Django


from django.test import TestCase
from django.test import Client

#Python
from http import HTTPStatus

#Models
from django.contrib.auth.models import User


class UserTestCase(TestCase):

    #La configuracion se ejecuta antes de cada metodo de prueba
    def setUp(self):
        self.c = Client()

    #Limipa la ejecucion despues de cada metodo de  prueba
    def tearDown(self):
        self.c = Client()

    def test_is_ok_page_login(self):
        response = self.c.get('/login')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_is_ok_page_register(self):
        response = self.c.get('/register')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_login_user(self):
        credentials = {
            'username': 'juancarlosgarcia',
            'password': '1234'
        }
        user = User.objects.create_user(**credentials)
        response = self.c.post('/login', credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_register_user(self, NULL=None):
        data = {
            'username': 'TestJC',
            'email': 'juan.garcia@gmail.com',
            'password': '123456A',
            'password_confirmation': '123456A',
        }
        response = self.c.post('/registro', data)
        try:
            user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            user = NULL
        self.assertIsInstance(user, User)
