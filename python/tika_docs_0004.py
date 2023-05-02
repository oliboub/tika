#!/usr/bin/env python
# coding: utf-8

# # test tika to convert documents in directory: documents
# - First prepare docs.txt by doing in linux:
#     > ls Engineering > docs.txt
#     > Category = Directory name

# #### Note: convert pdf to tiff with ghostscript
# **gs -q -dNOPAUSE -sDEVICE=tiffg4 -sOutputFile=test10.tiff test10.pdf -c quit**
# 
# #### Note: gimp save tiff files without layers
# ![gimp_tiff.jpg](attachment:206969f7-0e54-4896-b76e-79f7d94af981.jpg)

# In[1]:


import os
import socket
import re
from tika import parser
from metadata_mongo_model import *
from datetime import datetime


# In[2]:


import global_variables as g
g.init()


# In[3]:


connect('tika_metadata')

now = datetime.now()
 
#print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#print("date and time =", dt_string)

host=socket.gethostname()
fqdn = socket.getfqdn()
if g.DEBUG_OL >= 1:
    print(host,fqdn)
category="Engineering"

dirlist = os.listdir("../"+category)

if g.DEBUG_OL >= 1:
    print(dirlist)


# In[4]:


metadata_ref = open("../metadata_ref.txt","r").read()
if g.DEBUG_OL >= 1:
    print(metadata_ref)
metadata_lst = metadata_ref.split('\n')
if g.DEBUG_OL >= 1:
    print(metadata_lst,metadata_lst[0])


# In[24]:


def load_db_files(category,name,fulldir,host,fqdn,inode):
    if g.DEBUG_OL >= 2:
        print('function: load_db_files(',category,',',name,',',fulldir,',',host,',',fqdn,',',inode,')')
    createdfile=files.objects(inode=inode,server=host,fqdn=fqdn,filename=name,filedirectory=fulldir,category=category).first()

    if createdfile != None:
        message="<-- File: "+str(createdfile.server)+":"+str(createdfile.filedirectory)+"/"+str(createdfile.filename)+"\t with id: "+str(createdfile.id)+"\t already exits !"
        return message, str(createdfile.fileid)

    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    item=files()
    item.server=host
    item.fqdn=fqdn
    item.filename = name
    item.filedirectory = fulldir
    item.inode = inode
    item.category = category
    item.CreationDate = creationdate
    aaa=item.save()
    
    createdfile=files.objects(inode=inode,server=host,fqdn=fqdn,filename=name,filedirectory=fulldir,category=category).first()
        
    if g.DEBUG_OL >= 2:
        print('--> New file created with fileid=',createdfile.fileid)
    message="--> File: "+str(createdfile.server)+":"+str(createdfile.filedirectory)+'/'+str(createdfile.filename)+"\t with id: "+str(createdfile.id)+"\t is created !"
    return message,str(createdfile.fileid)


# In[25]:


## UNITARY TESTS - comment all lines before to save as python file

#load_db_files("Engineering","test2.jpg","/media/olivier/Donnees/Documents/Formations/tika/Engineering","pcobubuntu","pcobubuntu","113787699" )


# In[26]:


def load_db_metadata(meta,valeur):
    if g.DEBUG_OL >= 2:
        print('function: load_db_metadata(',meta,',',valeur,')')
    createdmetadata=metadata.objects(metadata=meta,value=valeur).first()

    if createdmetadata != None:
        message="<-- Metadata: \""+meta+"\" with value: \""+valeur+"\"\t with id:"+str(createdmetadata.id)+"\t already exists"
        return message,str(createdmetadata.metadataid)
    
    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S")
    item=metadata()
    item.metadata=meta
    item.value=valeur
    item.CreationDate = creationdate
    item.save()
    createdmetadata=metadata.objects(metadata=meta,value=valeur).first()
    if g.DEBUG_OL >= 2:
        print('--> Metadata',createdmetadata.metadata,'created with value',createdmetadata.value)
    message='--> Metadata \"'+str(createdmetadata.metadata)+'\" created with value: \"'+str(createdmetadata.value)+"\"\t with id: "+str(createdmetadata.id)+"\t is created !"
    return message,str(createdmetadata.metadataid)


# In[27]:


## UNITARY TESTS - comment all lines before to save as python file

#load_db_metadata('aircraft','a320')
#load_db_metadata('aircraft','a330')


# In[33]:


