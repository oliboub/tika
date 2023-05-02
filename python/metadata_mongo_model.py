#!/usr/bin/env python
# coding: utf-8

# ## tika_metadatas mongo_model

# In[1]:


import os
from mongoengine import *
from datetime import datetime


# In[2]:


import global_variables as g
g.init()


# In[ ]:


class files(Document):
#    id = SequenceField(primary_key=True)
    fileid = IntField(required=True, unique=True)
    filename = StringField(required=True)
    filedirectory=StringField(required=True)
    category=StringField()


# In[ ]:


class metadata(Document):
    metadataid=SequenceField()
    metadata = StringField(required=True)
    value = StringField(required=True)


# In[ ]:


class links:
    linkid = SequenceField()
    fileid=IntField(required=True)
    metadataid = IntField(required=True)


# In[ ]:


#if g.DEBUG_OL >= 1:
print(os.getcwd(),__name__,'imported')

