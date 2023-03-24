from django.http import JsonResponse

def home(request):
    return JsonResponse({'message': 'This is a test response.'})