def load_db_links(fileid,metaid):
    if g.DEBUG_OL >= 2:
        print('function: load_db_links(',fileid,',',metaid,')')
    
    createdlink=links.objects(fileid=int(fileid),metadataid=int(metaid)).first()
    if createdlink != None:
        message="<-- Link: \""+str(createdlink.fileid)+"\" <--> \""+str(createdlink.metadataid)+"\"\t with id:"+str(createdlink.id)+"\t already exists"
        return message,str(createdlink.linkid)

    now = datetime.now()
    creationdate = now.strftime("%d/%m/%Y %H:%M:%S") 
    item=links()
    item.fileid=int(fileid)
    item.metadataid=int(metaid)
    item.CreationDate = creationdate
    item.save()
        
    createdlink=links.objects(fileid=int(fileid),metadataid=int(metaid)).first()

    message="--> Link: \""+str(createdlink.fileid)+"\" <--> \""+str(createdlink.metadataid)+"\"\t with id:"+str(createdlink.id)+"\t  is created!"
    if g.DEBUG_OL >= 2:
        print(message)
    return message,str(createdlink.linkid)        


# In[34]:


## UNITARY TESTS - comment all lines before to save as python file

#load_db_links("1","1")


# In[49]:


def search_metadata(fileid,line,metadata_lst):
    if g.DEBUG_OL >= 2:
        print('function: search_metadata(',fileid,',',line,',',metadata_lst,')')
    if g.DEBUG_OL >= 2:
        print(line)
    for i in range(len(line)):
        line[i] = line[i].lower()
        if g.DEBUG_OL >= 2:
            print(line[i])

    for i in metadata_lst:
        checkkey=i.split(",")
        key=checkkey[0]
        indice=int(checkkey[1])
        if g.DEBUG_OL >= 2:
            print(key, indice)
        value = [s for s in line if key.lower() in s]
        if g.DEBUG_OL >= 2:
            print("value:",value, "value[0]",value[0])
        if value:
            if indice == 1:
                work = value[0].replace('part number','part')
                work = work.replace('part no','part')
                work = work.replace('\xa0','').replace('\t', ' ').replace(' : ',' ').replace(': ',' ').replace(':',' ').replace(', ',' ').replace(',',' ').split(' ')
                if g.DEBUG_OL >= 2:
                    print("work:",work)
                aa=work.index(key.lower())
                value=work[int(aa)+1].lstrip(" ").rstrip(" ")
                
            if indice == 0:
                work = value[0].replace('\xa0','').replace('\t', ' ').replace(', ',' ').replace(',',' ').split(':')
                toto=work
                if g.DEBUG_OL >= 2:
                    print(work)
                aa=work.index(key.lower())
                value=work[int(aa)+1].lstrip(" ").rstrip(" ")
                   

#        print(aa)
            if g.DEBUG_OL >= 2:
                print("key:",key,"\tvalue:",value)
            message,metaid=load_db_metadata(key,value)
            if g.DEBUG_OL >= 1:
                print(message)
            if g.DEBUG_OL >= 2:
                print(fileid,metaid)
            message,linkid=load_db_links(fileid,metaid)
            if g.DEBUG_OL >= 1:
                print(message)
#        else:
#            result=''
    return


# In[50]:


## UNITARY TESTS - comment all lines before to save as python file

#search_metadata("29",['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Aircraft: A330', '', 'Part NO: 10011', '', '', ''],['aircraft,1', 'part,1', 'title,0'])
#search_metadata("32",['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Texte de metadata', '', 'Ceci est un test de metadata', '', 'Title\xa0: Document de référence', '', '', '', '', '', 'Aircraft\xa0: A320\tceci est un avion avec des ailes', '', 'Part Number\xa0: JJ888888', ''] , ['aircraft,1', 'part,1', 'title,0'] )


# In[52]:


for i in dirlist:
    xx=[]
    str_match=[]
    if g.DEBUG_OL >= 2:
        print("-----------------------\n",i)
    full_dir=os.path.abspath("../"+category)
    aa="../"+category+'/'+i
    inode=os.stat(aa).st_ino
    if g.DEBUG_OL >= 2:
        print(full_dir,i,inode)
    parsed_file = parser.from_file(aa)
    my_content = parsed_file['content']
    line = my_content.split('\n')
    if g.DEBUG_OL >= 2:
        print(line[0:-1])

    if g.DEBUG_OL >= 2:
        print(category,i,full_dir,host,fqdn,inode)
    message,fileid=load_db_files(category,i,full_dir,host,fqdn,inode)
    if g.DEBUG_OL >= 1:
        print(message)
    result=search_metadata(fileid,line,metadata_lst)


# In[ ]:


if g.DEBUG_OL >= 1:
    print(os.getcwd(),__name__,'imported')


# In[ ]:




