from django.shortcuts import render_to_response 
from django.contrib.auth.decorators import login_required
# from company_site.news.models import NewsSummary 
# from company_site.polls.models import Poll

def home(request): 
    # news = NewsSummary.objects.all() 
    # poll = Poll.active.all()[0]
    return render_to_response ('base.html') 

@login_required # Decorator to denote that only authenticated / authorised users can access this view  
def profile(request):
    # employee = UserProfile.objects.get(user=request.user)
    return render_to_response('registration/account_home.html', {'user':request.user }) 