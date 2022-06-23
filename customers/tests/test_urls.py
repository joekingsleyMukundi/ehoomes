from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from tenant.views import *


class TestUrls(SimpleTestCase):

    def test_tenant_dashboard_url_is_resolved(self):
        url = reverse('tenant_dashboard')
        self.assertEquals(resolve(url).func, tenant_dashboard)

    def test_user_profile_url_is_resolved(self):
        url = reverse('user_profile')
        self.assertEquals(resolve(url).func, user_profile)
