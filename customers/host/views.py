from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST'])
def become_host(request):
  if request.method == 'POST':
    phone = request.data['phone']
    # TODO: create sent text functionality 
    
    return Responce("success", status=status.HTTP_200_OK)
  return Responce("success", status=status.HTTP_200_OK)
@api_view(['GET','POST'])
def host_dashboard(request):
  return Response("success",status=status.HTTP_200_OK)
