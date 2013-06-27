from django.conf.urls import patterns, url

from .views import sms_login

urlpatterns = patterns('sms.views',

    url(r'^sms/login/$', sms_login, name='sms_login'),
                
)
