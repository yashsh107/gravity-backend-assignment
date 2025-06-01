from django.contrib import admin
from user.models import * 

# Register your models here.

@admin.register(User)
class myapp(admin.ModelAdmin):
    list_display = ['id', 'email', 'password', 'created_at', 'updated_at']