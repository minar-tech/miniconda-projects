#!/home/mnyman/anaconda3/bin/python3.7

import re

def extract():
    pattern = re.compile('(Book.aspx\?id\=[a-zA-Z0-9]+\=)')

    for i, line in enumerate(open('dload/1.html')):
        for match in re.finditer(pattern, line):
            print('Found on line %s: %s' % (i+1, match.group()))

if __name__ == "__main__":
    extract()
