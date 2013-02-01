from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),

    #  Apps
    url(r'^',include('alineproject.apps.home.urls')),
    # url(r'^',include('alineproject.apps.accounts.urls')),
    # url(r'^',include('alineproject.apps.customers.urls')),
    # url(r'^',include('alineproject.apps.feedback.urls')),
    # url(r'^',include('alineproject.apps.projects.urls')),
    # url(r'^',include('alineproject.apps.requirements.urls')),
    # url(r'^',include('alineproject.apps.stages.urls')),
    # url(r'^',include('alineproject.apps.tasks.urls')),
    # url(r'^',include('alineproject.apps.wireframes.urls')),
    
    
)
