from django.utils.encoding import  smart_str, force_str,  smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from authentication.models import *
def user_active(func):
    def wrapper(request,*args,**kwargs):
        uid=kwargs['uid']
        id = smart_str(urlsafe_base64_decode(uid))
        user=CustomUser.objects.get(id = id)
        if user.is_active:
            raise Exception('User already active')
        return func(request,*args,**kwargs)
    return wrapper