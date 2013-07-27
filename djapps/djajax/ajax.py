from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

from djajax.util import run_script
from djajax.forms import ContactForm

@dajaxice_register
def run_ls_script(request):
    script_response = run_script('param1-value')
    return simplejson.dumps({'response': script_response})

@dajaxice_register
def call_passing_param(request, data):
    print "data----------->%s" % data
    return simplejson.dumps({'response': 'OK'})


@dajaxice_register
def send_message(req, form):
    f = ContactForm(form)
    if f.is_valid():
        print "success"
        return simplejson.dumps({'status':'Success!'})
    
    print "error"
    return simplejson.dumps({'status':f.errors})