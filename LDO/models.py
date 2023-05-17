from django.db import models
from . import tools


class Log(models.Model):
    """ The LOG class manage the DB schema and function to track execution logs. """

    #: ID for log entry. Autonumber.
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


class ERROR:
    """ This class is converted to a ERROR block inside the generated XML to make error location easy """

    def __init__(self, type: str, error_text: str):
        self._NAME = "ERROR"
        self._TEXT = error_text

        self.type = type

    @staticmethod
    def generate_class_definition_error(name: str, json_data):
        """ Generate error Code to be inserted in XML. This will make error location easier.
        Error Type is **DEFINITION** error: one or more of the required attributes are missing

        ..  code-block:: xml
            :caption: Error block preview
            :linenos:


            <ERROR type="DEFINITION">
                <!-- Error Text -->
            </ERROR>

        :param name: Parent Block Name
        :param json_data: Json Data refering to Block content
        :return: Object type
        :rtype: ERROR
        """
        print(f"DEFINITION error for block {name}. Replacing with DEFINITION ERROR BLOCK inside XML")
        return ERROR("DEFINITION", f"\nERROR inside block {name} structure. Error generated from:\n{str(json_data)}")

    @staticmethod
    def generate_class_structure_error(name: str, class_name: str):
        """ Generate error Code to be inserted in XML. This will make error location easier.
        Error Type is **STRUCTURE** error: the current block (**name** given by param) is not listed as a possible block configuration

        ..  code-block:: xml
            :caption: Error block preview
            :linenos:


            <ERROR type="STRUCTURE">
                <!-- Error Text -->
            </ERROR>

        :param name: Parent Block Name
        :param class_name: Name of the Class which generate the error
        :return: Object type
        :rtype: ERROR
        """
        print(f"FOUND error for block {name}. Replacing with FOUND ERROR BLOCK inside XML")
        return ERROR("FOUND", f"\nERROR generating block {name}.\nType not found for class {class_name}")


class ID:
    """ This class is converted to XML. Used to structure blocks with the same structure as ID """

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        # SOLO PER TEST
        if type(json_data) is str:
            self._TEXT = json_data
            return

        try:
            if name == "setId":
                self._generate_setid(json_data)
            elif name == "typeId":
                self._generate_typeid(json_data)
            elif name == "templateId":
                self._generate_templateid(json_data)
            elif name == "id":
                self._generate_id(json_data)
            else:
                print(f"Block {name} not found for class {self.__class__.__name__}")
                self.ERROR = ERROR.generate_class_structure_error(name, self.__class__.__name__)
        except:
            print(f"Error generating {name} block. Replacing with ERROR BLOCK")
            self.ERROR = ERROR.generate_class_definition_error(name, json_data)

    def _generate_setid(self, json_data):
        """ Populate Class ID based on setId structure. Used to manage the document versioning

        :param json_data: Json Data referring to Block content

        ..  admonition:: Structure
            :class: toggle danger

            ..  csv-table::
                :align: left
                :class: longtable
                :header: Attribute, Status

                root, REQUIRED
                extension, REQUIRED
                assigningAuthorityName, REQUIRED

        ..  admonition:: Generated XML
            :class: toggle tip

            ..  code-block:: xml

                <setId root="code" extension="code" assigningAuthorityName="name">

        """
        self.root = json_data["root"]
        self.extension = json_data["extension"]
        self.assigningAuthorityName = json_data["assigningAuthorityName"] if "assigningAuthorityName" in json_data else None

    def _generate_typeid(self, json_data):
        """ Populate Class ID based on typeId structure

        :param json_data: Json Data referring to Block content

        ..  admonition:: Structure
            :class: toggle danger

            ..  csv-table::
                :align: left
                :class: longtable
                :header: Attribute, Status

                root, REQUIRED
                extension, REQUIRED

        ..  admonition:: Generated XML
            :class: toggle tip

            ..  code-block:: xml

                <setId root="code" extension="code">

        """
        self.root = json_data["root"]
        self.extension = json_data["extension"]

    def _generate_templateid(self, json_data):
        """ Populate Class ID based on templateId structure

        :param json_data: Json Data referring to Block content

        ..  admonition:: Structure
            :class: toggle danger

            ..  csv-table::
                :align: left
                :class: longtable
                :header: Attribute, Status

                root, REQUIRED
                extension, REQUIRED

        ..  admonition:: Generated XML
            :class: toggle tip

            ..  code-block:: xml

                <setId root="code" extension="code">

        """
        self.root = json_data["root"]
        self.extension = json_data["extension"]

    def _generate_id(self, json_data):
        """ Populate Class ID based on setId structure

        :param json_data: Json Data referring to Block content

        ..  admonition:: Structure
            :class: toggle danger

            ..  csv-table::
                :align: left
                :class: longtable
                :header: Attribute, Status

                root, REQUIRED
                extension, REQUIRED
                assigningAuthorityName, REQUIRED

        ..  admonition:: Generated XML
            :class: toggle tip

            ..  code-block:: xml

                <setId root="code" extension="code" assigningAuthorityName="name">

        """
        self.root = json_data["root"]
        self.extension = json_data["extension"]
        self.assigningAuthorityName = json_data["assigningAuthorityName"]



