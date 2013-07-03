from django.views.generic import TemplateView

class DisplayPage1View(TemplateView):
    template_name = "page1.html"

    def get_context_data(self, **kwargs):
        context = super(DisplayPage1View, self).get_context_data(**kwargs)
        context['page'] = 'Page1'
        return context