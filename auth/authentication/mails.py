from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse

def otp_email(uid, token, username, receiver):
  subject = 'Verification'
  message = 'Dear ' + username + ' Welcome to Ehoomes. Let us verify your email. use this link:  https://www.ehoomes.com/activate/' +uid+'/'+token+'/'
  from_email = 'ehoomes@novaluxicawriters.com'
  try:
      send_mail(subject, message, from_email, [receiver])
      print('send')
  except BadHeaderError:
      raise BadHeaderError('invalid header found')


def send_custom_email(subject, message, receiver):
  from_email = 'ehoomes@novaluxicawriters.com'
  try:
      send_mail(subject, message, from_email, [receiver])
      print('send')
  except BadHeaderError:
      raise BadHeaderError('invalid header found')