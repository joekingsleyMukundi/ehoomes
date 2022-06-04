import random
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.crypto import get_random_string
# Create your models here.
class CustomUser(AbstractUser):
  id =  models.AutoField(primary_key=True)
  email = models.EmailField(verbose_name='Email', max_length=60, unique=True)
  username = models.CharField(verbose_name='Fullname', max_length=255)
  phone = models.CharField(max_length=255,null=True,blank=True)
  activationtoken = models.CharField (max_length= 255,default=get_random_string(length=32))
  is_host = models.BooleanField(default=False)
  is_verified = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)
  REQUIRED_FIELDS = ['username','phone']
  USERNAME_FIELD = 'email'
  
  def get_username(self):
      return self.email

