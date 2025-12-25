from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import ClientRegistrationSerializer, SellerRegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


def get_auth_response(user, message):
    refresh = RefreshToken.for_user(user)
    return Response(
        {
            "message": message,
            "user": {
                "email": user.email,
                "full_name": user.full_name,
                "is_client": user.is_client,
                "is_seller": user.is_seller,
            },
            "tokens": {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
        },
        status=status.HTTP_201_CREATED,
    )


class ClientRegistrationView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ClientRegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return get_auth_response(user, "Client registered successfully.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellerRegistrationView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = SellerRegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return get_auth_response(user, "Seller registered successfully.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
