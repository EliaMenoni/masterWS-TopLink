from django.shortcuts import render
from django.http import HttpResponse
import xml.etree.ElementTree as ET

# Create your views here.
def LDOXMLCreator(request, id):
    
    return HttpResponse(ET.tostring(root), content_type="application/xml")
