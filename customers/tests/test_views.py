from django.test import TestCase, Client
from django.urls import reverse
from tenant.models import *
class TestViews(TestCase):
  def setUp(self):
    self.client = Client()
    self.user = users.objects.create(username='test', phone='123456789', email='test2@gmail.com', password='test')
    self.tenant_dashboard = keja_tenant_dashboard.objects.create(my_active_rooms=1, user=self.user, expected_rent=2, pending_charges=3, my_pending_rooms=4)
    self.keja_invoices = keja_invoices.objects.create(invoice_id='1', invoice_name='test', user=self.user, invoice_status='test', invoice_number='1', invoice_date='test')

  def test_tenant_dashboard_view(self):
    response = self.client.get(reverse('tenant_dashboard'))
    self.assertEqual(response.status_code, 200)