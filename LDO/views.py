from django.shortcuts import render
from django.http import HttpResponse
import xml.etree.ElementTree as ET
import asyncio
from . import tools
# Create your views here.
async def composeLDO(request, id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    header, body = await asyncio.gather(tools.recParseXML(None, "./LDO/XMLTEMPLATE/ClinicalDocument/HEADER/"), tools.recParseXML(None, "./LDO/XMLTEMPLATE/ClinicalDocument/BODY/"))
    return HttpResponse(ET.tostring(header), content_type="application/xml")

