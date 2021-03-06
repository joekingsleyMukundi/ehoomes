from django.db import models

# Create your models here.
class users_model(models.Model):
  id =  models.AutoField(primary_key=True)
  user_id = models.CharField(max_length=100)
  username =  models.CharField(max_length=200,)
  user_phone = models.CharField(max_length=200,)
  email =  models.EmailField(max_length=200, unique=True)
  created_at = models.CharField(max_length=100)
  otp_become_host = models.IntegerField(default=0)


class keja_tenant_dashboard(models.Model):
  id = models.AutoField(primary_key = True);
  user = models.OneToOneField(users_model, on_delete=models.CASCADE)
  my_active_rooms = models.IntegerField(default=0);
  expected_rent = models.IntegerField(default=0);
  pending_charges = models.IntegerField(default=0);
  my_pending_rooms = models.IntegerField(default=0);
  automate_payments = models.BooleanField(default=False)
  active_deposits = models.FloatField(default=0)
  on_hold_deposits = models.FloatField(default=0)
  pending_deposits = models.FloatField(default=0)
  pending_payout = models.FloatField(default=0)

class keja_invoices(models.Model):
  id = models.AutoField(primary_key=True);
  user = models.ForeignKey(users_model, on_delete=models.CASCADE)
  invoice_id = models.CharField(max_length=200)
  invoice_name = models.CharField(max_length=200)
  invoice_status = models.CharField(max_length=200)
  invoice_number = models.CharField(max_length=200)
  invoice_date = models.CharField(max_length=200)

