from django.contrib import admin 
from hrms.core.models import Employee, Department  
from django.contrib.auth.models import User 

class EmployeeInline(admin.StackedInline):
    model = Employee
    fk_name = 'user'
    max_num = 1
    fieldsets = [
        ('Personal Information', {'fields': ['date_of_birth', 'gender', 'blood_group', 'nationality', 'marital_status']}), 
        ('Employment Information', {'fields': ['employee_number', 'department', 'pin_number', 
		'nssf_number', 'nhif_number', 'date_of_hire']}), ('Contact Information', {'fields': ['cellphone_number', 
		'postal_address', 'postal_code', 'physical_address', 'town', 'road', 'residence_area', 'house_number' ] } )
    ]

class NewUserAdmin(admin.ModelAdmin):
    inlines = [EmployeeInline, ]

admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
admin.site.register(Department) 
