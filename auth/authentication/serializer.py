from rest_framework import serializers
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import  smart_str, force_str,  smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .models import *
from .mails import *
from errors.request_validation_error import RequestValidationError


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email',
                  'username', 'phone', 'is_host', 'is_verified', 'is_active', 'activationtoken']

class ChangePasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length = 2)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        try:
            email = attrs.get('email')
            if CustomUser.objects.filter(email=email).exists():
                user = CustomUser.objects.get(email=email)
                uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
                token = PasswordResetTokenGenerator().make_token(user)
                url = 'http://127.0.0.1:8000/auth/password_reset/?uid='+uidb64+'/?token='+token+'/'
                subject = 'Password reset'
                message = 'You or someone else has initiated a password reset. if it was you click the link  to reset the password: '+url
                send_custom_email(subject,message,user.email)
                return attrs
            raise RequestValidationError('user doesnot exist')
        except Exception as e:
            print(e)
            raise RequestValidationError(e)

class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length = 5,write_only=True)
    confirm_password = serializers.CharField(min_length = 5,write_only=True)
    token = serializers.CharField(min_length=1,write_only=True)
    uidb64 = serializers.CharField(min_length=1,write_only=True)
    class Meta:
        fields=['password','confirm_password','token','uidb64']
    def validate(self, attrs):
        try:
            password = attrs.get('password')
            confirm_password = attrs.get('confirm_password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')
            if password != confirm_password:
              raise RequestValidationError('password dont match')
            id = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise RequestValidationError('reset link is invalid')
            user.set_password(password)
            user.save()
            subject = 'Password reset success'
            message = 'Your password has succcesfully been reset'
            send_custom_email(subject,message,user.email)
            return user;
        except Exception as e:
            print(e)
            raise RequestValidationError(e)

class ChangeEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=100)

    class Meta:
        fields = ['email']

    def validate(self, attrs, id):
        email = attrs.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise RequestValidationError("email already exists")
        user = CustomUser.objects.get(id=id);
        try:
            user.email = email
        except Exception as e:
            raise RequestValidationError(e)
