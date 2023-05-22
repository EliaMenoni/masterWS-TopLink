import os
import json

for root, dirs, files in os.walk(".", topdown=False):
    print(root, dirs, files)
    if "src.txt" not in files:
        break

    out = []
    src = open(root + "/src.txt")
    data = src.readlines()
    for index, line in enumerate(data):
        segment = line.split("/")[-1][0:-1]
        if len(data) > index + 1 and segment not in data[index + 1].split("/"):
            out.append(line)
        elif len(data) == index + 1:
            out.append(line)
        else:
            print("Deleted: ", line)
    src.close()
    src = open(root + "/src.txt", "w")
    src.write("".join(out))




