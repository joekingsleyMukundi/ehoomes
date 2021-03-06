from django.test import TestCase, Client
from django.urls import reverse
from tenant.models import *
import requests, json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = 'http://auth:8080/auth/token/'
        self.data = {'email': 'joekingsleymukundi@gmail.com', 'password': 'w57J23B4b4BcSZR'}
        self.tokens = requests.post(url=self.url, data=self.data)
        # print(self.tokens.json())
        # print(self.tokens.json()['access'])
        self.user = users_model.objects.create(username='joekingsleymukudi', user_phone='123456789', email='joekingsleymukundi@gmail.com',)
        self.tenant_dashboard = keja_tenant_dashboard.objects.create(my_active_rooms=1, user=self.user, expected_rent=2,
                                                                     pending_charges=3, my_pending_rooms=4)
        self.keja_invoices = keja_invoices.objects.create(invoice_id='1', invoice_name='test', user=self.user,
                                                          invoice_status='test', invoice_number='1',
                                                          invoice_date='test')

    def test_tenant_dashboard_view_GET(self):
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Bearer ' + self.tokens.json()['access']
        response = self.client.get(reverse('tenant_dashboard',))
        print((response.data))
        self.assertEqual(response.status_code, 200)

    def test_tenant_dashboard_view_not_authorized_GET(self):
        response = self.client.get(reverse('tenant_dashboard'))
        self.assertEqual(response.status_code, 401)

    def test_user_profile_view_GET(self):
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Bearer ' + self.tokens.json()['access']
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 200)

    def test_user_profile_view_not_authorized_GET(self):
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 401)

    def test_user_profile_view_POST(self):
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Bearer ' + self.tokens.json()['access']
        response = self.client.post(reverse('user_profile'),{'email': 'joekingsleymukundi@gmail.com','username': 'test', 'user_phone': '123456789',},)
        print(response.data)
        self.assertEqual(response.data['user']['username'], 'test')
        self.assertEqual(response.data['user']['user_phone'], '123456789')
        self.assertEqual(response.data['user']['email'], 'joekingsleymukundi@gmail.com')
        self.assertEqual(response.status_code, 200)

    def test_user_profile_view_not_authorized_POST(self):
        response = self.client.post(reverse('user_profile'),
                                    {'username': 'test', 'user_phone': '123456789', 'email': 'test@gmail.com'})
        self.assertEqual(response.status_code, 401)

    def test_tenant_profile_view_did_not_POST_with_no_data_passed(self):
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Bearer ' + self.tokens.json()['access']
        respocese = self.client.post(reverse('user_profile'),)
        self.assertEqual(respocese.status_code, 400)
