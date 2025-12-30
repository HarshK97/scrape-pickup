# API Documentation

Base URL: `http://127.0.0.1:8000/api`

## Authentication

### 1. Register Client
**Endpoint**: `POST /register/client/`

```bash
curl -X POST http://127.0.0.1:8000/api/register/client/ \
-H "Content-Type: application/json" \
-d '{
    "email": "client@example.com",
    "password": "strongpassword",
    "full_name": "Client Name",
    "phone_number": "1234567890",
    "address": "123 Main St",
    "city": "New York"
}'
```

### 2. Register Seller
**Endpoint**: `POST /register/seller/`

```bash
curl -X POST http://127.0.0.1:8000/api/register/seller/ \
-H "Content-Type: application/json" \
-d '{
    "email": "seller@example.com",
    "password": "strongpassword",
    "full_name": "Seller Name",
    "phone_number": "0987654321",
    "address": "456 Market St",
    "city": "New York",
    "scrape_types": ["PAPER", "PLASTIC"]
}'
```

### 3. Login
**Endpoint**: `POST /login/`

```bash
curl -X POST http://127.0.0.1:8000/api/login/ \
-H "Content-Type: application/json" \
-d '{
    "email": "client@example.com",
    "password": "strongpassword"
}'
```

**Response**:
```json
{
  "message": "...",
  "user": { ... },
  "access": "<ACCESS_TOKEN>",
  "refresh": "<REFRESH_TOKEN>"
}
```

---

## Pickup Request Flow

**Note**: All pickup endpoints require `Authorization: Bearer <ACCESS_TOKEN>` header.

### 1. Create Pickup Request
**Endpoint**: `POST /pickup/create/`
**Content-Type**: `multipart/form-data` (to support image upload)

```bash
curl -X POST http://127.0.0.1:8000/api/pickup/create/ \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-F "address=789 Pickup Lane" \
-F "latitude=40.7128" \
-F "longitude=-74.0060" \
-F "date=2025-01-15" \
-F "time_slot=09:00 AM - 11:00 AM" \
-F "scrape_image=@/path/to/image.jpg"
```

**Response**:
```json
{
    "message": "Pickup request initiated.",
    "request_id": 10,
    "status": "pending"
}
```

### 2. Add Contact Info & Send OTP
**Endpoint**: `POST /pickup/contact/`

```bash
curl -X POST http://127.0.0.1:8000/api/pickup/contact/ \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-F "request_id=10" \
-F "contact_name=John Doe" \
-F "contact_phone=5550001111"
```

**Response**:
```json
{
    "message": "Contact info updated. OTP sent.",
    "request_id": 10,
    "mock_otp": "1234"
}
```

### 3. Verify OTP
**Endpoint**: `POST /pickup/verify-otp/`

```bash
curl -X POST http://127.0.0.1:8000/api/pickup/verify-otp/ \
-H "Content-Type: application/json" \
-d '{
    "request_id": 10,
    "otp": "1234"
}'
```

**Response**:
```json
{
    "message": "Phone verified. Pickup confirmed."
}
```
