# gravity-backend-assignment

Django REST API with JWT Authentication and PostgreSQL Integration

Features :

- User Registration
- JWT Auth (Token-based login)
- Customer CRUD (Create, Read, Update, Delete)
- Search
- Pagination
- PostgreSQL support

---
Tech Stack

- Python
- Django + DRF
- PostgreSQL
- SimpleJWT

---

Setup Instructions

1. Clone the repo

2. Create a virtual environment
   python -m venv env
   source env/bin/activate

3. Install dependencies  
   pip install -r requirements.txt

4. Create .env file 
   Use .env.example as a template:

5. Setup PostgreSQL
   Make sure PostgreSQL is installed and running. Create a database and user:

    CREATE DATABASE your_db_name;
    CREATE USER your_user WITH PASSWORD 'your_password';
    ALTER ROLE your_user SET client_encoding TO 'utf8';
    ALTER ROLE your_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE your_user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_user;
    ALTER USER your_username WITH SUPERUSER;

6. Run migrations 

   python manage.py makemigrations
   python manage.py migrate

7. Run the server
   
   python manage.py runserver


------

API Usage

User

1. Register User
   
   Endpoint:
   POST /api/register/ 

   Request Body:
   {
    "email": "user@example.com",
    "password": "strongpassword",
    "confirm_password": "strongpassword"
   }

   
   Response (Success):
   {
    "detail": "Operation Successful",
    "result": {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0ODgxMzMzMywiaWF0IjoxNzQ4NzI2OTMzLCJqdGkiOiJiZWU5OTc2OGY1MjE0ZTdiYjFkYWFkOTc4OTM3NGIyYiIsInVzZXJfaWQiOiJjNTY1MzNmMC1lZTE2LTQ0ZTItYjgyNi0zZmQ4M2VhZjk1MjgifQ.OxHQ9YxhsdyxWjJwmEIKYbYlFCxUHAgBQCc9nW5quVs",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ4NzI3MjMzLCJpYXQiOjE3NDg3MjY5MzMsImp0aSI6ImYyMWE3ZTQwNzljOTQ0MWRhNzllZDk1YmYxOGQ5MTBhIiwidXNlcl9pZCI6ImM1NjUzM2YwLWVlMTYtNDRlMi1iODI2LTNmZDgzZWFmOTUyOCJ9.2i7LRBSd_-_8W_jTaoS7x7Pp5VOiIiPykijcRE1vh2o"
    }
    }


2. Token Generation

   Endpoint:
   POST /api/token/

   Request Body:
   {
    "email": "user@example.com",
    "password": "strongpassword"
   }

   Response (Success):
   {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc4MDMwMDgxOCwiaWF0IjoxNzQ4NzY0ODE4LCJqdGkiOiJkN2I1NzFlYTI2ZmY0ODEzODYxMGM5ZGRhNTYzMGM0MSIsInVzZXJfaWQiOiI4MzZkNWJiNi1iMGQ5LTRlMDEtYWJiNS1mNWM1ODI4MGE0NDAifQ.pAuSpn1oHhFnvZgQN6_c0f7-mJ2Se9WNRNyh1LCktdY",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgwMzAwODE4LCJpYXQiOjE3NDg3NjQ4MTgsImp0aSI6ImU1MGMwM2Q3ZDkyYjRlZDg4NGRkYzhjODUyYjU1NTNkIiwidXNlcl9pZCI6IjgzNmQ1YmI2LWIwZDktNGUwMS1hYmI1LWY1YzU4MjgwYTQ0MCJ9.05QOv4ycsJ2lTmxusvhxT05VotwaQAQhqtXX3gz_RiY"
    }


3. Refresh Token

   Endpoint:
   POST /api/token/refresh/

   Request Body:
   {
    "refresh": "token"
   }

   Response (Success):
   {
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ4NzI4NDA2LCJpYXQiOjE3NDg3MjgwNzAsImp0aSI6IjcyNDdiNmQwMTU4MDQxMDQ4OWQwY2ZhNGM3NDcyMmEwIiwidXNlcl9pZCI6IjgzNmQ1YmI2LWIwZDktNGUwMS1hYmI1LWY1YzU4MjgwYTQ0MCJ9.gSKlAQuISSaSUXx5bs51T72_URy5VOzd-vUGs16mU-0"
   }


Customers 

1. Create a new customer

   Endpoint:
   POST /api/customers/

   Request Headers:
   Authorization: Bearer <jwt_access_token>

   Request Body:
   {
    "name": "John Doe",
    "email": "John Doe",
    "mobile": "+1234567890",
    "address": "123 Main Street"
   }

   Response (Success):
   {
    "id": "7c4b96b0-ba64-4b77-904f-2fdf198f811e",
    "name": "John Doe",
    "email": "John Doe",
    "mobile": "+1234567890",
    "address": "123 Main Street"
    "created_at": "2025-06-01T13:51:23.342551",
    "updated_at": "2025-06-01T13:51:23.342567"
   }


2. List all customers

   Endpoint:
   GET /api/customers/

   Request Headers:
   Authorization: Bearer <jwt_access_token>

   Query Parameters:

   search — filters by name or email containing the value
   page — pagination page number

   Response (Success):
   {
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "baab6296-4c9d-4e27-8c49-14147d1d899b",
            "name": "Yash",
            "email": "yash@gmail.com",
            "mobile": "9424221883",
            "address": "Pandri Raipur",
            "created_at": "2025-06-01T13:21:19.192280",
            "updated_at": "2025-06-01T13:22:04.400377"
        },
        {
            "id": "12b5f74e-9da9-433d-927e-743954937402",
            "name": "Yash Sharma",
            "email": "yashshh@gmail.com",
            "mobile": "7974807001",
            "address": "Shankar nagar Raipur",
            "created_at": "2025-06-01T13:27:21.751170",
            "updated_at": "2025-06-01T13:27:21.751220"
        }
    ]
    }


3. Get a specific customer

   Endpoint:
   GET /api/customers/<id>/

   Request Headers:
   Authorization: Bearer <jwt_access_token>

   Response (Success):
   {
    "id": "baab6296-4c9d-4e27-8c49-14147d1d899b",
    "name": "Yash",
    "email": "yash@gmail.com",
    "mobile": "9424221883",
    "address": "Pandri Raipur",
    "created_at": "2025-06-01T13:21:19.192280",
    "updated_at": "2025-06-01T13:22:04.400377"
   }


4. Update Customer Info

   Endpoint:
   PUT /api/customers/<id>/

   Request Headers:
   Authorization: Bearer <jwt_access_token>

   Request Body:
   {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "mobile": "+1234567890",
    "address": "123 Main Street"
   }

   Response (Success):
   {
    "id": "baab6296-4c9d-4e27-8c49-14147d1d899b",
    "name": "Johnathan Doe",
    "email": "john.doe@example.com",
    "mobile": "+1234567890",
    "address": "456 New Address",
    "created_at": "2025-06-01T13:21:19.192280",
    "updated_at": "2025-06-01T13:22:04.400377"
   }   


5. Delete a Customer

   Endpoint:
   DELETE /api/customers/<id>/

   Request Headers:
   Authorization: Bearer <jwt_access_token>

   Response (Success):
   Status code: 204 No Content