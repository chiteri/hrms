from django.contrib import admin  
from hrms.core.models import Employee, FinancialPeriod  
from hrms.leaves.models import Holiday, LeaveApplication 

class HolidayAdmin(admin.ModelAdmin): 
    list_display=('name', 'type', 'period', 'begins_from', 'ends_at', 'description') 
    list_filter = ['type', 'period'] 
    search_fields = ['name'] 

class LeaveApplicationAdmin(admin.ModelAdmin): 
    list_display=('applicant', 'application_date', 'type', 'start_date', 'end_date', 'days_requested', 'status') 
    list_filter = ['applicant', 'application_date', 'type', 'status'] 
    search_fields = ['applicant'] 	
	
admin.site.register(Holiday, HolidayAdmin) 
admin.site.register(LeaveApplication, LeaveApplicationAdmin)