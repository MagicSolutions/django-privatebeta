try:
	from django.conf.urls import patterns, url
except:
	from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'privatebeta.views.invite', name='privatebeta_invite'),
    url(r'^sent/$', 'privatebeta.views.sent', name='privatebeta_sent'),
)
