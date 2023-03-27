from django.db import models
from . import tools
from dict2xml import dict2xml
class Log(models.Model):
    """ LOG """
    ID = models.AutoField(name="ID", primary_key=True)
    time = models.DateTimeField(name="Timestamp", auto_now=True)
    user = models.CharField(name="User", max_length=50)
    input = models.TextField(name="Input", blank=True)
    result = models.TextField(name="Output", blank=True)
    status = models.BooleanField(name="Stato", default=True)
    error_code = models.IntegerField(name="Error Code", default=0)
    error_message = models.TextField(name="Error Message", blank=True)

    def __str__(self):
        if self.status == 'OK':
            return "[" + self.time + "] " + self.user + " - " + self.status
        else:
            return "[" + self.time + "] " + self.user + " - " + self.status + " [" + self.error_code + "]"

class ID():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.assigningAuthorityName = json_data.get("assigningAuthorityName")
        self.assignedAuthorityName = json_data.get("assignedAuthorityName")
        self.extension = json_data.get("extension")
        self.root = json_data.get("root")

class CODE():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.displayName = json_data.get("displayName")
        self.codeSystemName = json_data.get("codeSystemName")
        self.codeSystem = json_data.get("codeSystem")
        self.code = json_data.get("code")

class DATA():
    def __init__(self, name:str, data):
        data = data.get(name)
        self._NAME = name
        self._TEXT = ""

        if not isinstance(data, dict):
            self._TEXT = data
        else:
            self._TEXT = ""
            self.value = data.get("value")

class DOCUMENT():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.id = ID("id", json_data) if json_data.get("id") is not None else None

        self.typeCode = json_data.get("typeCode")
        self.setId = ID("setId", json_data) if json_data.get("setId") is not None else None
        self.versionNumber = DATA("versionNumber", json_data) if json_data.get("versionNumber") is not None else None
        self.parentDocument = DOCUMENT("parentDocument", json_data) if json_data.get("parentDocument") is not None else None

class TELECOM():
    def __init__(self, name:str, json_data, index:int = None):
        json_data = json_data.get(name) if index == None else json_data.get(name)[index]
        self._NAME = name
        self._TEXT = ""

        self.use = json_data.get("use")
        self.value = json_data.get("value")

class NAME():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.family = DATA("family", json_data)
        self.given = DATA("given", json_data)
        self.prefix = DATA("prefix", json_data) if json_data.get("prefix") is not None else None

class LOCATION():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.addr = DATA("addr", json_data)
        self.censusTract = DATA("censusTract", json_data)
class PATIENT():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.name = NAME("name", json_data)
        self.administrativeGenderCode = CODE("administrativeGenderCode", json_data)
        self.birthTime = DATA("birthTime", json_data)
        self.birthPlace = LOCATION("birthPlace", json_data)

class ROLE():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.id = ID("id", json_data)
        self.telecom = [TELECOM("telecom", json_data, i) for i, _ in enumerate(json_data.get("telecom"))]
        self.patient = PATIENT("patient", json_data)
class TARGET():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.patientRole = ROLE("patientRole", json_data)
class LDO_HEADER():
    def __init__(self, json_data):
        # print(json_data.get("realmCode"))
        self._NAME = "HEADER"
        self._TEXT = ""

        # self.componentOf = None
        # self.legalAuthenticator = None
        # self.custodian = None
        # self.author = None
        self.recordTarget = TARGET("recordTarget", json_data)
        # self.relatedDocument = DOCUMENT("relatedDocument", json_data)
        # self.versionNumber = DATA("versionNumber", json_data)
        # self.languageCode = CODE("languageCode", json_data)
        # self.confidentialityCode = CODE("confidentialityCode", json_data)
        # self.effectiveTime = DATA("effectiveTime", json_data)
        # self.title = DATA("title", json_data)
        # self.code = CODE("code", json_data)
        # self.id = ID("id", json_data)
        # self.templateId = ID("templateId", json_data)
        # self.typeId = ID("typeId", json_data)
        # self.realmCode = CODE("realmCode", json_data)
        # self.setId = ID("setId", json_data)

    def to_XML(self):
        return tools.object_to_xml(self)