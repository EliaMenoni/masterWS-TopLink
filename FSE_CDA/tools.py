from typing import Any, List, Dict
from xml.etree import ElementTree as ET
from . import models
def get_members(obj: object) -> List[str]:
    """ Helper function
        Get class members other than functions and private members.
    """
    members = []
    for attr in dir(obj):
        if not callable(getattr(obj, attr)) and not attr.startswith("__"):
            members.append(attr)
    return members

def to_xml(obj: Any) -> Any:
    """ Convert a class object and its members to XML.

    Each class member is treated as a tag to the current XML-element.
    Each member object is treated as a new sub-element.
    Each 'list' member is treated as a new list tag.
    """

    if isinstance(obj, dict):
        raise Exception("Dictionary type is not supported.")

    root = None
    tags = {}

    subelements = {}  # type: Dict[Any, Any]
    for member in get_members(obj):
        item = getattr(obj, member)
        if(member == "_NAME" or member == "_TEXT"):
            continue
        # member = member.replace('_', '-')

        if member == "xsit":
            member = "xsi:type"

        # if object is None, add empty tag
        if item is not None:
            # Add list sub-elements
            if isinstance(item, (list, set)):
                subelements[member] = []
                for list_object in item:
                    subelements[member].append(to_xml(list_object))
            # Add sub-element
            elif not isinstance(item, (str, list, set, tuple)):
                subelements[member] = to_xml(item)
            # Add element's tag name
            elif isinstance(item, (tuple)):
                tags[item[0]] = item[1]
            else:
                tags[member] = item

    try:
        if obj._NAME:
            root = ET.Element(obj._NAME, tags)
        else:
            raise Exception("Name attribute can't be empty.")
    except (AttributeError, TypeError) as ex:
        print("Attribute value or type is wrong. %s: %s", obj, ex)
        raise

    # Add sub elements if any
    if subelements:
        for name, values in subelements.items():
            if isinstance(values, list):  # if list of elements. Add all sub-elements
                for value in values:
                    root.append(value)
            else: # else add object
                root.append(values)

    try:
        if obj._TEXT:
            root.text = obj._TEXT
    except AttributeError as ex:
        print("Attribute does not exists. %s: %s", obj, ex)
        raise

    return root

def object_to_xml(obj: Any) -> Any:
    """ Convert the given class object to xml document str.
    """
    return ET.tostring(element=to_xml(obj), encoding="UTF-8", xml_declaration=True)

def compose_LDO(json_data):
    ldo = models.LDO(json_data)

    return ldo
