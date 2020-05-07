#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd
table = pd.read_csv("C:/Users\Vikas\Downloads\data.csv")
table.head()


# In[84]:


# changig datatype for person_id
table['Person Id']= table['Person Id'].astype(str)


# In[85]:


def json_converter(data):
    dict = {
        "person_id": data['Person Id'],                     
        "datetime": data['Floor Access DateTime'],
        "floor_level": data['Floor Level'],
        "building":data['Building']
       }
    return dict


# In[86]:


dict={}  
dict=table.apply(lambda x: json_converter(x),axis= 1)


# In[90]:


dict[0:10]


# In[91]:


dict[1]


# In[ ]:




