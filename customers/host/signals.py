from django.db.models.signals import post_save
from ..utils.sms import SMS

def host_request(sender, instance, created, **kwargs):
