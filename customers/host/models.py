from django.db import models
from tenant.models import users_model

# Create your models here.
class host_model(models.Model):
    id=models.AutoField(primary_key=True)
    host_id=models.CharField(max_length=200)
    host_name = models.CharField(max_length=100)
    host_email = models.EmailField(max_length=100)
    host_phone = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)

    def __str__(self):
        return self.host_name


class host_dashboard(models.Model):
    id=models.AutoField(primary_key=True)
    host = models.OneToOneField(host_model, on_delete=models.CASCADE)
    expences = models.FloatField(default=0)
    revenue = models.FloatField(default=0)
    statment_of_operations = models.FloatField(default=0)
    pending_charges = models.FloatField(default=0)
    automate_payments = models.BooleanField(default=False)
    automate_managements = models.BooleanField(default=False)
    house_maintanance = models.IntegerField(default=0)
    pending_payout = models.FloatField(default=0)
    active_listings = models.IntegerField(default=0)
    vacants = models.IntegerField(default=0)
    active_deposits = models.FloatField(default=0)
    on_hold_deposits = models.FloatField(default=0)
    pending_deposits = models.FloatField(default=0)
    booked_listings = models.IntegerField(default=0)
    active_clients = models.IntegerField(default=0)


class host_appartments(models.Model):
    id=models.AutoField(primary_key=True)
    host = models.ForeignKey(host_model, on_delete=models.CASCADE)
    apartment_name = models.CharField(max_length=100)
    apartment_id = models.CharField(max_length=100)
    apartment_no_of_units = models.IntegerField(default=0)
class room_models(models.Model):
    id=models.AutoField(primary_key=True)
    room_host = models.ForeignKey(host_model, on_delete=models.CASCADE)
    apartment = models.ForeignKey(host_appartments, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=100)
    room_id = models.CharField(max_length=100)
    room_status = models.CharField(max_length=100)
    room_image = models.CharField(max_length=100)
    room_price = models.FloatField(default=0)
    room_tenant = models.ForeignKey(users_model, on_delete=models.CASCADE, null=True, blank=True)

class host_recent_transactions(models.Model):
    id=models.AutoField(primary_key=True)
    host = models.ForeignKey(host_model, on_delete=models.CASCADE)
    tenant = models.ForeignKey(users_model, on_delete=models.CASCADE)
    room = models.ForeignKey(room_models, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    amount = models.FloatField(default=0)
    created_at = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=100)
    transaction_to = models.CharField(max_length=100)
    transaction_from = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100)

class billing_activities(models.Model):
    id=models.AutoField(primary_key=True)
    host = models.ForeignKey(host_model, on_delete=models.CASCADE)
    tenant = models.ForeignKey(users_model, on_delete=models.CASCADE)
    created_at = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

class tenat_flow_model(models.Model):
    id=models.AutoField(primary_key=True)
    host = models.ForeignKey(host_model, on_delete=models.CASCADE)
    tenant = models.ForeignKey(users_model, on_delete=models.CASCADE)
    room = models.ForeignKey(room_models, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)

    