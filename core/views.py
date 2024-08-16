# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import jwt
import json
from . import database_conn
from datetime import datetime, timedelta
import hashlib

# Create your views here.

SECRET_KEY = 'your-secret-key'  # Replace with your actual secret key

@csrf_exempt
def login(request):
    if request.method == 'POST':
        # Parse the JSON data
        data = json.loads(request.body.decode('utf-8'))

        # Extract specific fields from the JSON data
        username = data.get('username')
        password = data.get('password')

        # Password should be hashed
        try:
            hashed_password = hashlib.md5(password.encode()).hexdigest()
        except Exception as error:
            return JsonResponse({'error': str(error)}, status=400)
        
        # Custom authentication logic (replace with your own)
        response = database_conn.authenticate(username, hashed_password)
        if response == "User found":
            # Manually create the JWT token
            payload = {
                'username': username,
                'exp': datetime.utcnow() + timedelta(days=14),  # Token expiration time
                'iat': datetime.utcnow(),  # Issued at time
            }
            access_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

            return JsonResponse({'access_token': access_token}, status=200)
        else:
            return JsonResponse({'error': str(response)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        # Parse the JSON data
        data = json.loads(request.body.decode('utf-8'))

        # Extract specific fields from the JSON data
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        # Password should be hashed
        try:
            hashed_password = hashlib.md5(password.encode()).hexdigest()
        except Exception as error:
            return JsonResponse({'error': str(error)}, status=400)

        
        # Custom registration logic (replace with your own)
        response = database_conn.register(Email=email,Username=username,Password=hashed_password)
        if response == "user added":
            # Manually create the JWT token
            payload = {
                'username': username,
                'exp': datetime.utcnow() + timedelta(days=14),  # Token expiration time
                'iat': datetime.utcnow(),  # Issued at time
            }
            access_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

            return JsonResponse({'access_token': access_token}, status=200)
        else:
            return JsonResponse({'error': str(response)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
