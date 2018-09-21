###############################################################################
#Download letter posters from abcjessusloveme.com
#reference:
#How to download a PDF file over HTTPS with Python
#https://stackoverflow.com/a/33488338
#
###############################################################################
import requests
import shutil
import sys

i=0
pairs = []
for x in range(14):
    pair=chr(ord('M')+x)
    pair+=chr(ord('m')+x)
    pairs.append(pair)

for x in pairs:
    filename= x + "Poster.pdf"
    url="https://www.abcjesuslovesme.com/media/documents/"+ filename
    r = requests.get(url, auth=('usrname', 'password'), verify=False,stream=True)
    r.raw.decode_content = True
    with open(filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
