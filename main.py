#print("Hello Everyone...This is one of my project where you can see the rotten tomato score of an movie ")
#from bs4 import BeautifulSoup
import requests

url= 'https://www.rottentomatoes.com'
source = requests.get(url,'lmxl')
print(source.text)
