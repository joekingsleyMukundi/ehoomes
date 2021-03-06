from errors.internalerror import Custom500error
from errors.notfound_errors import Custom404Error
from errors.request_validation_error import RequestValidationError
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.encoding import  smart_str, force_str,  smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import *
from .models import CustomUser
from .producer import publish
from decorators.customdecorators import *

# Create your views here.

# creting a custom jwt generator class to add more items to the token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims in our case adding the username
        token['username'] = user.username
        token['is_active']= user.is_active
        token['email'] = user.email
        token['is_host'] = user.is_host
        # ...

        return token
# creating a class based view for the jwt url inheriting the token generator class above
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# creating a documentation view with all the urls available
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def documentation(request):
  routes = [
        {'GET': '/api/v1/users/register', },
        {'POST': '/api/v1/users/register', },
        {'GET': '/api/v1/users/login', },
        {'POST': '/api/v1/users/login', },
        {'GET': '/api/v1/users/dashboard', }
    ]
  return Response(routes)

# activating the user view
@api_view(['GET'])
@user_active
def activate(request, uid, token):
  # retreving the id from the encoded string in the url
  try:
    id = smart_str(urlsafe_base64_decode(uid))
    print(id)
  except Exception as e:
    print(e)
    raise Exception(e)
  # check wheather the user exists
  if not CustomUser.objects.filter(id = id).exists():
    raise Exception('user does not exist')
  user = CustomUser.objects.get(id = id)
  user_token= user.activationtoken
  if token != user_token:
    raise Exception('invalid token')
  user.is_active = True
  try:
    user.save()
    # publishing a message to all consumers regarding the created user
    publish('user_created', user)
  except Exception as e:
    print(e)
    raise Custom500error(e)
  print('success')
  serializer = UserSerialiser(user, many=False)
  return Response(serializer.data)


@api_view(['GET','POST'])
def reset_password_request(request):
  if request.method == 'POST':
    serializer = ChangePasswordRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception = True);
    return Response ('success')
  return Response('reset password')


@api_view(['GET'])
def reset_password(request, uidb64, token):
  try:
      id = smart_str(urlsafe_base64_decode(uidb64))
      user = CustomUser.objects.get(id=id)
      if not PasswordResetTokenGenerator().check_token(user,token):
          raise Exception('invalid reset token')
      return Response({'success':True,'message':'Credentials are valid','uidb64':uidb64,'token':token})
  except Exception as e:
      raise Exception(e.message)

@api_view(['PATCH'])
def set_new_password(request):
  serializer = ChangePasswordSerializer(data=request.data)
  serializer.is_valid(raise_exception = True)
  return Response({'success':True,'message':'Password reset  successfully'},status=status.HTTP_200_OK)


@api_view(['GET','POST'])
@permission_classes((IsAuthenticated, ))
def update_email():
  serializer = ChangeEmailSerializer(attrs=request.data, id=request.user.id)
  serializer.is_valid(raise_exception=True)
  return Response({'success':True,'message':'email reset succcess'})


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