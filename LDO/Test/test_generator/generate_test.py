import os
import json

settings = {
    "value": 0,
    "attribute": 0
}

def insert_sub(root, sub:str, edited = None):
    subs = sub.split("/")
    back = None
    # print(subs[0])
    edit = None
    if ">" in subs[0]:
        edit = subs[0].split("\"")[1]
        subs[0] = "section"

    if isinstance(root, list):
        back = root
        if len(root) == 0:
            root = {}
        else:
            root = root.pop()
            
    if len(subs) == 1 and "_" not in subs[0]:
        # print(subs[0])
        if "@" in subs[0]:
            root[subs[0][1:-1]] = "@attr" + str(settings["attribute"])
            settings["attribute"] = settings["attribute"] + 1
        else:
            root[subs[0][:-1]] = "@value" + str(settings["value"])
            settings["value"] = settings["value"] + 1
    elif subs[0] in root:
        root[subs[0]] = insert_sub(root[subs[0]], "/".join(subs[1:]), edit)
    else:
        if len(subs) == 1 and "_" in subs[0]:
            # print(subs[1])
            # print(root, subs)
            if subs[0][:-2] in root and isinstance(root[subs[0][:-2]], list):
                root[subs[0][:-2]].append({})
            else:
                root[subs[0][:-2]] = []
        else:
            subs[0] = subs[0].removesuffix("\n")
            root[subs[0]] = insert_sub({}, "/".join(subs[1:]), edit)

    if edited is not None:
        # print(edit)
        root["ID"] = edited
    
    if back is not None:
        back.append(root)
        return back
    else:
        return root

def generate_json(component):
    struct_file = open("cargo.json")
    struct:json = json.load(struct_file)
    struct_file.close()
    struct["body"]["component"]["structuredBody"]["component"] = []
    # print(component)
    for block in component:
        # print(block)
        struct["body"]["component"]["structuredBody"]["component"].append(block)
        # print(struct["body"]["component"]["structuredBody"]["component"])
    return struct


for root, dirs, files in os.walk("OK", topdown=False):
    # print(root, dirs, files)
    out = []
    components = {}
    tmp_obj = {}
    # print(f"{root} {dirs} {files}")
    if len(files) == 0:
        break

    src = open(root + "/src.txt")
    data = src.readlines()
    for line in data:
        component_id = line.split("\"")[1]
        component_sub = line.split("/")[1:]
        # print(root, component_id, component_sub)
        if component_id in components:
            components[component_id] = insert_sub(components[component_id], "/".join(component_sub))
        else:
            components[component_id] = insert_sub({}, "/".join(component_sub))

    for component_id in components:
        tmp_obj = {}
        tmp_obj["ID"] = component_id
        tmp_obj["typeCode"] = "COMP"
        tmp_obj["section"] = components[component_id]
        out.append(tmp_obj)
        # print(out)
    json_out = generate_json(out)
    out = open(root + "/test.json", "w")
    out.write(json.dumps(json_out, indent=2))
    out.close()
    # print(components)




