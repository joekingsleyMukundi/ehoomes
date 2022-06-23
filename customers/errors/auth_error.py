from rest_framework.exceptions import APIException

class AuthenticationError (APIException):
  def __init__(self, message):
    self.detail = message
    self.status_code = 401