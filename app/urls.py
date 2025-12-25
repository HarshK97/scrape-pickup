from django.urls import path
from .views import ClientRegistrationView, SellerRegistrationView

urlpatterns = [
    path("register/client/", ClientRegistrationView.as_view(), name="register_client"),
    path("register/seller/", SellerRegistrationView.as_view(), name="register_seller"),
]
