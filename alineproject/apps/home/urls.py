from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('alineproject.apps.home.views',
	url(r'^$','home',name='home_url'),
	# url(r'^contact/$','contact_view',name='contact_view'),
	# url(r'^pendientes/$','pendientes',name='pendientes_view'),
)