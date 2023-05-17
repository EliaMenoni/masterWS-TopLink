import os
import json

settings = {
    "value": 0,
    "attribute": 0
}

def generate_json(json, path : str):
    component = path.split("/")[0]
    subs = path.split("/")[1:]
    if len(subs) == 0:
        if "@" in component:
            component = component[1:]
        json[component[0:-1]] = "@val"
        return json

    if component in json:
        json[component] = generate_json(json[component], "/".join(subs))
        return json
    else:
        json[component] = generate_json({}, "/".join(subs))
        return json

for root, dirs, files in os.walk(".", topdown=False):
    if "src.txt" not in files:
        break

    out = {}

    src = open(root + "/src.txt")
    data = src.readlines()
    src.close()
    for line in data:
        out = generate_json(out, line)

    struct_file = open("cargo.json")
    struct_json = json.load(struct_file)
    struct_file.close()

    struct_json["header"] = out

    src = open(root + "/test.json", "w")
    src.write(json.dumps(struct_json, indent=2))
    src.close()