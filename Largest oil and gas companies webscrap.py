#!/usr/bin/env python
# coding: utf-8

# In[113]:


from bs4 import BeautifulSoup
import requests
import pandas as pd 


# In[124]:


URL = 'https://en.wikipedia.org/wiki/List_of_largest_oil_and_gas_companies_by_revenue'
page = requests.get(URL)
soup1= BeautifulSoup(page.text, "html")
print(soup1)


# In[125]:


#table = soup1.find('table')
#print(table)


# In[128]:


soup1.find_all('table')[0]


# In[129]:


soup1.find('table', class_ = "wikitable sortable")


# In[130]:


table = soup1.find_all('table')[0]
print(table)


# In[131]:


world_titles = table.find_all('th')


# In[132]:


world_titles


# In[133]:


world_table_titles = [title.text.strip() for title in world_titles]


print(world_table_titles)
#df


# In[134]:


df = pd.DataFrame(columns = world_table_titles)
df


# In[135]:


column_data = table.find_all('tr')


# In[146]:


for row in column_data[1:]: 
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    #print(individual_row_data)
    
    #
    lenght = len(df)
    df.loc[lenght] = individual_row_data

    


# In[147]:


df


# In[148]:


df.to_csv(r'C:\Users\juani\OneDrive\Desktop\PYTHON\myexercises\webscrap\ranking_oil_companies.csv')


# In[73]:





# In[ ]:




