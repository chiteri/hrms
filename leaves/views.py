from django.core.context_processors import csrf 
from django.template import RequestContext
from django.shortcuts import render_to_response 
from django.contrib.auth.decorators import login_required 
from hrms.core.models import Employee, Department, FinancialPeriod 
from hrms.leaves.models import LeaveApplication 
from hrms.leaves.forms import LeaveApplicationForm
from django.http import HttpResponseRedirect 

# Create your views here.
@login_required # Decorator to denote that only authenticated / authorised users can access this view  
def leaves_home(request):
    # employee = UserProfile.objects.get(user=request.user)
    fpr = FinancialPeriod.objects.all() 
    return render_to_response('leaves/leaves_home.html', {'user':request.user, 'periods':fpr }) 

@login_required 	
def leaves_in_period(request, period_id): 
    pid = period_id # obtain the period id passed as a second parameter to the view 
    period = FinancialPeriod.objects.get(pk=pid) 
    applications = LeaveApplication.objects.filter(start_date__gte=period.begins_from, end_date__lte=period.ends_at ) 
    return render_to_response('leaves/list_of_leaves.html', 
	{'period':period, 'leave_applications':applications, 'user':request.user })     

@login_required 	
def apply(request): 
	
    errors = []
    if request.method == 'POST':
        form = LeaveApplicationForm(request.POST)
        if form.is_valid():
            employee = Employee.objects.get(user=request.user) 
			
			# Determine the department of an amployee so that its head can approve the leave 
            manager = Employee.objects.get(user=employee.department.manager)
			
            # print manager.first_name 
            # return 

            cd = form.cleaned_data 
			
			# Collect the rest of the info from the application form 
            application = LeaveApplication (applicant=employee, start_date=cd['start_date'], 
			end_date=cd['end_date'], type=cd['type'], days_requested=0,description=cd['description'] , 
			half_day=cd['half_day'], status=1, approved_by=manager)
			
			# Save the data
            application.save() 
            #return HttpResponseRedirect('/leaves/apply/outcome/')
            return render_to_response('leaves/leaves_home.html') 
    else: 
        form = LeaveApplicationForm()
		
    return render_to_response('leaves/application_form.html', {'form':form}, context_instance=RequestContext(request) )
    