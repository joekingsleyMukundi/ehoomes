from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def tenant_dashboard(request):
  userEmail = request.user.email
  tenant = keja_tenant_dashboard.objects.get({'email':userEmail})
  serializer = TenantDashboardSerializer(tenant, many=False)
  return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def user_profile(request):
  if  request.method == 'POST':
    serializer = UpdateUserProfileSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({"success": True, 'user': serializer.data},status=HTTP_200_OK)
  return Response({request.user})