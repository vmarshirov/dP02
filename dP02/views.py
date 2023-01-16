from django.http import HttpResponse
def index(request):
    return HttpResponse("Привет, мир!")

def abc(request):
    return HttpResponse("Привет, abc!")
