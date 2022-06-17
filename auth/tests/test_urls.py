from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from authentication.views import getUsers, set_new_password, reset_password, reset_password_request, activate, documentation, MyTokenObtainPairView

class TestUrls(SimpleTestCase):

  def test_get_users_url_is_resolved(self):
    # geting the url using the name and asserting it will it the view it is supposed to
    url = reverse('get_users')
    # print(resolve(url))
    self.assertEquals(resolve(url).func, getUsers)
    # test if tyhe url actually works
    

  def test_token_obtain_pair_url_is_resolved(self):
    # geting the url using the name and asserting it will it the viwe it is supposed to
    url = reverse('token_obtain_pair')
    # print(resolve(url))
    # in cases of classbased views  after func we add func.view_class
    self.assertEquals(resolve(url).func.view_class, MyTokenObtainPairView)

  def test_activate_users_url_is_resolved(self):
    # geting the url using the name and asserting it will it the viwe it is supposed to
    # in cases of  having query params or parameters in our url we use args
    url = reverse('activate_users', args=['some-uid','some-token'])
    # print(resolve(url))
    self.assertEquals(resolve(url).func, activate)
