from django.contrib import admin
from .models import Employee, Position
from .forms import EmployeeForm


class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position)
# admin.site.register(Boss,BossAdmin)