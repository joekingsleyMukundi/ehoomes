from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from decorators.custom_auth_decorators import authenticate_user
from errors.validationerror import ValidationError


# Create your views here.
@api_view(['GET'])
@authenticate_user
def tenant_dashboard(request):
    userEmail = request.user['email']
    tenant = keja_tenant_dashboard.objects.get(user__email=userEmail)
    serializer = TenantDashboardSerializer(tenant, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@authenticate_user
def user_profile(request):
    if request.method == 'POST':
        try:
            serializer = UpdateUserProfileSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            return Response({"success": True, 'user': serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            raise ValidationError("some or all the values are missing")

    userEmail = request.user['email']
    user = users_model.objects.get(email=userEmail)
    serializer = UserProfileSerializer(user, many=False)
    return Response(serializer.data)
