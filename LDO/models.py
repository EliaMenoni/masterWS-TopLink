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

class ERROR():
    def __init__(self, error_text:str):
        self._NAME = "ERROR"
        self._TEXT = error_text

class ID():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        # SOLO PER TEST
        if type(json_data) is str:
            self._TEXT = json_data
            return

        try:
            if name == "setId":
                self.root = json_data["root"]
                self.extension = json_data["extension"]
                self.assigningAuthorityName = json_data["assigningAuthorityName"]
            elif name == "typeId":
                self.root = json_data["root"]
                self.extension = json_data["extension"]
            elif name == "templateId":
                self.root = json_data["root"]
                self.extension = json_data["extension"]
            elif name == "id":
                self.root = json_data["root"]
                self.extension = json_data["extension"]
                self.assigningAuthorityName = json_data["assigningAuthorityName"]
            else:
                print(f"Block {name} not found for class {self.__class__.__name__}")
        except:
            print(f"Error generating {name} block. Replacing with ERROR BLOCK")
            self.ERROR = ERROR(f"\nERROR generating block {name}. Input Data:\n{str(json_data)}")

class CODE():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        # SOLO PER TEST
        if type(json_data) is str:
            self._TEXT = json_data
            return

        try:
            if name == "code":
                self.code = json_data["code"]
                self.codeSystem = json_data["codeSystem"]
                self.codeSystemName = json_data["codeSystemName"]
                self.displayName = json_data["displayName"]
                self._01_translation = CODE("translation", json_data) if "translation" in json_data else None
            elif name == "translation":
                self.code = json_data["code"]
                self.codeSystem = json_data["codeSystem"]
                self.codeSystemName = json_data["codeSystemName"]
                self.displayName = json_data["displayName"]
            elif name == "administrativeGenderCode":
                self.code = json_data["code"]
                self.codeSystem = json_data["codeSystem"]
                self.codeSystemName = json_data["codeSystemName"]
                self.displayName = json_data["displayName"] if "displayName" in json_data else None
            elif name == "value":
                self.code = json_data["code"]
                self.codeSystem = json_data["codeSystem"]
                self.xsit = json_data["xsi:type"] if "xsi:type" in json_data else None #???
                self.codeSystemName = json_data["codeSystemName"] if "codeSystemName" in json_data else None #???
                self.displayName = json_data["displayName"] if "displayName" in json_data else None
            elif name == "realmCode":
                self.code = json_data["code"]
            elif name == "administrationUnitCode":
                self.code = json_data["code"]
            elif name == "routeCode":
                self.code = json_data["code"]
            elif name == "statusCode":
                self.code = json_data["code"] # COMPLETED
            elif name == "languageCode":
                self.code = json_data["code"]
            elif name == "signatureCode":
                self.code = json_data["code"]
            elif name == "confidentialityCode":
                self.code = json_data["code"]
                self.codeSystem = json_data["codeSystem"]
                self.codeSystemName = json_data["codeSystemName"]
            else:
                print(f"Block {name} not found for class {self.__class__.__name__}")
        except:
            print(f"Error generating {name} block. Replacing with ERROR BLOCK")
            self.ERROR = ERROR(f"\nERROR generating block {name}. Input Data:\n{str(json_data)}")

            # self._02originalText = TEXT("originalText", json_data) if json_data.get("originalText") is not None else None

class DATA():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        # SOLO PER TEST
        if type(json_data) is str:
            self._TEXT = json_data
            return

        try:
            if name == "versionNumber":
                self.value = json_data["value"]
            elif name == "effectiveTime":
                self.value = json_data["value"]
            elif name == "birthTime":
                self.value = json_data["value"]
            elif name == "time":
                self.value = json_data["value"]
            elif name == "low" or name == "high":
                self.value = json_data["value"]
            else:
                print(f"Block {name} not found for class {self.__class__.__name__}")
        except:
            print(f"Error generating {name} block. Replacing with ERROR BLOCK")
            self.ERROR = ERROR(f"\nERROR generating block {name}. Input Data:\n{str(json_data)}")
        # if isinstance(data, str):
        #     self._TEXT = data
        # else:
        #     data = data.get(name)
        #     self._TEXT = ""
        #
        #     if not isinstance(data, dict):
        #         self._TEXT = data
        #     elif "value" in data:
        #         self._TEXT = ""
        #         self.value = data.get("value")
        #     elif "code" in data:
        #         self._TEXT = ""
        #         self.code = data.get("code")

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

        # SOLO PER TEST
        # if type(json_data) is str:
        #     self._TEXT = json_data
        #     return
        #
        # try:
        #     if name == "setId":
        #
        #     else:
        #         print(f"Block {name} not found for class {self.__class__.__name__}")
        # except:
        #     print(f"Error generating {name} block. Replacing with ERROR BLOCK")
        #     self.ERROR = ERROR(f"ERROR generating block {name}. Input Data:\n{str(json_data)}")

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

        self.addr = ADDR("addr", json_data) if json_data.get("addr") is not None else None
        self.censusTract = DATA("censusTract", json_data) if json_data.get("censusTract") is not None else None
        self.name = DATA("name", json_data) if json_data.get("name") is not None else None

        self.healthCareFacility = HEALTHCAREFACILITY("healthCareFacility", json_data) if json_data.get("healthCareFacility") is not None else None
