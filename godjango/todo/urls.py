from django.conf.urls import patterns, url
from django.views.generic import TemplateView, ListView, DetailView

from views import DisplayTaskView, DisplayTaskRedirectView, SuggestionView

from .models import Task

urlpatterns = patterns('todo.views',

    url(r'^(?P<task_id>\d+)-(?P<slug>[-\w]+)/$', DisplayTaskView.as_view(), name="task_page_old"),
    url(r'^(?P<task_id>\d+)/$', DisplayTaskRedirectView.as_view()),
    
    # using convertion open task_list.html template
    url(r'^tasklistview/$', ListView.as_view(
                                model = Task,
                                paginate_by = '5',
                                queryset = Task.objects.all(),
                                context_object_name = "tasks",), name="task_list"),
    
    url(r'^suggest/$', SuggestionView.as_view(), name="task_suggest"),
        
    # using convertion open task_detail.html template
    url(r'^detail/(?P<pk>\d+)-(?P<slug>[-\w]+)/$', DetailView.as_view(
                                context_object_name="task",
                                model=Task,), name="task_destail"),
    
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home_page"),
    
    
        
)
