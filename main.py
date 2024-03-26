#print("Hello Everyone...This is one of my project where you can see the rotten tomato score of an movie ")
from bs4 import BeautifulSoup
import requests
print("Enter a movie name: ")
title= input()
source= requests.get('https://www.rottentomatoes.com/{title}').text
soup=BeautifulSoup(source, 'html.parser')

div= soup.find('div',class_='container rt-layout__body').main
div2=div.find('div')
print(div2.prettify())

# main= div.find('main',id_='main_container',class_='container rt-layout__body')
# print(main)