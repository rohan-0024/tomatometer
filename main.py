#print("Hello Everyone...This is one of my project where you can see the rotten tomato score of an movie ")
from bs4 import BeautifulSoup
import requests

source= requests.get('https://www.rottentomatoes.com/').text
soup=BeautifulSoup(source,'lmxl')
print(soup.prettify())