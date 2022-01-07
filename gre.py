
import re
import signal
from contextlib import contextmanager

fileToRead = 'strs'


class TimeoutException(Exception): pass

@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

def emailRegex(string):
    regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    emails = re.findall(regex, string)
    return [x[0] for x in emails]

def httpRegex(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]


def writeFile(listData):
    file = open(fileToWrite, 'w+')
    strData = ""
    for item in listData:
        strData = strData+item+'\n'
    file.write(strData)

if __name__ == "__main__":
    emails = []
    env_vars = []
    urls = []
    file = open(fileToRead, 'r')
    listLine = file.readlines()
    counter = 0
    for line in listLine:
        print(counter, line)
        counter += 1

        lines = line.split()
        for line in lines:        
            try:
                with time_limit(1):
                    f_urls = httpRegex(line)
                    urls += f_urls
            except TimeoutException as e:
                print("Timed out!")
                        
            try:
                with time_limit(1):
                    f_emails = emailRegex(line)
                    emails += f_emails
            except TimeoutException as e:
                print("Timed out!")

    fileToWrite = 'emailExtracted.txt'

    if emails:
        uniqEmail = set(emails)
        print(len(uniqEmail), "emails collected!")
        writeFile(uniqEmail)

    fileToWrite = 'urlsExtracted.txt'

    if urls:
        uniq = set(urls)
        print(len(uniq), "urls collected!")
        writeFile(uniq)
