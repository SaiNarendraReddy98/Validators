from django.contrib import admin
from app.models import *
# Register your models here.

class Studentcustomize(admin.ModelAdmin):
    list_display = ['Sname','Snumber','Slocation','email','renteremail']
    list_display_links = ['Sname']
    
admin.site.register(Student,Studentcustomize)
