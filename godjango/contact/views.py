from django.shortcuts import *
from django.template import RequestContext

from django.forms.formsets import formset_factory

from .forms import FeedbackForm, SuggestionForm, QuestionForm

def contact(request):
    if request.method == 'POST':
        print(request.POST['name'])
        print(request.POST['message'])
        message = 'Thank you for your feedback'
        return render_to_response('contact.html', {'success': message}, 
                                  context_instance=RequestContext(request))
    else:
        return render_to_response('contact.html', {}, 
                                  context_instance=RequestContext(request))

def contactbf(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if (form.is_valid()):
            print(request.POST['name'])
            print(request.POST['message'])
            message = 'Thank you for your feedback'
        else:
            message = 'sorry, something went wrong'        
        return render_to_response('contactbf.html', {'success': message}, 
                                  context_instance=RequestContext(request))
    else:
        return render_to_response('contactbf.html', {'form':FeedbackForm()}, 
                                  context_instance=RequestContext(request))


def suggestion(request):
    if request.method == "POST":

        form = SuggestionForm(request.POST)

        if (form.is_valid()):
            try:
                print(request.POST['title'])
                return redirect('/')
            except:
                pass
    else:
        form = SuggestionForm()
        
    return render_to_response('suggestion.html',
                {'form': form},
                context_instance=RequestContext(request))
                
                
def interview(request):
    QuestionFormSet = formset_factory(QuestionForm, extra=5)
    if request.method == "POST":
        formset = QuestionFormSet(request.POST)

        if(formset.is_valid()):
            message = "Thank you"
            for form in formset:
                print form
                form.save()
        else:
            message = "Something went wrong"

        return render_to_response('interview.html',
                {'message': message},
                context_instance=RequestContext(request))
    else:
        return render_to_response('interview.html',
                {'formset': QuestionFormSet()},
                context_instance=RequestContext(request))
