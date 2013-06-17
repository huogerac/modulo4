from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^contact/$', 'contact.views.contact'),
    url(r'^contactbf/$', 'contact.views.contactbf'),
    url(r'^suggestion/$', 'contact.views.suggestion'),
    url(r'^interview/$', 'contact.views.interview'),
    
    # Django-Admin
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'', include('todo.urls')),
)
