from django.test import TestCase
from tenant.models import *


class TestModels(TestCase):
    def setUp(self):
        self.user = users_model.objects.create(username='test', user_phone='123456789', email='test@gmail.com')

    def test_user_model(self):
        self.assertEqual(self.user.username, 'test')
        self.assertEqual(self.user.user_phone, '123456789')
        self.assertEqual(self.user.email, 'test@gmail.com')

    def test_tenant_dashboard_model(self):
        self.tenant_dashboard = keja_tenant_dashboard.objects.create(my_active_rooms=1, user=self.user, expected_rent=2,
                                                                     pending_charges=3, my_pending_rooms=4)
        self.assertEqual(self.tenant_dashboard.my_active_rooms, 1)
        self.assertEqual(self.tenant_dashboard.expected_rent, 2)
        self.assertEqual(self.tenant_dashboard.pending_charges, 3)
        self.assertEqual(self.tenant_dashboard.my_pending_rooms, 4)
        self.assertEqual(self.tenant_dashboard.user.username, 'test')
        self.assertEqual(self.tenant_dashboard.user.user_phone, '123456789')
        self.assertEqual(self.tenant_dashboard.user.email, 'test@gmail.com')

    def test_keja_invoices(self):
        self.keja_invoices = keja_invoices.objects.create(invoice_id='1', invoice_name='test', user=self.user,
                                                          invoice_status='test', invoice_number='1',
                                                          invoice_date='test')
        self.assertEqual(self.keja_invoices.invoice_id, '1')
        self.assertEqual(self.keja_invoices.invoice_name, 'test')
        self.assertEqual(self.keja_invoices.invoice_status, 'test')
        self.assertEqual(self.keja_invoices.invoice_number, '1')
        self.assertEqual(self.keja_invoices.invoice_date, 'test')
        self.assertEqual(self.keja_invoices.user.username, 'test')
        self.assertEqual(self.keja_invoices.user.user_phone, '123456789')
        self.assertEqual(self.keja_invoices.user.email, 'test@gmail.com')
