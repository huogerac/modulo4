from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

class DisplayPage1View(TemplateView):
    template_name = "page1.html"

    def get_context_data(self, **kwargs):
        context = super(DisplayPage1View, self).get_context_data(**kwargs)
        context['page'] = 'Page1'
        return context
    

@login_required(login_url='/admin/login/')
#@user_passes_test(lambda u: u.has_perm('page.can_view'), login_url='/admin/login/')
def display_page2(request):
    template_name = "page2.html"

    #if not request.user.is_authenticated():
    #    return HttpResponseRedirect('/admin/login/?next=%s' % request.path)

    if not request.user.has_perm('page.can_view'):
        return HttpResponse("You can't view this page")
    
    return render_to_response(template_name, {'page': 'Page2'}, 
                                  context_instance=RequestContext(request))
