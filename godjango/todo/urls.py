from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.views.generic import ListView

from views import DisplayTaskView, DisplayTaskRedirectView, SuggestionView

from .models import Task

urlpatterns = patterns('todo.views',

    url(r'^(?P<task_id>\d+)-(?P<slug>[-\w]+)/$', DisplayTaskView.as_view(), name="task_page"),
    url(r'^(?P<task_id>\d+)/$', DisplayTaskRedirectView.as_view()),
    
    url(r'^tasklistview/$', ListView.as_view(
                                model = Task,
                                paginate_by = '5',
                                queryset = Task.objects.all(),
                                context_object_name = "tasks",
                                template_name='task-listview.html')),
    
    url(r'^suggest/$', SuggestionView.as_view()),
    
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home_page"),
    
    
        
)
