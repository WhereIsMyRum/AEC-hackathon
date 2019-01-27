from django.contrib import admin

# Register your models here.

from .models import Element
from .models import ElementAdmin


admin.site.register(Element, ElementAdmin)
