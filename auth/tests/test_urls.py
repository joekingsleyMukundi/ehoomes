from django.test import SimpleTestCase
from django.urls import reverse, resolve
from authentication.views import getUsers, set_new_password, reset_password, reset_password_request, activate, documentation, MyTokenObtainPairView

class TestUrls(SimpleTestCase):

  def test_get_users_url_is_resolved(self):
    # geting the url using the name and asserting it will it the viwe it is supposed to
    url = reverse('get_users')
    # print(resolve(url))
    self.assertEquals(resolve(url).func, getUsers)

  def test_token_obtain_pair_url_is_resolved(self):
    # geting the url using the name and asserting it will it the viwe it is supposed to
    url = reverse('token_obtain_pair')
    # print(resolve(url))
    # in cases of classbased views  after func we add func.view_class
    self.assertEquals(resolve(url).func.view_class, MyTokenObtainPairView)