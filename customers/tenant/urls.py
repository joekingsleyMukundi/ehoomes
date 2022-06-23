from django.urls import path
from . import views

urlpatterns = [
  path('dashboard/', views.tenant_dashboard, name='tenant_dashboard'),
  path('profile/', views.user_profile, name='user_profile'),
]