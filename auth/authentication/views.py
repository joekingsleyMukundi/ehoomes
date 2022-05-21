from errors.internalerror import Custom500error
from errors.notfound_errors import Custom404Error
from errors.request_validation_error import RequestValidationError
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerialiser
from .models import CustomUser

# Create your views here.

@api_view(['GET'])
def documentation(request):
  routes = [
        {'GET': '/api/v1/users/register', },
        {'POST': '/api/v1/users/register', },
        {'GET': '/api/v1/users/login', },
        {'POST': '/api/v1/users/login', },
        {'GET': '/api/v1/users/dashboard', }
    ]
  return Response(routes)

@api_view(['GET'])
def getUsers(request):
  users = CustomUser.objects.all()
  serializer = UserSerialiser(users, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def error_400(request, exception=None):
  print(request)
  raise RequestValidationError('BadREquest')

@api_view(['GET'])
def error_404(request, exception=None):
  raise Custom404Error('Not Found')

@api_view(['GET'])
def error_500(request, exception=None):
  print(request)
  raise Custom500error('Intrenal server Error')