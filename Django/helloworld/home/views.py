from django.http import HttpResponse


# Create your views here.
def helloworld(request):
    return HttpResponse("hello world")
