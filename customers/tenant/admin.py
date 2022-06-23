from django.contrib import admin
from .models import users_model,keja_tenant_dashboard,keja_invoices

# Register your models here.
admin.site.register(users_model)
admin.site.register(keja_tenant_dashboard)
admin.site.register(keja_invoices)
