import re
import sys
from termcolor import colored

FILE = "strings2.txt"
SIZE = int(sys.argv[2])
PATTERN = ".*"+sys.argv[1]+".*"
print("Searching for pattern: ", PATTERN)

with open(FILE) as f:
    line = f.readline()
    while line:
        result = re.match(PATTERN, line)
        if result:
            a = re.search(r'\b({})\b'.format(sys.argv[1]), line)
            if a != None:
                start = a.start()
                if start > SIZE:
                    print(line[start-SIZE:start].replace("\n",""),end="")
                    print(colored(sys.argv[1], 'red'),end="")
                    print(line[start+len(sys.argv[1]):start+len(sys.argv[1])+SIZE].replace("\n",""))
                else: 
                    print(line[:start].replace("\n",""),end="")
                    print(colored(sys.argv[1], 'red'),end="")
                    print(line[start+len(sys.argv[1]):start+len(sys.argv[1])+SIZE].replace("\n",""))
        line = f.readline()