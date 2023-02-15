from django.shortcuts import render
from django.http import HttpResponse
import xml.etree.ElementTree as ET
from . import tools
# Create your views here.
def LDOXMLCreator(request, id):
    root = tools.recParseXML(ET.parse("./LDO/XMLTEMPLATE/ClinicalDocument.xml").getroot(), "./LDO/XMLTEMPLATE/ClinicalDocument/")
    return HttpResponse(ET.tostring(root), content_type="application/xml")
