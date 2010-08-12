from django.contrib import admin 
from hrms.core.models import Employee, Department, Nationality   
from django.contrib.auth.models import User 

class EmployeeInline(admin.StackedInline):
    model = Employee
    fk_name = 'user'
    max_num = 1
    fieldsets = [
        ('Personal Information', {'fields': ['date_of_birth', 'gender', 'blood_group', 'nationality', 'marital_status']}), 
        ('Employment Information', {'fields': ['employee_number', 'department', 'job_title', 'employee_category', 
		'contract_type', 'pin_number', 'nssf_number', 'nhif_number', 'date_of_hire']}), 
		('Contact Information', {'fields': ['cellphone_number', 'postal_address', 'postal_code', 'physical_address', 
		'town', 'road', 'residence_area', 'house_number' ] } )
    ]

class NewUserAdmin(admin.ModelAdmin):
    inlines = [EmployeeInline, ]	
    # list_display=('user', 'gender', 'department', 'job_title', 'contract_type', 'date_of_hire' ) 
	
class NationalityAdmin (admin.ModelAdmin): 
    # fieldsets=[
	#(None, {'fields':['body']}),  
	#('Date Information', {'fields':['pub_date'], 'classes': ['collapse']}), ] 
    # inlines=[ChoiceInline] 
    list_display=('country_code', 'country', 'nationality_name') 
    list_filter = ['country_code'] 
    search_fields = ['country_code', 'country'] 
	
class DepartmentAdmin (admin.ModelAdmin): 
    # fieldsets=[
	#(None, {'fields':['body']}),  
	#('Date Information', {'fields':['pub_date'], 'classes': ['collapse']}), ] 
    # inlines=[ChoiceInline] 
    list_display=('name_of_department', 'manager', 'description') 
    list_filter = ['name_of_department'] 
    search_fields = ['name_of_department'] 
	
admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
admin.site.register(Department, DepartmentAdmin) 
admin.site.register(Nationality, NationalityAdmin) 
