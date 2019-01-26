from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Element

def home(request):
    return render(request, 'homepage/index.html')

def search(request):
    product_list = Element.objects.order_by('time_stamp')
    context = {'product_list': product_list}
    return render(request, 'homepage/search.html', context)

def newobject(request):
    return render(request, 'homepage/newobject.html')

def detail(request, object_code):
    elem = get_object_or_404(Element, object_code=object_code)
    return render(request, 'homepage/detail.html', {'product': elem})


# Create your views here.
