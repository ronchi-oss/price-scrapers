import sys
from bs4 import BeautifulSoup

tag_name, prop_name, prop_val = sys.argv[1:]

soup = BeautifulSoup(sys.stdin.read(), features='html.parser')
price = soup.find(tag_name, {prop_name: prop_val}).text.strip()
print(price)
