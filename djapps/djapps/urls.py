from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',

    # admin:
    url(r'^admin/', include(admin.site.urls)),

    #dajaxice
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

    # Examples:
    # url(r'^$', 'djapps.views.home', name='home'),
    # url(r'^djapps/', include('djapps.foo.urls')),

)

urlpatterns += patterns('',
    url(r'', include('djajax.urls')),
)
