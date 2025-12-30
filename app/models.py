from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=150, blank=True)

    # Common Fields
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)

    # Role Flags
    is_client = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    # Vendor Specific Fields
    business_name = models.CharField(max_length=255, blank=True)
    business_type = models.CharField(max_length=100, blank=True)
    operating_areas = models.TextField(blank=True, help_text="Comma separated list of cities")
    
    # Documents
    business_license = models.FileField(upload_to="vendor_docs/license/", blank=True, null=True)
    gst_certificate = models.FileField(upload_to="vendor_docs/gst/", blank=True, null=True)
    address_proof = models.FileField(upload_to="vendor_docs/address/", blank=True, null=True)
    id_proof = models.FileField(upload_to="vendor_docs/id/", blank=True, null=True)

    # Verification Flags
    is_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)

    # storing list like ["PAPER", "GLASS"]
    scrape_types = models.JSONField(default=list, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
