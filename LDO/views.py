from django.shortcuts import render
from django.http import HttpResponse
import xml.etree.ElementTree as ET

# Create your views here.
def LDOXMLCreator(request, id):
    root = ET.Element("ClinicalDocument" + str(id))
    root.attrib['schemaLocation'] = "BLA BLA BLA BL"
    ET.SubElement(root, 'PROVA', {'arrt': 'ciaociao'}).text = "domani"
    return HttpResponse(ET.tostring(root), content_type="application/xml")
