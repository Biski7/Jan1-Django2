from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'App_2/index.html')

def other(request):
    return render(request, 'App_2/other.html')

def another(request):
    return render(request, 'App_2/another.html')