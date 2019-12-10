#!/home/mnyman/anaconda3/bin/python3.7

# Get first listpage as raw HTML from remote. Save.

from requests import get

def dl_initial_page(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

if __name__ == "__main__":
    # execute only if run as a script
    url = 'http://indianislamicmanuscript.com/En/booklibrarylist.aspx?lid=c7WaqaYw0rs='
    file = 'dload/1.html'
    dl_initial_page(url, file)
