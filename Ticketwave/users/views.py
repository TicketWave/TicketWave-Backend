from django.http import JsonResponse
from django.contrib.auth.models import User

def home(request):
    return JsonResponse({'message': 'This is a test response.'})
def user_profile(request):
    user=request.user
    # user_data={
    #     'id'=user.id
    #     'name'=user.name
    #     'fist_name'=user.first_name
    #     'last_name'=user.last_name
    #     'is_public'=user.is_public
    #     'image_id'=user.image_id
    #     'email'=user_emails.email
    #     'verified'=user_emails.verified
    # }
    return JsonResponse(user_data)
