#!/home/mnyman/miniconda3/envs/chains/bin/python

import time
from requests import get

def runProcess():

    # ---------- read collection of hrefs to list ----------
    hrefs = "pages.txt"
    var_hrefs = open(hrefs, "r")
    coll = var_hrefs.readlines()
    var_hrefs.close()

    # ---------- write collection of hrefs to list ----------
    for i, href in enumerate(coll):
        # name target file
        count = 35 - i 
        target_file = "1_raw/%d.html" % count
        file_name = "%d.html" % count

        # get remote content
        href = href.rstrip()
        response = get(href)
        time.sleep(5)

        # write to file
        f = open(target_file, "wb")
        f.write(response.content)
        f.close()
        print("File done!")


if __name__ == "__main__":
    runProcess()

