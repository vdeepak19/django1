from django.shortcuts import render

# Create your views here.
def Homepage(request):
    return render(request, 'homepage.html')

def Homepage1(request):
    return render(request, 'navbar.html')

def page1(request):
    return render(request, 'page1.html')