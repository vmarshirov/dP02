from django.http import HttpResponse


def index(request):
    return HttpResponse("App1, Привет, мир!")


def f_int(request, value):
    print(value)
    return HttpResponse(f"int, {value}")
