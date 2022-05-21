from distutils.log import error
from rest_framework.views import exception_handler
def custom_error_handler(exc, context):
  response = exception_handler(exc, context)
  if response is not None:
    response.data['status_code'] = response.status_code
    error_message = [
      {
        'message': response.data['detail']
      }
    ]
    response.data['errors'] = error_message
    del response.data['detail']
    del response.data['status_code']
    return response