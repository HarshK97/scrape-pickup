import requests
import json
import random
import string

BASE_URL = "http://127.0.0.1:8000/api"


def generate_random_email():
    return (
        f"testuser_{''.join(random.choices(string.ascii_lowercase, k=5))}@example.com"
    )


def run_verification():
    print("Starting Verification...")

    # 1. Register Client
    email = generate_random_email()
    password = "password123"
    print(f"\n[1] Registering Client with email: {email}")

    payload = {
        "email": email,
        "password": password,
        "full_name": "Test Client",
        "phone_number": "1234567890",
        "address": "123 Test St",
        "city": "Test City",
    }

    try:
        resp = requests.post(f"{BASE_URL}/register/client/", json=payload)
        if resp.status_code == 201:
            print("  SUCCESS: Client registered.")
        else:
            print(f"  FAILED: {resp.status_code} - {resp.text[:2000]}")
            return
    except Exception as e:
        print(f"  ERROR: Could not connect to server. {e}")
        return

    # 2. Login
    print("\n[2] Logging in...")
    login_payload = {"email": email, "password": password}
    resp = requests.post(f"{BASE_URL}/login/", json=login_payload)
    if resp.status_code == 200:
        data = resp.json()
        access_token = data.get("access")
        refresh_token = data.get("refresh")
        print("  SUCCESS: Logged in.")
    else:
        print(f"  FAILED: {resp.status_code} - {resp.text}")
        return

    headers = {"Authorization": f"Bearer {access_token}"}

    # 3. Create Pickup Request
    print("\n[3] Creating Pickup Request...")
    pickup_data = {
        "address": "Pickup Address 123",
        "date": "2025-01-01",
        "time_slot": "10:00 AM - 12:00 PM",
        "latitude": 19.0760,  # Mumbai coordinates example
        "longitude": 72.8777,
    }
    resp = requests.post(
        f"{BASE_URL}/pickup/create/", data=pickup_data, headers=headers
    )

    if resp.status_code == 201:
        req_data = resp.json()
        request_id = req_data.get("request_id")
        print(f"  SUCCESS: Pickup Request Created. ID: {request_id}")
    else:
        print(f"  FAILED: {resp.status_code} - {resp.text}")
        return

    channel = "email"
    print(f"\n[4] Testing OTP Send ({channel})...")
    otp_payload = {"contact": email, "channel": channel}
    resp = requests.post(f"{BASE_URL}/otp/send/", json=otp_payload)
    
    otp = None
    if resp.status_code == 200:
        data = resp.json()
        otp = data.get("mock_otp")
        print(f"  SUCCESS: OTP Sent. Mock OTP: {otp}")
    else:
        print(f"  FAILED: {resp.status_code} - {resp.text}")
        return

    # 5. Verify OTP
    print(f"\n[5] Verifying OTP: {otp}...")
    verify_data = {"contact": email, "otp": otp}
    resp = requests.post(f"{BASE_URL}/otp/verify/", json=verify_data)

    if resp.status_code == 200:
        print("  SUCCESS: OTP Verified.")
    else:
        print(f"  FAILED: {resp.status_code} - {resp.text}")
        return

    print("\n------------------------------------------------")
    print("ALL ENDPOINTS WORKING PROPERLY")
    print("------------------------------------------------")


if __name__ == "__main__":
    run_verification()
