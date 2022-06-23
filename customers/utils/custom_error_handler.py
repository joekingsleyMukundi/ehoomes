from rest_framework.views import exception_handler

def custom_error_handler(exec, context):
  response = exception_handler(exec, context)
  if response is not None:
    response.data['status_code'] = response.status_code
    error_message = [
      {
        'message': response.data['detail']
      }
    ]
    response.data['errors'] = error_message
    del response.data['status_code']
    del response.data['detail']
    return response
    