class ADDR():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self._01city = DATA("city", json_data) if json_data.get("city") is not None else None
        self._01censusTract = DATA("censusTract", json_data) if json_data.get("censusTract") is not None else None

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

        self._01id = ID("id", json_data)
        self._02telecom = [TELECOM("telecom", json_data, i) for i, _ in enumerate(json_data.get("telecom"))] if json_data.get("telecom") is not None else None

        # For Patient
        self._03patient = PATIENT("patient", json_data) if json_data.get("patient") is not None else None

        self._04playingEntity = ENTITY("playingEntity", json_data)  if json_data.get("playingEntity") is not None else None
class ENTITY():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self._01name = NAME("name", json_data) if json_data.get("name") is not None else None
class REPRESENTED():
    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

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
        self.signatureCode = CODE("signatureCode", json_data)
        self.assignedEntity = ASSIGNED("assignedEntity", json_data)
        self.representedOrganization = REPRESENTED("representedOrganization", json_data)
class TIME():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        if isinstance(json_data, str):
            self._TEXT = json_data
        else:
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
class STRCUTUREDBODY():
    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.classCode = json_data.get("classCode")
        self.moodCode = json_data.get("moodCode")
        self.components = [COMPONENT("component", json_data, i) for i, _ in enumerate(json_data.get("component"))] if json_data.get("component") is not None else None
class OBSERVATION():
    def __init__(self, name:str, json_data, index:int = None):
        json_data = json_data.get(name) if index == None else json_data.get(name)[index]
        self._NAME = name
        self._TEXT = ""

        self.moodCode = json_data.get("moodCode")
        self.classCode = json_data.get("classCode")
        self._01code = CODE("code", json_data)
        self._02statusCode = CODE("statusCode", json_data) if json_data.get("statusCode") is not None else None
        self._04effectiveTime = TIME("effectiveTime", json_data) if json_data.get("effectiveTime") is not None else None
        if json_data.get("value") is not None:
            if "value" in json_data.get("value"):
                self._05value = CODE("value", json_data)
            else:
                self._05value = CODE("value", json_data)
        self._06entryRelationship = ENTRY("entryRelationship", json_data) if json_data.get("entryRelationship") is not None else None
        self._07text = TEXT("text", json_data) if json_data.get("text") is not None else None
class ENTRY():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""
        self._01observation = [OBSERVATION("observation", json_data, i) for i, _ in enumerate(json_data.get("observation"))] if json_data.get("observation") is not None else None
        self._02substanceAdministration = [SUBSTANCEADMINISTRATION("substanceAdministration", json_data, i) for i, _ in enumerate(json_data.get("substanceAdministration"))] if json_data.get("substanceAdministration") is not None else None
        self._03supply = [SUPPLY("supply", json_data, i) for i, _ in enumerate(json_data.get("supply"))] if json_data.get("supply") is not None else None

class SUBSTANCEADMINISTRATION():
    def __init__(self, name: str, json_data, index: int = None):
        json_data = json_data.get(name) if index == None else json_data.get(name)[index]
        self._NAME = name
        self._TEXT = ""

        self.moodCode = json_data.get("moodCode")
        self.classCode = json_data.get("classCode")
        self._01statusCode = CODE("statusCode", json_data) if json_data.get("statusCode") is not None else None
        self._02effectiveTime = TIME("effectiveTime", json_data) if json_data.get("effectiveTime") is not None else None
        self._03routeCode = CODE("routeCode", json_data) if json_data.get("routeCode") is not None else None
        self._04doseQuantity = QUANTITY("doseQuantity", json_data) if json_data.get("doseQuantity") is not None else None
        self._05rateQuantity = QUANTITY("rateQuantity", json_data) if json_data.get("rateQuantity") is not None else None
        self._06administrationUnitCode = CODE("administrationUnitCode", json_data) if json_data.get("administrationUnitCode") is not None else None
        self._07consumable = CONSUMABLE("consumable", json_data) if json_data.get("consumable") is not None else None
        self._08participant = PARTICIPANT("participant", json_data) if json_data.get("participant") is not None else None
        self._09entryRelationship = ENTRY("entryRelationship", json_data) if json_data.get("entryRelationship") is not None else None
