from django.views.generic import TemplateView, RedirectView
from django.views.generic.edit import FormView

from .forms import TaskForm
from .models import Task

class DisplayTaskView(TemplateView):
    template_name = "task.html"

    def get_context_data(self, **kwargs):
        context = super(DisplayTaskView, self).get_context_data(**kwargs)
        context['task'] = Task.objects.get(pk=self.kwargs.get('task_id', None))
        return context

class DisplayTaskRedirectView(RedirectView):

    def get(self, request, *args, **kwargs):
        task_id = self.kwargs.get('task_id', None)
        task = Task.objects.get(pk=task_id)
        self.url = '/%s-%s' % (task.id, task.slug)
        return super(DisplayTaskRedirectView, self).get(request, *args, **kwargs)

class SuggestionView(FormView):
    form_class = TaskForm 
    success_url = "/"
    template_name = "suggest.html"

    def form_valid(self, form):
        print(self.request.POST['name'])
        print(self.request.POST['description'])
        return super(SuggestionView, self).form_valid(form)
