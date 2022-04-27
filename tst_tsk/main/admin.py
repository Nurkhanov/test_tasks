import imp
from django.contrib import admin
from pkg_resources import empty_provider
from .models import Employee, Position, Boss


# Register your models here.
admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Boss)