class SUPPLY():
    def __init__(self, name:str, json_data, index: int = None):
        json_data = json_data.get(name) if index == None else json_data.get(name)[index]
        self._NAME = name
        self._TEXT = ""

        self.moodCode = json_data.get("moodCode")
        self.classCode = json_data.get("classCode")
        self._01quantity = QUANTITY("quantity", json_data) if json_data.get("quantity") is not None else None
class PARTICIPANT():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self._01time = TIME("time", json_data) if json_data.get("time") is not None else None
        self._02role = ROLE("participantRole", json_data) if json_data.get("participantRole") is not None else None


class CONSUMABLE():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self._01manufacturedProduct = MANUFACTUREDPRODUCT("manufacturedProduct", json_data) if json_data.get("manufacturedProduct") is not None else None
class MANUFACTUREDPRODUCT():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self._01manufacturedMaterial = MANUFACTUREDMATERIAL("manufacturedMaterial", json_data) if json_data.get("manufacturedMaterial") is not None else None
class MANUFACTUREDMATERIAL():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self._01code = CODE("code", json_data)

class QUANTITY():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.value = json_data.get("value")
        self.unit = json_data.get("unit")

        self.low = QUANTITY("low", json_data) if json_data.get("low") is not None else None
        self.high = QUANTITY("high", json_data) if json_data.get("high") is not None else None

class SECTION():
    def __init__(self, name:str, json_data, index:int = None):
        json_data = json_data.get(name) if index is None else json_data.get(name)[index]
        self._NAME = name
        self._TEXT = ""

        self.ID = json_data.get("ID")
        self.classCode = json_data.get("classCode")
        self.moodCode = json_data.get("moodCode")
        self._01code = CODE("code", json_data)
        self._02title = DATA("title", json_data)
        self._03text = TEXT("text", json_data)

        self._04entry = ENTRY("entry", json_data) if json_data.get("entry") is not None else None
        # self._05component = [COMPONENT("component", json_data, i) for i, _ in enumerate(json_data.get("component"))] if json_data.get("component") is not None else None
        if json_data.get("component") is not None:
            if isinstance(json_data.get("component"), list):
                self._05component = [COMPONENT("component", json_data, i) for i, _ in enumerate(json_data.get("component"))] if json_data.get("component") is not None else None
            else:
                self._05component = COMPONENT("component", json_data) if json_data.get("component") is not None else None
class TEXT():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        if isinstance(json_data, str):
            self._TEXT = json_data
        else:
            self._TEXT = ""
            self.list = TEXT_LIST("list", json_data) if json_data.get("list") is not None else None
            self.paragraph = DATA("paragraph", json_data) if json_data.get("paragraph") is not None else None
            self.reference = REFERENCE("reference", json_data) if json_data.get("reference") is not None else None
class REFERENCE():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.value = json_data.get("value")
class TEXT_LIST():
    def __init__(self, name:str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.item = [ITEM("item", json_data, i) for i, _ in enumerate(json_data)]
class ITEM():
    def __init__(self, name:str, json_data, index:int = None):
        json_data = json_data[index].get(name)
        self._NAME = name
        self._TEXT = ""

        self.component = COMPONENT("component", json_data)
class COMPONENT():
    def __init__(self, name:str, json_data, index:int = None):

        json_data = json_data.get(name) if index is None else json_data.get(name)[index]
        self._NAME = name
        self._TEXT = json_data.get("value") if json_data.get("value") is not None else ""

        self.structuredBody = STRCUTUREDBODY("structuredBody", json_data) if json_data.get("structuredBody") is not None else None

        self.ID = json_data.get("ID")
        self.typeCode = json_data.get("typeCode")

        if json_data.get("section") is not None:
            if isinstance(json_data.get("section"), list):
                self.section = [SECTION("section", json_data, i) for i, _ in enumerate(json_data.get("section"))] if json_data.get("section") is not None else None
            else:
                self.section = SECTION("section", json_data) if json_data.get("section") is not None else None
class LDO():
    def __init__(self, JSON):
        self._NAME = "ClinicalDocument"
        self._TEXT = ""

        self.xmlnsns0 = ("xmlns:ns0", "urn:hl7-org:v3")
        self.xmlnsxsi = ("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        self.xsi = ("xsi:schemaLocation", "urn:hl7-org:v3 CDA.xsd")

        json_data = JSON.get("header")
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

        json_data = JSON.get("body")
        self._27component = COMPONENT("component", json_data)

    def to_XML(self):
        return tools.object_to_xml(self)

