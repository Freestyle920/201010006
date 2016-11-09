
# coding: utf-8

# In[2]:

import os
KEY="6f525355466d696e39317666736479"
TYPE='xml'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX='1'
END_INDEX='10'
LINE_NUM='2'


# In[3]:

url='http://openapi.seoul.go.kr:8088/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=START_INDEX
url+='/'
url+=END_INDEX
url+='/'
url+=LINE_NUM


# In[4]:

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)
print params[31:]


# In[5]:

import urlparse
_url='http://openAPI.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)


# In[6]:

print url


# In[7]:

import requests
data=requests.get(url).text
print data


# In[8]:

type(data)


# In[9]:

import re
p=re.compile('<STATION_NM>(.+?)</STATION_NM>')
res=p.findall(data)
for item in res:
    print item


# In[10]:

import xml.etree.ElementTree as ET
tree=ET.fromstring(data.encode('utf-8'))


# In[ ]:



