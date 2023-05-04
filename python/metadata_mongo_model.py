#!/usr/bin/env python
# coding: utf-8

# ## tika_metadatas mongo_model

# In[ ]:


import os
from mongoengine import *
from datetime import datetime


# In[ ]:


import global_variables as g
g.init()


# In[ ]:


class files(Document):
#    id = SequenceField(primary_key=True)
#    fileid = IntField(required=True, unique=True)
    fileid = SequenceField()
    server = StringField(required=True)
    fqdn = StringField(required=True)
    filename = StringField(required=True)
    filedirectory = StringField(required=True)
    inode = LongField(required=True)
    md5sum = StringField(required=True)
    category = StringField()
    CreationDate = DateTimeField()


# In[ ]:


class metadata(Document):
    metadataid=SequenceField()
    metadata = StringField(required=True)
    value = StringField(required=True)
    language=StringField()
    CreationDate = DateTimeField()


# In[ ]:


class links(Document):
    linkid = SequenceField()
    fileid=IntField(required=True)
    metadataid = IntField(required=True)
    CreationDate = DateTimeField()


# In[ ]:


#if g.DEBUG_OL >= 1:
print(os.getcwd(),__name__,'imported')

