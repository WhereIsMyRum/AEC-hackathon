from django.shortcuts import render

from .models import Element

def home(request):
    return render(request, 'homepage/index.html')

def search(request):
    product_list = Element.objects.order_by('time_stamp')
    context = {'product_list': product_list}
    return render(request, 'homepage/search.html', context)

def newobject(request):
    return render(request, 'homepage/newobject.html')


# Create your views here.
