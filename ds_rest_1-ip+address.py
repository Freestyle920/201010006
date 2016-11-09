
# coding: utf-8

# In[1]:

import requests
url = 'http://freegeoip.net/json/'
geostr=requests.get(url).text
print geostr


# In[2]:

type(geostr)


# In[3]:

import json
geojson=json.loads(geostr)


# In[4]:

type(geojson)


# In[5]:

print geojson['ip']


# In[6]:

geojson.get('ip')


# In[8]:

country=geojson.get('country_code')
print country.decode('utf-8')


# In[9]:

import json
import urllib

def getCountry(ipAddress):
    response = urllib.urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")
print(getCountry("39.118.87.152"))


# In[10]:

import requests
send_url = 'http://freegeoip.net/json/39.118.87.152'
r = requests.get(send_url)
j=json.loads(r.text)
type(j)
print j.keys()


# In[11]:

for k,v in j.iteritems():
    print k,"\t: ",v


# In[ ]:



