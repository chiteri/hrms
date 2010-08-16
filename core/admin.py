from django.contrib import admin 
from hrms.core.models import Employee, Department, Nationality, FinancialPeriod,\
HomeContact, SummerContact, Spouse, Dependant, NextOfKin, AcademicQualification, DocumentsChecklist   
from django.contrib.auth.models import User 

class SpouseInline(admin.TabularInline):
    model = Spouse 
    extra = 1 
    max_num = 1 
	
class HomeContactInline(admin.TabularInline):
    model = HomeContact 
    extra = 1 
    max_num = 1 

class SummerContactInline(admin.TabularInline):
    model = SummerContact 
    extra = 1 
    max_num = 2
	
class NextOfKinInline(admin.TabularInline):
    model = NextOfKin 
    extra = 3 
    max_num = 4 

class DependantInline(admin.TabularInline):
    model = Dependant 
    extra = 3 
    max_num = 6 
	
class AcademicQualificationInline(admin.TabularInline):
    model = AcademicQualification 
    extra = 3 
    max_num = 6 
	
class DocumentsChecklistInline(admin.TabularInline):
    model = DocumentsChecklist 
    extra = 3 
    max_num = 6 
	
class EmployeeInline(admin.StackedInline):
    model = Employee
    fk_name = 'user'
    max_num = 1 
    # inlines = [SpouseInline, HomeContactInline, SummerContactInline, NextOfKinInline,  DependantInline, AcademicQualificationInline,] 
    list_filter = ['citizen'] 
    fieldsets = [
        ('Personal Information', {'fields': ['date_of_birth', ('gender', 'marital_status'), 'blood_group', 
		('nationality', 'citizen'), 'national_id_or_passport'], 'classes': [ 'extrapretty']}), 
        ('Employment Information', {'fields': ['employee_number', 'date_of_hire', ('department', 'job_title'), 
		('employee_category', 'contract_type'), 'pin_number', ('nssf_number', 'nhif_number') ], 'classes': [ 'extrapretty'] }), 
		('Contact Information', {'fields': ['cellphone_number', ('postal_address', 'postal_code'), 'town', 'road', 
		('physical_address', 'house_number'), 'residence_area' ], 'classes': [ 'extrapretty'] } )
    ] 
	
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('user', 'employee_number', 'gender', 'date_of_hire', 'department', 'job_title', 'contract_type' )
    inlines = [SpouseInline, HomeContactInline, SummerContactInline, NextOfKinInline,  DependantInline, 
	AcademicQualificationInline, DocumentsChecklistInline ] 
    list_filter = ['citizen', 'gender', 'employee_category'] 
    fieldsets = [  ('User Information', {'fields': ['user'], 'classes': [ 'extrapretty']}),
        ('Personal Information', {'fields': ['date_of_birth', ('gender', 'marital_status'), 'blood_group', 
		('nationality', 'citizen'), 'national_id_or_passport'], 'classes': [ 'extrapretty']}), 
        ('Employment Information', {'fields': [('employee_number', 'supervisor'), 'date_of_hire', ('department', 'job_title'), 
		('employee_category', 'contract_type'), 'pin_number', ('nssf_number', 'nhif_number') ], 'classes': [ 'extrapretty'] }), 
		('Contact Information', {'fields': ['cellphone_number', ('postal_address', 'postal_code'), 'town', 'road', 
		('physical_address', 'house_number'), 'residence_area' ], 'classes': [ 'extrapretty'] } ), 
        ('Documents Collected Check-list', {'fields': [], 'classes': [ 'extrapretty', 'collapse']}),
    ] 
    search_fields  = ['employee_number', 'national_id_or_passport']

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
    search_fields = ['country_code', 'country', 'nationality_name'] 
	
class FinancialPeriodAdmin(admin.ModelAdmin): 
    list_display=('begins_from', 'ends_at', 'description') 
    list_filter = ['begins_from'] 
    # search_fields = ['country_code', 'country'] 
	
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
admin.site.register(Employee, EmployeeAdmin) 
admin.site.register(FinancialPeriod, FinancialPeriodAdmin) 
