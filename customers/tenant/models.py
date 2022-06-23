from django.db import models

# Create your models here.
class users(models.Model):
  id =  models.AutoField(primary_key=True)
  username =  models.CharField(max_length=200,)
  phone =  models.CharField(max_length=200),
  email =  models.EmailField(max_length=60, unique=True)

  def __str__(self):
    return self.email

class keja_tenant_dashboard(models.Model):
  id = models.AutoField(primary_key = True);
  user = models.ForeignKey(users, on_delete=models.CASCADE)
  my_active_rooms = models.IntegerField(default=0);
  expected_rent = models.IntegerField(default=0);
  pending_charges = models.IntegerField(default=0);
  my_pending_rooms = models.IntegerField(default=0);

class keja_invoices(models.Model):
  id = models.AutoField(primary_key=True);
  user = models.ForeignKey(users, on_delete=models.CASCADE)
  invoice_id = models.CharField(max_length=200)
  invoice_name = models.CharField(max_length=200)
  invoice_status = models.CharField(max_length=200)
  invoice_number = models.CharField(max_length=200)
  invoice_date = models.CharField(max_length=200)