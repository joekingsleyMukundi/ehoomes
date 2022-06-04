from django.db.models.signals import post_save, post_delete
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import random
from .mails import *
from .models import *


def user_created(sender, instance, created, **kwargs):
    if created:
        user = instance
        token = user.activationtoken
        uid = urlsafe_base64_encode(smart_bytes(user.id))
        otp_email(uid, token, user.username, user.email)


post_save.connect(user_created, sender=CustomUser)
