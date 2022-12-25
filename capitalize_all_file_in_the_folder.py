import os
import sys
if len(sys.argv)!=2:
    print("Wrong usage,please enter a folder name")
    sys.exit(1)


files = []

with os.scandir(sys.argv[1]) as entries:
    for entry in entries:
        if entry.name != sys.argv[0] and entry.is_file():
            files.append(entry.name)

new_files_names = []
for each in files:
    tmp = each.capitalize()
    os.rename(each,tmp)

