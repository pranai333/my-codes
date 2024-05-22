from django.contrib import admin
from dbapp.models import Employee,Department

# Register your models here.
class Employeeadmin(admin.ModelAdmin):
    list_display=['dptno','dptname']

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['empno','empname','salary','grade','images']
    list_filter=['salary','empname']
    list_editable=['images']
    #search_fields=['empno']
    ordering=['empno']

    def grade(self,object):
        if object.salary>150000:
            return 'Best'
        elif object.salary>100000:
            return 'Average'
        else:
            return 'Low'
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department,Employeeadmin)
#admin.site.register(employeeBooks,EmployeeAdmin)

