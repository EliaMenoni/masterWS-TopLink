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
    def __init__(self, name:str, json_data, value:str = ""):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = value

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
        elif "value" in data:
            self._TEXT = ""
            self.value = data.get("value")
        elif "code" in data:
            self._TEXT = ""
            self.code = data.get("code")

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

class ORGANIZATIONPART():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.id = ID("id", json_data)

class SERVICEPROVIDER():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.id = ID("id", json_data)
        self.name = DATA("name", json_data)
        self.asOrganizationPartOf = ORGANIZATIONPART("asOrganizationPartOf", json_data)
        self.telecom = [TELECOM("telecom", json_data, i) for i, _ in enumerate(json_data.get("telecom"))]
class HEALTHCAREFACILITY():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.id = ID("id", json_data)
        self.location = LOCATION("location", json_data)
        self.serviceProviderOrganization = SERVICEPROVIDER("serviceProviderOrganization", json_data)

class LOCATION():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.addr = DATA("addr", json_data) if json_data.get("addr") is not None else None
        self.censusTract = DATA("censusTract", json_data) if json_data.get("censusTract") is not None else None
        self.name = DATA("name", json_data) if json_data.get("name") is not None else None

        self.healthCareFacility = HEALTHCAREFACILITY("healthCareFacility", json_data) if json_data.get("healthCareFacility") is not None else None

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

        # For Patient
        self.patient = PATIENT("patient", json_data)

class REPRESENTED():
    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""
        print(json_data)
        self.id = ID("id", json_data) if json_data.get("id") is not None else None
        self.name = NAME("name", json_data) if json_data.get("name") is not None else None
        self.telecom = [TELECOM("telecom", json_data, i) for i, _ in enumerate(json_data.get("telecom"))] if json_data.get("telecom") is not None else None
        self.time = DATA("time", json_data) if json_data.get("time") is not None else None
        self.assignedAuthor = ASSIGNED("assignedAuthor", json_data) if json_data.get("assignedAuthor") is not None else None

class ASSIGNED():
    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        # For AUTHOR
        self.classCode = json_data.get("classCode")
        self.id = ID("id", json_data) if json_data.get("id") is not None else None
        self.assignedPerson = ASSIGNED("assignedPerson", json_data) if json_data.get("assignedPerson") is not None else None
        self.telecom = [TELECOM("telecom", json_data, i) for i, _ in enumerate(json_data.get("telecom"))] if json_data.get("telecom") is not None else None
        self.name = NAME("name", json_data) if json_data.get("name") is not None else None
        self.assignedAuthor = REPRESENTED("assignedAuthor", json_data) if json_data.get("assignedAuthor") is not None else None
        self.representedCustodianOrganization = REPRESENTED("representedCustodianOrganization", json_data) if json_data.get("representedCustodianOrganization") is not None else None


class AUTHOR():
    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.time = DATA("time", json_data)
        self.assignedAuthor = ASSIGNED("assignedAuthor", json_data)

class CUSTODIAN():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.assignedCustodian = ASSIGNED("assignedCustodian", json_data)
class TARGET():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.patientRole = ROLE("patientRole", json_data)

class AUTHENTICATOR():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.time = DATA("time", json_data)
        self.signatureCode = DATA("signatureCode", json_data)
        self.assignedEntity = ASSIGNED("assignedEntity", json_data)
        self.representedOrganization = REPRESENTED("representedOrganization", json_data)

class TIME():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        if json_data is None:
            self.low = DATA("low", {"low": {"value": "null"}})
            self.high = DATA("high", {"high": {"value": "null"}})
        else:
            self.low = DATA("low", json_data) if json_data.get("low") is not None else DATA("low", {"low": {"value": "null"}})
            self.high = DATA("high", json_data) if json_data.get("high") is not None else DATA("high", {"high": {"value": "null"}})

class RESPONSIBLE():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.assignedEntity = ASSIGNED("assignedEntity", json_data) if json_data.get("assignedEntity") is not None else None
class ENCOUNTER():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.id = ID("id", json_data)
        self.effectiveTime = TIME("effectiveTime", json_data)
        self.responsibleParty = RESPONSIBLE("responsibleParty", json_data)
        self.location = LOCATION("location", json_data)
class COMPONENTOF():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.encompassingEncounter = ENCOUNTER("encompassingEncounter", json_data)

class LDO_HEADER():
    def __init__(self, json_data):
        # print(json_data.get("realmCode"))
        self._NAME = "HEADER"
        self._TEXT = ""

        self._10setId = ID("setId", json_data)
        self._11realmCode = CODE("realmCode", json_data)
        self._12typeId = ID("typeId", json_data)
        self._13templateId = ID("templateId", json_data)
        self._14id = ID("id", json_data)
        self._15code = CODE("code", json_data)
        self._16title = DATA("title", json_data)
        self._17effectiveTime = DATA("effectiveTime", json_data)
        self._18confidentialityCode = CODE("confidentialityCode", json_data)
        self._19languageCode = CODE("languageCode", json_data)
        self._20versionNumber = DATA("versionNumber", json_data)
        self._21relatedDocument = DOCUMENT("relatedDocument", json_data)
        self._22recordTarget = TARGET("recordTarget", json_data)
        self._23author = AUTHOR("author", json_data)
        self._24custodian = CUSTODIAN("custodian", json_data)
        self._25legalAuthenticator = AUTHENTICATOR("legalAuthenticator", json_data)
        self._26componentOf = COMPONENTOF("componentOf", json_data)

    def to_XML(self):
        return tools.object_to_xml(self)