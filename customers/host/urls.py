from django.urls import path
from . import views

urlpatterns=[
  path('',views.become_host, name='become_host'),
  path('dashboard/', views.host_dashboard, name='host_dashboard'),
]