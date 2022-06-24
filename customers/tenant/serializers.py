from rest_framework import serializers
from .models import *
from  errors import db_error


class TenantDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = keja_tenant_dashboard
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = users_model
        fields = '__all__'

class UpdateUserProfileSerializer(serializers.Serializer):
  email = serializers.EmailField(required=True)
  username = serializers.CharField(required=True)
  user_phone = serializers.CharField(required=True)
  class Meta:
    fields = ['username', 'email', 'user_phone']
  
  def validate(self, data):
    username = data.get('username')
    email = data.get('email')
    user_phone = data.get('user_phone')
    if not username or not email or not user_phone:
      raise db_error.ValidationError("some or all the values are missing")
    # save changed data to the database
    try:
      user = users_model.objects.get(email=email)
      user.username = username
      user.user_phone=user_phone
      user.save ()
      return user
    except Exception as e:
      raise db_error.DbConnectionError(e)