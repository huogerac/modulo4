from django.views.generic import TemplateView
from djajax.forms import ContactForm

class DisplayPage1View(TemplateView):
    template_name = "page1.html"

    def get_context_data(self, **kwargs):
        context = super(DisplayPage1View, self).get_context_data(**kwargs)
        context['page'] = 'Page1'
        return context
    
    
class DisplayPage2View(TemplateView):
    template_name = "page2.html"

    def get_context_data(self, **kwargs):
        context = super(DisplayPage2View, self).get_context_data(**kwargs)
        context['page'] = 'Page2'
        context['form'] = ContactForm()
        return context