from django.shortcuts import render_to_response 
from django.contrib.auth.decorators import login_required 
from hrms.core.models import FinancialPeriod 
# Create your views here.

@login_required # Decorator to denote that only authenticated / authorised users can access this view  
def leaves_home(request):
    # employee = UserProfile.objects.get(user=request.user)
    f = FinancialPeriod.objects.all() 
    return render_to_response('leaves/leaves_home.html', {'user':request.user, 'periods':f }) 