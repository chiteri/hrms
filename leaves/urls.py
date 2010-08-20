from django.conf.urls.defaults import * 
# from company_site.polls.models import Poll 

#info_dict = {
#    'queryset': Poll.objects.all(),
#}

urlpatterns = patterns('django.views.generic.list_detail', 
    #(r'^$', 'object_list', info_dict),
    #(r'^(?P<object_id>\d+)/$', 'object_detail', info_dict), 	
    # url(r'^(?P<object_id>\d+)/results/$', 'object_detail', dict(info_dict, template_name='polls/results.html'), 'poll_results'),
)

#urlpatterns += patterns ('company_site.polls.views', 
#    (r'^(?P<poll_id>\d+)/vote/$', 'vote'), 
#)