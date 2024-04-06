from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.utils import timezone

@api_view(['POST'])
@csrf_exempt
def Signup_view(request):
    if request.method == 'POST':
        try:
            data = request.data
            name = data.get('name')
            email = data.get('email')
            role = 'Candidate'
            password = data.get('password')
            account_status = 'Active'
            created_by = 'user'
            created_at = timezone.now()

            # Validate data
            if not name or not email or not password:
                return JsonResponse({'error_message': 'Name, email, and password are required'}, status=400)

            # Create Student object (rename the variable to avoid conflict)
            new_student = Student.objects.create(
                name=name,
                email=email,
                role=role,
                password=password,
                account_status=account_status,
                created_by=created_by,
                created_at=created_at
            )

            # Save Student object
            new_student.save()

            return JsonResponse({'message': 'Data successfully inserted into the database'})

        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'error_message': str(e)}, status=500)

    return JsonResponse({'error_message': 'Invalid request method'}, status=400)
