from tastypie.resources import ModelResource
from homepage.models import Element

class ElementResource(ModelResource):
    class Meta:
        queryset = Element.objects.all()
        resource_name = 'element'