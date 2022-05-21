from django.urls import path, include
from . import views
urlpatterns = [
  path('',views.documentation, name='documentation'),
  path('auth/', include('djoser.urls')),
  path('auth/', include('djoser.urls.jwt')),
  path('api/v1/users',views.getUsers,)
]