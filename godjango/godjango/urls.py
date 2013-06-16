from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^contact/$', 'contact.views.contact'),
    url(r'^contactbf/$', 'contact.views.contactbf'),
    url(r'^suggestion/$', 'contact.views.suggestion'),
    url(r'^interview/$', 'contact.views.interview'),
    
    # url(r'^$', 'godjango.views.home', name='home'),
    # url(r'^godjango/', include('godjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'', include('todo.urls')),
)
