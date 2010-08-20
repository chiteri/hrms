from django.shortcuts import render_to_response 
# from company_site.news.models import NewsSummary 
# from company_site.polls.models import Poll

def home(request): 
    # news = NewsSummary.objects.all() 
    # poll = Poll.active.all()[0]
    return render_to_response ('base.html')