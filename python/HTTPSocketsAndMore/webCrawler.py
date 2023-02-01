import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# ignore ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode + ssl.CERT_NONE

# ask for URL
url = input("Enter - ")
# open and read url
html = urllib.request.urlopen(url, context=ctx).read()
# get back a soup object (parse the HTML)
soup = BeautifulSoup(html, "html.parser")
# retrieve all anchor tags
tags = soup("a")
for tag in tags:
    # save all links to a textfile
    with open('links.txt', 'w') as f:
        f.write(tag.get("href", None))
    # print(tag.get("href", None))
