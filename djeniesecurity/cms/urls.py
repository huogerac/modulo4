from django.conf.urls import patterns, url

from .views import DisplayPage1View, display_page2

urlpatterns = patterns('cms.views',

    #url(r'^cms1/$', SuggestionView.as_view(), name="task_suggest"),
    url(r'^page1$', DisplayPage1View.as_view(), name="link_page1"),
    url(r'^page2$', display_page2, name="link_page2"),
    
)
