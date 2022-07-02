import africastalking
import os
from dotenv import load_dotenv
from errors.smsvalidationerror import SmsValidationError

load_dotenv()


class SMS:
    def __init__(self):
        self.username = os.getenv('AFRICASTALKINGUSERNAME')
        self.api_key = os.getenv('AFRICASTALKINGAPIKEY')

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self, phone, otp):
        # Set the numbers you want to send to in international format
        recipients = [phone]

        # Set your message
        message = "Welcome to ur hosting program. Here is your  activation code "

        # Set your shortCode or senderId
        sender = "50804"
        try:
            # That's it, hit send, and we'll take care of the rest.
            response = self.sms.send(message, recipients, sender)
            print(response)
        except Exception as e:
            print('Encountered an error while sending: %s' % str(e))
            raise SmsValidationError(e)
