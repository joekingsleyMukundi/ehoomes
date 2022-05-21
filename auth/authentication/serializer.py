from rest_framework import serializers
from .models import *


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email',
                  'first_name', 'last_name', 'phone']