class CODE:
    """ This class is converted to XML. Used to structure blocks with the same structure as CODE """
    
    def __init__(self, name: str, json_data):
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
                self.xsit = json_data["xsi:type"] if "xsi:type" in json_data else None  # ???
                self.codeSystemName = json_data["codeSystemName"] if "codeSystemName" in json_data else None  # ???
                self.displayName = json_data["displayName"] if "displayName" in json_data else None
            elif name == "realmCode":
                self.code = json_data["code"]
            elif name == "administrationUnitCode":
                self.code = json_data["code"]
            elif name == "routeCode":
                self.code = json_data["code"]
            elif name == "statusCode":
                self.code = json_data["code"]  # COMPLETED
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
                self.ERROR = ERROR.generate_class_structure_error(name, self.__class__.__name__)
        except:
            print(f"Error generating {name} block. Replacing with ERROR BLOCK")
            self.ERROR = ERROR.generate_class_definition_error(name, json_data)

            # DA AGGIUNGERE A TEXT
            # self._02originalText = TEXT("originalText", json_data) if json_data.get("originalText") is not None else None


class DATA:
    """ This class is converted to XML. Used to structure blocks with generic data """
    
    def __init__(self, name: str, json_data):
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
                self.ERROR = ERROR.generate_class_structure_error(name, self.__class__.__name__)
        except:
            print(f"Error generating {name} block. Replacing with ERROR BLOCK")
            self.ERROR = ERROR.generate_class_definition_error(name, json_data)


class DOCUMENT:
    """ This class is converted to XML. Used to structure blocks with the same structure as DOCUMENT """

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        # SOLO PER TEST
        if type(json_data) is str:
            self._TEXT = json_data
            return

        try:
            if name == "relatedDocument":
                self.typeCode = json_data["typeCode"]
                self._01_parentDocument = DOCUMENT("parentDocument", json_data)
            elif name == "parentDocument":
                self.id = ID("id", json_data)
                self.setId = ID("setId", json_data)
                self.versionNumber = DATA("versionNumber", json_data)
            else:
                print(f"Block {name} not found for class {self.__class__.__name__}")
                self.ERROR = ERROR.generate_class_structure_error(name, self.__class__.__name__)
        except:
            print(f"Error generating {name} block. Replacing with ERROR BLOCK")
            self.ERROR = ERROR.generate_class_definition_error(name, json_data)


