#!/usr/bin/env python
# coding: utf-8

# In[51]:


import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.magicbricks.com/project-south-city-for-rent-in-kolkata-pppfr")
c = r.content

soup = BeautifulSoup(c,"html.parser")


all = soup.find_all("div",{"class":"m-srp-card SRCard"})


# In[52]:


l = []
for item in all:
    d = {}
    d["Price"] = item.find("div",{"class":"m-srp-card__price"}).text.replace("\n","")
    d["BHK"] = item.find("span",{"class":"m-srp-card__title__bhk"}).text.replace("\n","")
    d["Furnishing"] = item.find_all("div",{"class":"m-srp-card__summary__info"})[1].text
    d["Available for"] = item.find_all("div",{"class":"m-srp-card__summary__info"})[2].text
    d["Bathrooms"] = item.find_all("div",{"class":"m-srp-card__summary__info"})[3].text
    l.append(d)
l


# In[53]:


import pandas
df = pandas.DataFrame(l)


# In[54]:


df


# In[50]:


df.to_csv("Output.csv")


# In[ ]:




