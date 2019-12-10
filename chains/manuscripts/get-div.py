#!/home/mnyman/anaconda3/bin/python3.7

# <ul class="ms-list">

import requests
from bs4 import BeautifulSoup

def get_section():
    page = requests.get("http://indianislamicmanuscript.com/En/booklibrarylist.aspx?lid=c7WaqaYw0rs=")
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(list(soup.ul.children))
    print (soup.find_all("ul", class_="ms-list"))


if __name__ == "__main__":
    get_section()
