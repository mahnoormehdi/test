from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page requested")
    friends=['maha','ali','mish']
    return JsonResponse(friends,safe=False)