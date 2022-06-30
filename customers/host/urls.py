from django.urls import path
from . import views

urlpatterns=[
  path('dashboard/', views.host_dashboard, name='host_dashboard'),
]