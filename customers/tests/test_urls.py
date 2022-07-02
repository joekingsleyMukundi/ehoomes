from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tenant.views import *
from host.views import *


class TestUrls(SimpleTestCase):

    def test_tenant_dashboard_url_is_resolved(self):
        url = reverse('tenant_dashboard')
        self.assertEqual(resolve(url).func, tenant_dashboard)

    def test_user_profile_url_is_resolved(self):
        url = reverse('user_profile')
        self.assertEqual(resolve(url).func, user_profile)

    def test_host_dashboard_url_is_resolved(self):
        url = reverse('host_dashboard')
        print(resolve(url).func)
        self.assertEqual(resolve(url).func, host_dashboard)
    
    def test_become_host_url_is_resolved(self):
        url = reverse('become_host')
        self.assertEqual(resolve(url).func, become_host)
