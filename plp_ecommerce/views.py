from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to the PLP Ecommerce Page</h1>")
