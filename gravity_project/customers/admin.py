from django.contrib import admin
from customers.models import *

# Register your models here.

@admin.register(Customer)
class myapp(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'mobile', 'address', 'created_at', 'updated_at']