from django.shortcuts import render

def home(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')

def products(request):
    return render(request, 'homepage/products.html')
# Create your views here.
