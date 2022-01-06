import re

info = ["PROCESSOR_LEVEL=","HOMEPATH=","OS=","NUMBER_OF_PROCESSORS=","HOMEDRIVE=","COMPUTERNAME=","PROCESSOR_ARCHITECTURE=","PROCESSOR_IDENTIFIER="]
information_string = ""
for i in info:
    information_string += i +"|"
information_string = information_string[:-1]
FILE = "strings2.txt"

set_information = {}

with open(FILE) as f:
    line = f.readline()
    while line:
        result = re.match(information_string, line)
        if result:
            line = line.replace("\n","")
            if line in set_information:
                set_information[line] += 1
            else:
                set_information[line] = 1
        line = f.readline()

set_information = dict(sorted(set_information.items(), key=lambda item: item[1],reverse=True))

count = 0
for i in set_information:
    splited = i.split("=")
    print("{:<30} {:<50}".format(splited[0],splited[1]))
    count += 1
    if count == len(info):
        break
