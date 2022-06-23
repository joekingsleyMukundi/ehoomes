from rest_framework import serializers
from errors import *
from .models import *

class TenantDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = keja_tenant_dashboard
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class UpdateUserProfileSerializer(serializers.ModelSerializer):
  id = serializers.IntegerField(read_only=True)
  username = serializers.CharField(required=True)
  email = serializers.EmailField(required=True)
  phone = serializers.CharField(required=True)
  class Meta:
    fields = ['username', 'email', 'phone']
  
  def validate(self, data):
    id = data.get('id')
    username = data.get('username')
    email = data.get('email')
    phone = data.get('phone')
    # save changed data to the database
    try:
      user = users.objects.get(id=id)
      user.username = username
      user.phone=phone
      user.email = email
      user.save ()
      return user
    except Exception as e:
      print(e)
      raise db_connection_error.DbConnectionError(e)