import random

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.sms import SMS
from tenant.models import *
from errors.db_error import *
from decorators.custom_auth_decorators import authenticate_user
from .models import *


# Create your views here.
@api_view(['GET', 'POST'])
@authenticate_user
def become_host(request):
    if request.method == 'POST':
        phone = request.data['phone']
        otp = random.randint(1000, 9999)
        users_model.otp_become_host = otp
        try:
            users_model.save()
        except Exception as e:
            raise DbConnectionError(e)
        SMS().send(phone)
        return Response({"success": True, "message": "we have sent you a verification code to you phone number"},
                        status=status.HTTP_200_OK)

    return Response("success", status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@authenticate_user
def activate_host(request):
    if request.method == 'POST':
        code = request.data['verification_code']
        user = users_model.objects.get(id=request.user.id)
        db_code = user.otp
        if not code == db_code:
            raise ValidationError('verification code is invalid')
        try:
            created_host = host_model.objects.create(host_id=user.user_id, host_name=username, host_email=email,
                                                     host_phone=user_phone)
            return Response({"success": True, "message": "host created  successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            raise DbConnectionError(e)


@api_view(['GET', 'POST'])
@authenticate_user
def host_dashboard(request):
    return Response("success", status=status.HTTP_200_OK)
