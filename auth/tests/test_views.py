from django.test import TestCase, Client
from django.urls import  reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from authentication.models import *
import json
# client is a way to test our view
class TestViews(TestCase):

  # this function will run b4 evry ttest tto a ssume a certain cenario
  def setUp(self):
    self.client = Client()
    self.get_users = reverse('get_users')
     # because the some uid and token donot exist we need to ceate the user and get the id and token
    self.user = CustomUser.objects.create(
      email="joekings@gmail.com",
      username = "joekingsley",
      phone="06456554",
      password="Mukundirandal254"
    )
    self.id = urlsafe_base64_encode(smart_bytes(self.user.id))

    self.activate_user = reverse('activate_users',args=[self.id, self.user.activationtoken])
   

  def test_get_users_GET(self):
    response = self.client.get(self.get_users)
    self.assertEquals(response.status_code, 200)
    # so if you wwant to test the template used in this case we do this
    # self.assertTemplateUsed(response, 'html template')

  def test_reset_password_GET(self):
    response = self.client.get(self.activate_user)
    self.assertEquals(response.status_code, 200)

# test to see if data will be added in post request 
  # def test_authentication_create_new_user_POST_create_new_user(self):
  #   response = self.client.post(reverse('registerusers'),{
  #     'usernaem':"username ",
  #     'email:':'rmail'
  #   })
  #   self.assertEquals(responce.status_code, 200)
    # self.assertEquals(customuser.objects.first().username, 'name we used')

# test to see that no data will be added if empty data is posted
# def test_user_not_created_when_no_data_POST(self):
#   # REALISE ITS A POST BUT WE HAVE NOT SENT ANY DATA
#   response = self.client.post(reverse('registerusers'),)
#   self.assertEquals(responce.status_code, 200)
#   self.assertEquals(CUSTOMUSER.objects.count(),0)

  # def delete_user_DELETE(self):
  #   # ALWAYS KNOW that the tests alawaus creates  a new database which is empty
  #   CustomUser.objects.create(
  #     email="joekings@gmail.com",
  #     username = "joekingsley",
  #     phone="06456554",
  #     password="Mukundirandal254"
  #   )
  #   # we use url names always remember
  #   response = self.client.delet(reverse('deletuser'),json.damps({'id':1
  #   }))
  #   self.assertEquals(responce.statuscode, 201)
  #   self.assertEquals(customuser.objects.count(),0)
  
  # def delete_user_when_no_data_provided_DELETE(self):
  #   # ALWAYS KNOW that the tests alawaus creates  a new database which is empty
  #   CustomUser.objects.create(
  #     email="joekings@gmail.com",
  #     username = "joekingsley",
  #     phone="06456554",
  #     password="Mukundirandal254"
  #   )
  #   # we use url names always remember
  #   response = self.client.delet(reverse('deletuser'))
  #   self.assertEquals(responce.statuscode, 404)
  #   self.assertEquals(customuser.objects.count(),1)