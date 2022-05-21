from rest_framework.exceptions import APIException


class RequestValidationError (APIException):
    def __init__(self, message):
        self.detail = message
        print('hey')
        self.status_code = 400

