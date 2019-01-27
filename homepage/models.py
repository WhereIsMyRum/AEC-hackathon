from django.db import models

# Create your models here.

class Element(models.Model):
    STATUS = (
        ('Pr', "In production"),
        ('Sh', "Shipped out"),
        ('Tr', "In transit"),
        ('Sd', "At the site"),
        ('In', "Installed"),
    )
    object_code = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    status = models.CharField(max_length=2, choices=STATUS)
    component_type = models.CharField(max_length=30)
    time_stamp = models.DateTimeField('Last updated')


    def __str__(self):
        return '%s %s %s %s %s %s' % (self.object_code,
        self.manufacturer, self.model, self.status, self.component_type,
        self.time_stamp)