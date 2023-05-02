#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from metadata_mongo_model import *
from datetime import datetime
import global_variables as g
g.init()

connect('tika_metadata')

now = datetime.now()
 
#print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#print("date and time =", dt_string)


# In[ ]:


#if g.DEBUG_OL >= 1:
print(os.getcwd(),__name__,'imported')

