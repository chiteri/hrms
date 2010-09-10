from hrms.leaves.models import LeaveApplication
from django.forms import ModelForm 

class LeaveApplicationForm(ModelForm):
    class Meta:
        model = LeaveApplication 
        exclude = ('applicant', 'application_date', 'days_requested', 'status', 'approved_by', 'approval_date', )