class TELECOM:
    """ This class is converted to XML. Used to structure blocks with the same structure as TELECOM """

    def __init__(self, name: str, json_data, index: int = None):
        json_data = json_data.get(name) if index is None else json_data.get(name)[index]
        self._NAME = name
        self._TEXT = ""

        # SOLO PER TEST
        if type(json_data) is str:
            self._TEXT = json_data
            return

        try:
            if name == "telecom":
                self.use = json_data["use"]
                self.value = json_data["value"]
            else:
                print(f"Block {name} not found for class {self.__class__.__name__}")
                self.ERROR = ERROR.generate_class_structure_error(name, self.__class__.__name__)
        except:
            print(f"Error generating {name} block. Replacing with ERROR BLOCK")
            self.ERROR = ERROR.generate_class_definition_error(name, json_data)


class NAME:
    """ This class is converted to XML. Used to structure blocks with the same structure as NAME """

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        # SOLO PER TEST
        if type(json_data) is str:
            self._TEXT = json_data
            return

        try:
            if name == "name":
                self.family = DATA("family", json_data)
                self.given = DATA("given", json_data)
                self.prefix = DATA("prefix", json_data) if "prefix" in json_data else None
            else:
                print(f"Block {name} not found for class {self.__class__.__name__}")
                self.ERROR = ERROR.generate_class_structure_error(name, self.__class__.__name__)
        except:
            print(f"Error generating {name} block. Replacing with ERROR BLOCK")
            self.ERROR = ERROR.generate_class_definition_error(name, json_data)


class ORGANIZATION:
    """ This class is converted to XML. Used to structure blocks with the same structure as ORGANIZATION """

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        # SOLO PER TEST
        if type(json_data) is str:
            self._TEXT = json_data
            return

        try:
            if name == "asOrganizationPartOf":
                self.id = ID("id", json_data)
            elif name == "serviceProviderOrganization":
                self.id = ID("id", json_data)
                self.name = DATA("name", json_data)
                self.asOrganizationPartOf = ORGANIZATION("asOrganizationPartOf", json_data)
                self.telecom = [TELECOM("telecom", json_data, i) for i, _ in enumerate(json_data.get("telecom"))]
            else:
                print(f"Block {name} not found for class {self.__class__.__name__}")
                self.ERROR = ERROR.generate_class_structure_error(name, self.__class__.__name__)
        except:
            print(f"Error generating {name} block. Replacing with ERROR BLOCK")
            self.ERROR = ERROR.generate_class_definition_error(name, json_data)


class HEALTHCAREFACILITY:
    """ This class is converted to XML. Used to structure blocks with the same structure as HEALTHCAREFACILITY """

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        # SOLO PER TEST
        if type(json_data) is str:
            self._TEXT = json_data
            return

        try:
            if name == "healthCareFacility":
                self.id = ID("id", json_data)
                self.location = LOCATION("location", json_data)
                self.serviceProviderOrganization = ORGANIZATION("serviceProviderOrganization", json_data)
            else:
                print(f"Block {name} not found for class {self.__class__.__name__}")
                self.ERROR = ERROR.generate_class_structure_error(name, self.__class__.__name__)
        except:
            print(f"Error generating {name} block. Replacing with ERROR BLOCK")
            self.ERROR = ERROR.generate_class_definition_error(name, json_data)


class LOCATION:
    """ This class is converted to XML. Used to structure blocks with the same structure as HEALTHCAREFACILITY """

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        # SOLO PER TEST
        if type(json_data) is str:
            self._TEXT = json_data
            return

        try:
            if name == "location":
                self.name = DATA("name", json_data) if "name" in json_data else None
                self.censusTract = DATA("censusTract", json_data) if "censusTract" in json_data else None
                self.addr = ADDR("addr", json_data) if "addr" in json_data else None
                self.healthCareFacility = HEALTHCAREFACILITY("healthCareFacility", json_data) if "healthCareFacility" in json_data else None
            elif name == "birthPlace":
                self.addr = ADDR("addr", json_data) if "addr" in json_data else None
            else:
                print(f"Block {name} not found for class {self.__class__.__name__}")
                self.ERROR = ERROR.generate_class_structure_error(name, self.__class__.__name__)
        except:
            print(f"Error generating {name} block. Replacing with ERROR BLOCK")
            self.ERROR = ERROR.generate_class_definition_error(name, json_data)


