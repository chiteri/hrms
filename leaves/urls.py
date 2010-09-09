from django.conf.urls.defaults import * 
from hrms.leaves.models import LeaveApplication  

info_dict = {
    'queryset': LeaveApplication.objects.all()
}

urlpatterns = patterns('hrms.leaves.views', 
    (r'^$', 'leaves_home'),
    (r'^period/(?P<period_id>\d{1,4})/$', 'leaves_in_period'), 
)

urlpatterns += patterns('django.views.generic.list_detail', 
    # (r'^$', 'object_list', info_dict),
    (r'^(?P<object_id>\d+)/details/$', 'object_detail', info_dict), 	
    # url(r'^(?P<object_id>\d+)/results/$', 'object_detail', dict(info_dict, template_name='polls/results.html'), 'poll_results'),
)

#urlpatterns += patterns ('company_site.polls.views', 
#    (r'^(?P<poll_id>\d+)/vote/$', 'vote'), 
#)