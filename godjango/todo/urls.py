from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from views import DisplayTaskView, DisplayTaskRedirectView

urlpatterns = patterns('todo.views',

    url(r'^(?P<task_id>\d+)-(?P<slug>[-\w]+)/$', DisplayTaskView.as_view()),
    url(r'^(?P<task_id>\d+)/$', DisplayTaskRedirectView.as_view()),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
        
)
