from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
  path('',views.documentation, name='documentation'),
  path('auth/', include('djoser.urls')),
  path('auth/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('api/v1/users/',views.getUsers,),
  path('auth/activate/<str:uid>/<str:token>/',views.activate),
  path('auth/password_reset_request/',views.reset_password_request),
  path('auth/password_reset/<str:uidb64>/<str:token>/',views.reset_password),
  path('auth/set_new_password/',views.set_new_password)
]