class ADDR:
    """ This class is converted to XML. Used to structure blocks with the same structure as ADDR """

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        # SOLO PER TEST
        if type(json_data) is str:
            self._TEXT = json_data
            return

        try:
            if name == "addr":
                self.__generate_addr(json_data)
            else:
                print(f"Block {name} not found for class {self.__class__.__name__}")
                self.ERROR = ERROR.generate_class_structure_error(name, self.__class__.__name__)
        except:
            print(f"Error generating {name} block. Replacing with ERROR BLOCK")
            self.ERROR = ERROR.generate_class_definition_error(name, json_data)

    def __generate_addr(self, json_data):
        """ Generate an ADDR block
        :param json_data: json forma data refering to ADDR
        :type json_data: dict, required
        """

        self.use = json_data["use"] if "use" in json_data else None
        self.city = DATA("city", json_data)
        self.censusTract = DATA("censusTract", json_data)
        self.state = DATA("state", json_data) if "state" in json_data else None
        self.country = DATA("country", json_data) if "country" in json_data else None
        self.county = DATA("county", json_data) if "county" in json_data else None
        self.postalCode = DATA("postalCode", json_data) if "postalCode" in json_data else None
        self.streetAddressLine = DATA("streetAddressLine", json_data) if "streetAddressLine" in json_data else None


class PATIENT:
    """ This class is converted to XML. Used to structure blocks with the same structure as PATIENT """

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        # SOLO PER TEST
        if type(json_data) is str:
            self._TEXT = json_data
            return

        try:
            if name == "patient":
                self.name = NAME("name", json_data)
                self.administrativeGenderCode = CODE("administrativeGenderCode", json_data)
                self.birthTime = DATA("birthTime", json_data)
                self.birthPlace = LOCATION("birthPlace", json_data)
            else:
                print(f"Block {name} not found for class {self.__class__.__name__}")
                self.ERROR = ERROR.generate_class_structure_error(name, self.__class__.__name__)
        except:
            print(f"Error generating {name} block. Replacing with ERROR BLOCK")
            self.ERROR = ERROR.generate_class_definition_error(name, json_data)


class ROLE:
    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self._01id = ID("id", json_data)
        self._02telecom = [TELECOM("telecom", json_data, i) for i, _ in enumerate(json_data.get("telecom"))] if json_data.get("telecom") is not None else None

        # For Patient
        self._03patient = PATIENT("patient", json_data) if json_data.get("patient") is not None else None

        self._04playingEntity = ENTITY("playingEntity", json_data) if json_data.get("playingEntity") is not None else None


class ENTITY:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self._01name = NAME("name", json_data) if json_data.get("name") is not None else None


class REPRESENTED:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.id = ID("id", json_data) if json_data.get("id") is not None else None
        self.name = NAME("name", json_data) if json_data.get("name") is not None else None
        self.telecom = [TELECOM("telecom", json_data, i) for i, _ in enumerate(json_data.get("telecom"))] if json_data.get("telecom") is not None else None
        self.time = DATA("time", json_data) if json_data.get("time") is not None else None
        self.assignedAuthor = ASSIGNED("assignedAuthor", json_data) if json_data.get("assignedAuthor") is not None else None


class ASSIGNED:
    

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


class AUTHOR:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.time = DATA("time", json_data)
        self.assignedAuthor = ASSIGNED("assignedAuthor", json_data)


class CUSTODIAN:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.assignedCustodian = ASSIGNED("assignedCustodian", json_data)


class TARGET:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.patientRole = ROLE("patientRole", json_data)


class AUTHENTICATOR:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.time = DATA("time", json_data)
        self.signatureCode = CODE("signatureCode", json_data)
        self.assignedEntity = ASSIGNED("assignedEntity", json_data)
        self.representedOrganization = REPRESENTED("representedOrganization", json_data)


class TIME:
    

    def __init__(self, name: str, json_data):
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


