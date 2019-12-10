#!/home/mnyman/anaconda3/bin/python3.7

from bs4 import BeautifulSoup

def readFile():

    tag = '<ul class="ms-list">'
    soup = BeautifulSoup(open("dload/1.html"), "html.parser")
    print(soup.select("ul.ms-list"))


if __name__ == "__main__":
    # execute only if run as a script
    readFile()
