from django.test import TestCase
from tenant.models import *
from host.models import *


class TestModels(TestCase):
    def setUp(self):
        self.user = users_model.objects.create(username='test', user_phone='123456789', email='test@gmail.com', created_at='test')
        self.host = host_model.objects.create(host_id='1', host_name='test', host_email='test@gmail.com', host_phone='123456789', created_at='test')
        self.appartments = host_appartments.objects.create(host=self.host, apartment_name='test', apartment_id='1',apartment_no_of_units=2)
        self.rooms = room_models.objects.create(room_id='1', room_price=10000, room_status='test', room_image='test', apartment=self.appartments,room_host=self.host,room_tenant=self.user,)

    def test_user_model(self):
        self.assertEqual(self.user.username, 'test')
        self.assertEqual(self.user.user_phone, '123456789')
        self.assertEqual(self.user.email, 'test@gmail.com')
        self.assertEqual(self.user.created_at, 'test')

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

    def tests_host_model(self):
        self.assertEqual(self.host.host_name, 'test')
        self.assertEqual(self.host.host_id, '1')
        self.assertEqual(self.host.host_phone, '123456789')
        self.assertEqual(self.host.host_email, 'test@gmail.com')
        

    def test_host_dashboard_model(self):
        self.host_dashboard = host_dashboard.objects.create(host=self.host, expences=10000, revenue=20000, statment_of_operations=-30000, pending_charges = 40000, automate_payments=False, automate_managements=False, house_maintanance=1, pending_payout=20000, active_listings=2, vacants=3, active_deposits= 200000,on_hold_deposits=40000, pending_deposits=50000, booked_listings=3, active_clients=4)

        self.assertEqual(self.host_dashboard.host.host_name, 'test')
        self.assertEqual(self.host_dashboard.host.host_id, '1')
        self.assertEqual(self.host_dashboard.host.host_phone, '123456789')
        self.assertEqual(self.host_dashboard.host.host_email, 'test@gmail.com')
        self.assertEqual(self.host_dashboard.host.created_at, 'test')
        self.assertEqual(self.host_dashboard.expences, 10000)
        self.assertEqual(self.host_dashboard.revenue, 20000)
        self.assertEqual(self.host_dashboard.statment_of_operations, -30000)
        self.assertEqual(self.host_dashboard.pending_charges, 40000)
        self.assertEqual(self.host_dashboard.automate_payments, False)
        self.assertEqual(self.host_dashboard.automate_managements, False)
        self.assertEqual(self.host_dashboard.house_maintanance, 1)
        self.assertEqual(self.host_dashboard.pending_payout, 20000)
        self.assertEqual(self.host_dashboard.active_listings, 2)
        self.assertEqual(self.host_dashboard.vacants, 3)
        self.assertEqual(self.host_dashboard.active_deposits, 200000)
        self.assertEqual(self.host_dashboard.on_hold_deposits, 40000)
        self.assertEqual(self.host_dashboard.pending_deposits, 50000)
        self.assertEqual(self.host_dashboard.booked_listings, 3)
        self.assertEqual(self.host_dashboard.active_clients, 4)

    def test_host_tenant_flow_model(self):
        self.host_tenant_flow = tenat_flow_model.objects.create(host=self.host, tenant=self.user, room=self.rooms, status='test', created_at='test',)

        self.assertEqual(self.host_tenant_flow.host.host_name, 'test')
        self.assertEqual(self.host_tenant_flow.host.host_id, '1')
        self.assertEqual(self.host_tenant_flow.host.host_phone, '123456789')
        self.assertEqual(self.host_tenant_flow.host.host_email, 'test@gmail.com')
        self.assertEqual(self.host_tenant_flow.host.created_at, 'test')
        self.assertEqual(self.host_tenant_flow.tenant.username, 'test')
        self.assertEqual(self.host_tenant_flow.tenant.user_phone, '123456789')
        self.assertEqual(self.host_tenant_flow.tenant.email, 'test@gmail.com')
        self.assertEqual(self.host_tenant_flow.room.room_id, '1')
        self.assertEqual(self.host_tenant_flow.room.room_status, 'test')
        self.assertEqual(self.host_tenant_flow.room.room_image, 'test')
        self.assertEqual(self.host_tenant_flow.room.room_price, 10000)

    def test_host_recent_transactions_model(self):
        self.host_recent_transactions = host_recent_transactions.objects.create(host=self.host, tenant=self.user, room=self.rooms, status='test', created_at='test', amount=10000, transaction_type='test', transaction_to='test',  transaction_from='test', transaction_id='1')

        self.assertEqual(self.host_recent_transactions.host.host_name, 'test')
        self.assertEqual(self.host_recent_transactions.host.host_id, '1')
        self.assertEqual(self.host_recent_transactions.host.host_phone, '123456789')
        self.assertEqual(self.host_recent_transactions.host.host_email, 'test@gmail.com')
        self.assertEqual(self.host_recent_transactions.host.created_at, 'test')
        self.assertEqual(self.host_recent_transactions.tenant.username, 'test')
        self.assertEqual(self.host_recent_transactions.tenant.user_phone, '123456789')
        self.assertEqual(self.host_recent_transactions.tenant.email, 'test@gmail.com')
        self.assertEqual(self.host_recent_transactions.room.room_id, '1')
        self.assertEqual(self.host_recent_transactions.room.room_status, 'test')
        self.assertEqual(self.host_recent_transactions.room.room_image, 'test')
        self.assertEqual(self.host_recent_transactions.room.room_price, 10000)
        self.assertEqual(self.host_recent_transactions.status, 'test')
        self.assertEqual(self.host_recent_transactions.created_at, 'test')
        self.assertEqual(self.host_recent_transactions.amount, 10000)
        self.assertEqual(self.host_recent_transactions.transaction_type, 'test')
        self.assertEqual(self.host_recent_transactions.transaction_to, 'test')
        self.assertEqual(self.host_recent_transactions.transaction_from, 'test')
        self.assertEqual(self.host_recent_transactions.transaction_id, '1')

    def test_billing_activities_model(self):
        self.billing_activities = billing_activities.objects.create(host=self.host, tenant=self.user, message='test', created_at='test',)

        self.assertEqual(self.billing_activities.host.host_name, 'test')
        self.assertEqual(self.billing_activities.host.host_id, '1')
        self.assertEqual(self.billing_activities.host.host_phone, '123456789')
        self.assertEqual(self.billing_activities.host.host_email, 'test@gmail.com')
        self.assertEqual(self.billing_activities.tenant.username, 'test')
        self.assertEqual(self.billing_activities.tenant.user_phone, '123456789')
        self.assertEqual(self.billing_activities.tenant.email, 'test@gmail.com')
        self.assertEqual(self.billing_activities.message, 'test')
        self.assertEqual(self.billing_activities.created_at, 'test')

        