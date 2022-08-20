from dataclasses import field
from django.contrib import admin
from api.models import *
# Register your models here.
@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','date_of_birth','state','gender',
    'location','profile_img','resume_doc']
    