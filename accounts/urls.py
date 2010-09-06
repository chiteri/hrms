from django.conf.urls.defaults import * 

urlpatterns = patterns('hrms.accounts.views', 
    (r'^$', 'home'), 
    (r'^profile/$', 'profile'), 	
 )

urlpatterns += patterns ( 'django.contrib.auth.views', 
    # (r'^login/$', 'login', {'template_name': 'regsitration/login.html', 'redirect_field_name':'leaves/base_leaves.html'} ), 
    (r'^login/$', 'login'), 
    (r'^logout/$', 'logout'), 
    # {'template_name': 'regsitration/login.html', 'redirect_field_name':'leaves/base_leaves.html'} ), 
)