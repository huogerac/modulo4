from django.http import HttpResponse

import json


def sms_login(request):
    response_data = {}
    response_data['authenticated'] = 'true'
    return HttpResponse(json.dumps(response_data), mimetype="application/json")