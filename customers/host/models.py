from django.db import models

# Create your models here.
class host_model(models.Model):
    id=models.AutoField(primary_key=True)
    host_id=models.CharField(max_length=200)
    host_name = models.CharField(max_length=100)
    host_email = models.EmailField(max_length=100)
    host_phone = models.CharField(max_length=100)
    host_address = models.CharField(max_length=100)
    host_city = models.CharField(max_length=100)
    host_state = models.CharField(max_length=100)
    host_country = models.CharField(max_length=100)
    host_zip = models.CharField(max_length=100)
    host_confirm_password = models.CharField(max_length=100)
    host_image = models.ImageField(upload_to='host_images', blank=True)
    host_about = models.TextField(max_length=1000)
    host_verified = models.BooleanField(default=False)
    host_verification_code = models.CharField(max_length=100)
    host_created_at = models.DateTimeField(auto_now_add=True)

