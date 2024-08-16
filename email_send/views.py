from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def send(request):
    if request.method == "POST":
        try:
            # Parse the JSON data
            data = json.loads(request.body.decode('utf-8'))

            # Define the required fields
            required_fields = ['username', 'emergency_contacts', 'user_message']

            # Check if all required fields are present
            missing_fields = [field for field in required_fields if field not in data]

            if missing_fields:
                return JsonResponse({
                    'error': 'Missing fields',
                    'missing_fields': missing_fields
                }, status=400)

            username = data.get('username')
            emergency_contacts = data.get('emergency_contacts')
            user_message = data.get('user_message')


            subject = f"EMERGENCY: {username} NEEDS HELP!!!" 
            message = f"{user_message}|| THIS IS AN AUTO_GENERATED MESSAGE SENT BY {username} BECAUSE THEY NEED YOUR HELP. PS. NOTE THIS IS FOR A PROJECT AND NOBODY IS ACTUALLY IN DANGER"

            with get_connection(host=settings.EMAIL_HOST,port=settings.EMAIL_PORT,username=settings.EMAIL_HOST_USER,password=settings.EMAIL_HOST_PASSWORD, use_tls=settings.EMAIL_USE_TLS) as connection:  
                email_from = settings.EMAIL_HOST_USER  
                recipient_list = emergency_contacts
                EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
            return JsonResponse({'success': 'Email has been sent'}, status=200)
        except Exception as error:
            return JsonResponse({'error': str(error)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)