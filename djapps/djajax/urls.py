from django.conf.urls import patterns, url

from .views import DisplayPage1View
from djajax.views import DisplayPage2View

urlpatterns = patterns('djajax.views',

    #url(r'^cms1/$', SuggestionView.as_view(), name="task_suggest"),
    url(r'^page1/', DisplayPage1View.as_view(), name="link_page1"),
    url(r'^page2/', DisplayPage2View.as_view(), name="link_page2"),
)
