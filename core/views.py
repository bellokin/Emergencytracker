# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import jwt
from . import database_conn
from datetime import datetime, timedelta

# Create your views here.

SECRET_KEY = 'your-secret-key'  # Replace with your actual secret key

@csrf_exempt
def login(request):
    if request.method == 'POST':
        # Parse the request data
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Custom authentication logic (replace with your own)
        if database_conn.authenticate(username, password):
            # Manually create the JWT token
            payload = {
                'username': username,
                'exp': datetime.utcnow() + timedelta(days=14),  # Token expiration time
                'iat': datetime.utcnow(),  # Issued at time
            }
            access_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

            return JsonResponse({'access_token': access_token}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
def signup(request):
    pass
