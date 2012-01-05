from django.conf.urls.defaults import * 
from hrms.leaves.models import LeaveApplication  

info_dict = {
    'queryset': LeaveApplication.objects.all()
}

urlpatterns = patterns('hrms.leaves.views', 
    (r'^$', 'leaves_home'),
    (r'^period/(?P<period_id>\d{1,4})/$', 'leaves_in_period'), 
    (r'^apply/$', 'apply'), 
)

urlpatterns += patterns('django.views.generic.list_detail', 
    (r'^(?P<object_id>\d+)/details/$', 'object_detail', info_dict), 	
)
