#pip install beautifulsoup4 pandas selenium
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver=webdriver.Chrome("")     #install the webdriver for chrome version and keep the downloaded part here
driver.get("")
results=[]
other_results=[]
content=driver.page_source
soup=BeautifulSoup(content)

for elements in soup.findall(""): #go to page location click on inspect on what you want to upload
    name=elements.find("")
    if name not in results:
        results.append(name.text)


df=pd.dataframe({'names':results})
df.to_csv('names.csv',index=False,encoding='utf-8')     
    

#if two contents are required
for a in soup.findall(""): #go to page location click on inspect on what you want to upload
    name=a.find("")
    if name not in results:
        results.append(name.text)


for b in soup.findall(""): #go to page location click on inspect on what you want to upload
    date=b.find("")
    if date not in results:
        other_results.append(name.text)

f=pd.dataframe({'names':results,'date':other_results})
df.to_csv('names.csv',index=False,encoding='utf-8')             