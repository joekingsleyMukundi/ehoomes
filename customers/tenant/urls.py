from django.urls import path
from . import views

urlpatterns = [
  path('dashboard/', views.tenant_dashboard, name='tenant_dashboard'),
  path('profile/', views.tenant_profile, name='tenant_profile'),
]