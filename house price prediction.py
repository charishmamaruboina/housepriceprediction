#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
houseDf = pd.read_csv(r"Housing.csv")
houseDf.head()


# In[2]:


houseDf.info()


# In[3]:


houseDf.describe()


# In[4]:


houseDf.columns


# In[5]:


sns.pairplot(houseDf)


# In[ ]:




