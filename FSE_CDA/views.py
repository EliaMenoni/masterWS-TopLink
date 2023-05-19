from django.http import HttpResponse, HttpResponseBadRequest
import json
from . import tools

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def composeLDO(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
    else:
        return HttpResponseBadRequest("GET request not allowed")

    LDO_XML = tools.compose_LDO(json_data)

    return HttpResponse(LDO_XML.to_XML(), content_type="application/xml")


