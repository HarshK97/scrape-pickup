from django.urls import path
from .views import ClientRegistrationView, SellerRegistrationView, SendOTPView, VerifyOTPView

urlpatterns = [
    path("register/client/", ClientRegistrationView.as_view(), name="register_client"),
    path("register/seller/", SellerRegistrationView.as_view(), name="register_seller"),
    path("otp/send/", SendOTPView.as_view(), name="otp_send"),
    path("otp/verify/", VerifyOTPView.as_view(), name="otp_verify"),
]
