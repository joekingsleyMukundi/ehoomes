from errors.auth_error import AuthenticationError
from tenant.models import  users_model
import jwt
import os
from dotenv import load_dotenv
load_dotenv()
# authentication decorator
def authenticate_user(func):
  def wrapper(request, *args, **kwargs):
    #  getting the base token from the headders
    base_token = request.META.get('HTTP_AUTHORIZATION')
    # validation of the token
    if base_token is None:
      raise AuthenticationError('user not authenticated')
    split_base_token = base_token.split(' ')
    if len(split_base_token) != 2:
      raise AuthenticationError('Authorization header must contain two space-delimited values')
    if split_base_token[0] != 'Bearer':
      raise AuthenticationError('Authorization header must start with Bearer ')
      # getting the actual token
    token = split_base_token[1]
    # decoding the token
    try:
      secretKey = os.getenv('SIGNINGKEY')
      payload = jwt.decode(token, secretKey, algorithms=['HS256'])
    except Exception as e:
      print(e)
      raise AuthenticationError('invalid token')
    # checking if the user exists
    username = payload['username']
    if not users_model.objects.filter(username = username).exists():
      raise AuthenticationError('user does not exist')
    # checking if the user is active
    is_active = payload['is_active']
    if not is_active:
      raise AuthenticationError('no active user  is found under those credentials')
    # retuning the authenticated user in request
    user = payload
    request.user = user
    return func(request, *args, **kwargs)
  return wrapper
  
