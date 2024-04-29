#!/usr/bin/env python
# coding: utf-8

# In[6]:


from bs4 import BeautifulSoup
import requests


# In[7]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


# In[5]:


print(soup)


# In[11]:


soup.find_all('table')


# FOUND OUR TABLE

# In[12]:


soup.find_all('table')[1]


# In[13]:


table = soup.find_all('table')[1]


# In[14]:


print(table)


# PULL DATA FROM THE COLUMNS

# In[24]:


world_titles = table.find_all('th')


# In[25]:


world_titles


# In[26]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[ ]:





# USING PANDA

# In[27]:


import pandas as pd


# In[31]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[41]:


column_data = table.find_all('tr')


# PULL DATA FOR ROWS

# In[47]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)


# In[48]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[49]:


df


# EXPORT TO FOLDER AS A CSV FILE

# In[52]:


df.to_csv(r'C:\Users\KC\OneDrive\web scraping\Companies.csv', index = False)

