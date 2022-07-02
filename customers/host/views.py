import random

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.sms import SMS
from ..tenant.models import *
from ..errors.db_error import DbConnectionError


# Create your views here.
@api_view(['GET', 'POST'])
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
def host_dashboard(request):
    return Response("success", status=status.HTTP_200_OK)
