from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mmu.views.home', name='home'),
    # url(r'^mmu/', include('mmu.foo.urls')),
    url(r'^$', 'middmusic.views.index'),

	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.MEDIA_ROOT,
	}),

	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.STATIC_ROOT,
	}),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
