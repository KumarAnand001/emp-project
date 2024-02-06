from django.contrib import admin
from testApp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):

    list_display = [

        'eNo',
        'eName',
        'eSal',
        'eAdd'
    ]
# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
