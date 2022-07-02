from rest_framework.exceptions import APIException


class SmsValidationError(APIException):
    def __init__(self, message):
        self.detail = message
        self.status_code = 400
