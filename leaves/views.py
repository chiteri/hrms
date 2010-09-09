from django.shortcuts import render_to_response 
from django.contrib.auth.decorators import login_required 
from hrms.core.models import FinancialPeriod 
from hrms.leaves.models import LeaveApplication 
# Create your views here.

@login_required # Decorator to denote that only authenticated / authorised users can access this view  
def leaves_home(request):
    # employee = UserProfile.objects.get(user=request.user)
    f = FinancialPeriod.objects.all() 
    return render_to_response('leaves/leaves_home.html', {'user':request.user, 'periods':f }) 

@login_required 	
def leaves_in_period(request, period_id): 
    pid = period_id # obtain the period id passed as a second parameter to the view 
    period = FinancialPeriod.objects.get(pk=pid) 
    applications = LeaveApplication.objects.filter(start_date__gte=period.begins_from, end_date__lte=period.ends_at ) 
    return render_to_response('leaves/list_of_leaves.html', 
	{'period':period, 'leave_applications':applications, 'user':request.user })     

    