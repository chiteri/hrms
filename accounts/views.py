from django.shortcuts import render_to_response 
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect

def home(request): 
    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/accounts/profile/') 
		
    return render_to_response ('base.html') 

@login_required # Decorator to denote that only authenticated / authorised users can access this view  
def profile(request):
    # employee = UserProfile.objects.get(user=request.user)
    return render_to_response('registration/account_home.html', {'user':request.user }) 