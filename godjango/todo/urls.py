from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('todo.views',

    url(r'^$', TemplateView.as_view(template_name='index.html')),
        
)
