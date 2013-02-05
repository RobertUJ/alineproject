from django.conf.urls.defaults import patterns,url
urlpatterns = patterns('alineproject.apps.accounts.views',
	url(r'^accounts/$','login',name='login_url'),
)



	
