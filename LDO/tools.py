import pathlib
import xml.etree.ElementTree as ET
import re

def checkRequire(fileName : str):
    comp = fileName.split('_')
    comp[0] = comp[0].split(".")
    comp[1] = comp[1].split(".")
    try:
    	return comp[0][1] != 'O', comp[1][0]
    except:
    	return True, comp[1][0]

def recParseXML(XMLRoot : ET.Element, FolderRoot : str) -> ET.Element:
    print(FolderRoot)
    currentFiles = pathlib.Path(FolderRoot)
    folders = [f.name for f in currentFiles.iterdir() if f.is_dir()]
    files = [f.name[0:-4] for f in currentFiles.iterdir() if f.is_file()]
    for item in currentFiles.iterdir():
        if item.name[0] == '.':
            continue
        index = int(re.split(r"\.|\_", item.name)[0])
        print(item.name)
        if item.is_file() and item.name[0:-4] in files:
            files.remove(item.name[0:-4])
            if item.name[0:-4] in folders:
                folders.remove(item.name[0:-4])
                XMLRoot.insert(index, recParseXML(ET.parse(item).getroot(), FolderRoot + item.name[0:-4] + "/"))
            else:
                XMLRoot.insert(index, ET.parse(item).getroot())

        if item.is_dir() and item.name in folders:
            folders.remove(item.name)
            if item.name in files:
                files.remove(item.name)
                XMLRoot.insert(index, recParseXML(ET.parse(FolderRoot + item.name + ".xml").getroot(), FolderRoot + item.name + "/"))
            else:
                name = item.name.split("_")[1]
                XMLRoot.insert(index, recParseXML(ET.Element(name), FolderRoot + item.name + "/"))

    return XMLRoot