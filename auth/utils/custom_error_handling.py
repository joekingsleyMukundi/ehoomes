from rest_framework.views import exception_handler
def custom_error_handler(exc, context):
  response = exception_handler(exc, context)
  if response is not None:
    response.data['status_code'] = response.status_code
    if not 'detail' in response.data.keys():
      if 'email' in response.data.keys():
        error_message = [
          {
            'message': response.data['email']
          }
        ]
        del response.data['email']
      elif 'password' in response.data.keys():
        error_message = [
          {
            'message': response.data['password']
          }
        ]
        del response.data['password']
    else:
      error_message = [
        {
          'message': response.data['detail']
        }
      ]
      del response.data['detail']
    response.data['errors'] = error_message
    del response.data['status_code']
    return response