class RESPONSIBLE:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.assignedEntity = ASSIGNED("assignedEntity", json_data) if json_data.get("assignedEntity") is not None else None


class ENCOUNTER:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.id = ID("id", json_data)
        self.effectiveTime = TIME("effectiveTime", json_data)
        self.responsibleParty = RESPONSIBLE("responsibleParty", json_data)
        self.location = LOCATION("location", json_data)


class COMPONENTOF:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.encompassingEncounter = ENCOUNTER("encompassingEncounter", json_data)


class STRCUTUREDBODY:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.classCode = json_data.get("classCode")
        self.moodCode = json_data.get("moodCode")
        self.components = [COMPONENT("component", json_data, i) for i, _ in enumerate(json_data.get("component"))] if json_data.get("component") is not None else None


class OBSERVATION:
    

    def __init__(self, name: str, json_data, index: int = None):
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


class ENTRY:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""
        self._01observation = [OBSERVATION("observation", json_data, i) for i, _ in enumerate(json_data.get("observation"))] if json_data.get("observation") is not None else None
        self._02substanceAdministration = [SUBSTANCEADMINISTRATION("substanceAdministration", json_data, i) for i, _ in enumerate(json_data.get("substanceAdministration"))] if json_data.get("substanceAdministration") is not None else None
        self._03supply = [SUPPLY("supply", json_data, i) for i, _ in enumerate(json_data.get("supply"))] if json_data.get("supply") is not None else None


class SUBSTANCEADMINISTRATION:
    

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


class SUPPLY:
    

    def __init__(self, name: str, json_data, index: int = None):
        json_data = json_data.get(name) if index == None else json_data.get(name)[index]
        self._NAME = name
        self._TEXT = ""

        self.moodCode = json_data.get("moodCode")
        self.classCode = json_data.get("classCode")
        self._01quantity = QUANTITY("quantity", json_data) if json_data.get("quantity") is not None else None


class PARTICIPANT:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self._01time = TIME("time", json_data) if json_data.get("time") is not None else None
        self._02role = ROLE("participantRole", json_data) if json_data.get("participantRole") is not None else None


class CONSUMABLE:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self._01manufacturedProduct = MANUFACTUREDPRODUCT("manufacturedProduct", json_data) if json_data.get("manufacturedProduct") is not None else None


class MANUFACTUREDPRODUCT:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self._01manufacturedMaterial = MANUFACTUREDMATERIAL("manufacturedMaterial", json_data) if json_data.get("manufacturedMaterial") is not None else None


class MANUFACTUREDMATERIAL:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self._01code = CODE("code", json_data)


class QUANTITY:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.value = json_data.get("value")
        self.unit = json_data.get("unit")

        self.low = QUANTITY("low", json_data) if json_data.get("low") is not None else None
        self.high = QUANTITY("high", json_data) if json_data.get("high") is not None else None


class SECTION:
    

    def __init__(self, name: str, json_data, index: int = None):
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


class TEXT:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        if isinstance(json_data, str):
            self._TEXT = json_data
        else:
            self._TEXT = ""
            self.list = TEXT_LIST("list", json_data) if json_data.get("list") is not None else None
            self.paragraph = DATA("paragraph", json_data) if json_data.get("paragraph") is not None else None
            self.reference = REFERENCE("reference", json_data) if json_data.get("reference") is not None else None


class REFERENCE:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.value = json_data.get("value")


class TEXT_LIST:
    

    def __init__(self, name: str, json_data):
        json_data = json_data.get(name)
        self._NAME = name
        self._TEXT = ""

        self.item = [ITEM("item", json_data, i) for i, _ in enumerate(json_data)]


class ITEM:
    

    def __init__(self, name: str, json_data, index: int = None):
        json_data = json_data[index].get(name)
        self._NAME = name
        self._TEXT = ""

        self.component = COMPONENT("component", json_data)


class COMPONENT:
    

    def __init__(self, name: str, json_data, index: int = None)q

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


class LDO:
    

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
