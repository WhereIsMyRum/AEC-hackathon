from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
import requests

from .models import Element
from .forms import ElementForm

def home(request):
    return render(request, 'homepage/index.html')

def search(request):
    product_list = Element.objects.order_by('time_stamp')
    context = {'product_list': product_list}
    return render(request, 'homepage/search.html', context)

def newobject(request):
    if request.method == "POST":
        form = ElementForm(request.POST)
        if form.is_valid():
            elem = form.save(commit=False)
            elem.object_code = "65132168431"
            elem.manufacturer = form['manufacturer'].value()
            elem.model = form['model'].value()
            elem.status = "In production"
            elem.component_type = form['component_type'].value()
            elem.time_stamp = datetime.datetime.now()
            elem.save()
            return HttpResponse("element added")
    else:
        form = ElementForm()
    return render(request, 'homepage/newobject.html', {'form': form})

def detail(request, object_code):
    elem = get_object_or_404(Element, object_code=object_code)
    return render(request, 'homepage/detail.html', {'product': elem})

def postnew(request):
    return

def change(request):
    el = Element.objects.get(pk=1)
    el = Element.objects.first()
    el.status = "Pr"
    el.save()
    return HttpResponse(el.status)
# Create your views here.
