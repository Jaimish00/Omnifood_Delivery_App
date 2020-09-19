from django.http import JsonResponse

# Create your views here.
def home(request):
    return JsonResponse({'info': 'Omnifood Service', 'further_info': 'A Final Year Project'})