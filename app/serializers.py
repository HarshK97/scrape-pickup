from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data["user"] = {
            "email": self.user.email,
            "full_name": self.user.full_name,
            "is_client": self.user.is_client,
            "is_seller": self.user.is_seller,
        }
        return data


class ClientRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "full_name", "phone_number", "address", "city"]

    def create(self, validated_data):
        validated_data["is_client"] = True
        return User.objects.create_user(**validated_data)


class SellerRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    scrape_types = serializers.ListField(
        child=serializers.CharField(max_length=50), allow_empty=False
    )

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "full_name",
            "phone_number",
            "address",
            "city",
            "scrape_types",
            "business_name",
            "business_type",
            "operating_areas",
            "business_license",
            "gst_certificate",
            "address_proof",
            "id_proof",
        ]

    def create(self, validated_data):
        validated_data["is_seller"] = True
        return User.objects.create_user(**validated_data)
