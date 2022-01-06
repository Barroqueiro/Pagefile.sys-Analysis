import re

DISALLOWED_CHARACTERS = "*\n\r\t?;"
PATTERN = "C:\\\\Users\\\\Cruzd|C:\\\\Program Files|C:\\\\Program Files (x86)|C:\\\\Users\\\\Public|C:\\\\ProgramData"
FILE = "strings2.txt"

def clean_list(path_list):
    res = []
    for path in path_list:
        for c in DISALLOWED_CHARACTERS:
            path = path.replace(c,"")
        if path != "":
            res += [path]
    return res

def print_tree(directories, before):
    space =  '    '
    branch = '│   '
    tee =    '├───'
    last =   '└───'
    count = 0
    length = len(directories)
    for d in directories:
        if length == 1:
            print(before+last+d)
        elif count == 0:
            print(before+tee+d)
        elif count < length-1:
            print(before+tee+d)
        else:  
            print(before+last+d)
        if count == length-1:
            print_tree(directories[d], before+space)
        else:
            print_tree(directories[d], before+branch)
        count+=1

set_directories = set()

with open(FILE) as f:
    line = f.readline()
    while line:
        result = re.match(PATTERN, line)
        if result:
            set_directories.add(line)
        line = f.readline()

result = {}

for directory in set_directories:
    splited_directories = directory.split("\\")
    splited_directories = clean_list(splited_directories)
    last_keys = []
    for folder in splited_directories:
        if last_keys == []:
            if folder not in result:
                result[folder] = {}
            last_keys.append(folder)
        else:
            temp = result
            for last in last_keys:
                temp = temp[last]
            if folder not in temp:
                temp[folder] = {}
            last_keys.append(folder)

print_tree(result,"")