from django.http import JsonResponse

def listDiscounts(request):
    
    return JsonResponse({'message': 'This is a test response.'})
