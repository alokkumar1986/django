from django.contrib import admin
from .models import Colour, Flower, Highestqualification, Student, Subject

# Register your models here.
admin.site.register(Highestqualification)
admin.site.register(Colour)
admin.site.register(Flower)
admin.site.register(Subject)
admin.site.register(Student)

