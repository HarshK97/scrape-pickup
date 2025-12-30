from twilio.rest import Client
import os
import random

class OTPService:
    def __init__(self):
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.service_sid = os.getenv("TWILIO_SERVICE_SID") # Optional if using Verify API
        self.phone_number = os.getenv("TWILIO_PHONE_NUMBER")
        
        self.client = None
        if self.account_sid and self.auth_token:
            try:
                self.client = Client(self.account_sid, self.auth_token)
            except Exception as e:
                print(f"Twilio Client Init Error: {e}")

    def send_otp(self, phone_number):
        """
        Sends an OTP to the given phone number.
        Returns the OTP code if successful (or if using mock/fallback), else None.
        """
        # Generate a random 4-digit OTP
        otp_code = str(random.randint(1000, 9999))

        if self.client and self.phone_number:
            try:
                message = self.client.messages.create(
                    body=f"Your Pickup Request OTP is: {otp_code}",
                    from_=self.phone_number,
                    to=phone_number
                )
                print(f"OTP Sent via Twilio SID: {message.sid}")
                return otp_code
            except Exception as e:
                print(f"Failed to send OTP via Twilio: {e}")
                # Fallback to returning OTP for local testing/dev
                return otp_code
        else:
            print(f"Twilio not configured. MOCK OTP: {otp_code}")
            return otp_code

    def verify_otp(self, input_otp, expected_otp):
        """
        Simple verification logic. 
        Could be expanded to use Twilio Verify API later.
        """
        return input_otp == expected_otp
