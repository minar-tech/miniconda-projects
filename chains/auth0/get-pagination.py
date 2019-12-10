#!/home/mnyman/miniconda3/envs/chains/bin/python

import sys

#<ul class="pagination">

from bs4 import BeautifulSoup
import re

def get_section(param):

    # ---------- bs Extract pagination ----------
    fo = "2strip/%s" % param
    f = open(fo)  # <_io.TextIOWrapper name='2strip/1.html' mode='r' encoding='UTF-8'>
    soup = BeautifulSoup(f, features="lxml")  #<html>...</html>
    f.close()
    target = (soup.find_all("ul", class_="pagination"))  # <ul class="pagination">...</ul>

    # ---------- regex Find next page ----------
    #m = re.search(r'(\bselected\b)(["><a-zA-Z\s=/-]*)([1-9]{1,2})(["><a-zA-Z\s=/-]*)([1-9]{1,2})(["><a-zA-Z\s=/-]*)([1-9]{1,2})', str(target))
    #m = re.search(r'(\bselected\b)(\D+)([1-9]{1,2})(\D+)([0-9]{1,2})(\D+)([0-9]{1,2})', str(target))
    m = re.search(r'\bselected\b\D+[1-9]{1,2}\D+[0-9]{1,2}\D+([0-9]{1,2})', str(target))
    print(m.group(1))


if __name__ == "__main__":
    get_section(sys.argv[1])
