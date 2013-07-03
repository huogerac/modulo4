from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

from djajax.util import run_script

@dajaxice_register
def sayhello(request):
    run_script('param1-value')
    return simplejson.dumps({'message':'Hello World'})