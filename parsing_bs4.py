import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.bom.gov.au/qld/observations/qldall.shtml')
r.raise_for_status()
soup = BeautifulSoup(r.text, 'html.parser')

for i in soup.findAll('a', href=True):
    if '/products' in i['href']:
        output = i['href']
        output = output.replace('/products', 'http://bom.gov.au/fwo').replace('shtml', 'json')
        print("'"+output +"',")