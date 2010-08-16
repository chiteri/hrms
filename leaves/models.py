from django.db import models 
from hrms.core.models import Employee, FinancialPeriod 
import datetime 

# Create your models here.  
# A model for all the Public and Work holidays 
class Holiday(models.Model):  
    PUBLIC_HOLIDAY = 1
    WORK_HOLIDAY = 2 
    OTHER_HOLIDAY = 3 
    HOLIDAY_TYPES = (
        (PUBLIC_HOLIDAY, 'Public Holiday'), 
        (WORK_HOLIDAY, 'Work Holiday'), 
        (OTHER_HOLIDAY, 'Other Holiday'), 
	)
    # Core Fields 
    begins_from = models.DateField(blank=False, help_text="Day when the holiday starts.") 
    ends_at = models.DateField(blank=False, help_text="Day when the holiday ends.")  
    name = models.CharField(blank=False, max_length=25) 
    type = models.IntegerField(max_length=1, blank=False, choices=HOLIDAY_TYPES) 
    period = models.ForeignKey(FinancialPeriod, blank=False)
    description = models.TextField(max_length=100, help_text="A description about the holiday / its relevance.") 
	
    def __unicode__(self): 
        return u"%s"%(self.name)

# A model for the leaves in the system  
class LeaveCategory(models.Model): 
    name = models.CharField(blank=False, max_length=25, unique=True) 
    days_assigned = models.IntegerField(blank=False, max_length=3, default=0) 
    description = models.TextField(blank=False)
    accumulates = models.BooleanField(default=False) 
	
    class Meta: 
        verbose_name_plural = 'Leave Categories' 
		
    def __unicode__(self): 
        return u"%s"%(self.name) 
		
# Model for leave applications 
class LeaveApplication(models.Model): 
    # Leave statuses 
    PENDING = 1
    APPROVED = 2 
    REJECTED = 3 
    CANCELLED = 4 
    LEAVE_APPLICATION_STATUSES = (
        (PENDING, 'Pending'), 
        (APPROVED, 'Approved'), 
        (REJECTED, 'Rejected'), 
        ( CANCELLED, 'Cancelled'), 
	)

    # Core Fields 
    applicant = models.ForeignKey(Employee, related_name='leave_application_submitter')
    application_date = models.DateTimeField(blank=False, default=datetime.datetime.now) 
    start_date = models.DateTimeField(blank=False, default=datetime.datetime.now) 
    end_date = models.DateTimeField(blank=False, default=datetime.datetime.now) 
    type = models.ForeignKey(LeaveCategory, blank=False)
    days_requested = models.IntegerField(blank=False, max_length=2, default=1) 
    description = models.TextField(blank=False, help_text="A short explanation why the leave is being requested") 
    half_day = models.BooleanField(default=False, help_text="Check if the leave is being applied for is for half a day.")  
    status = models.IntegerField(blank=False, max_length=1, choices=LEAVE_APPLICATION_STATUSES ) 
    approved_by = models.ForeignKey(Employee,related_name='leave_application_approver') # For applications that are cancelled, etc
    approval_date = models.DateTimeField(blank=False, default=datetime.datetime.now) 
	
# TODO: Model the Leave entitlement to employees and How to carry them over across periods  
