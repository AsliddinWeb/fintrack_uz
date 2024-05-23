from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticated

# Jwt
from rest_framework_simplejwt.tokens import RefreshToken

# Local
from .serializers import (RegisterSerializer, LogoutSerializer,
                          AccountUpdateSerializer, AccountImageSerializer)
from .models import Account

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "User created successfully"
            }, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_204_NO_CONTENT)


class AccountImageUpdateView(generics.UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountImageSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.account

class UserUpdateView(generics.UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.account