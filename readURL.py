import urllib.request
import re
'''
Created on Jan 28, 2017

@author: rkbergsma
'''

x = urllib.request.urlopen("http://www.techradar.com/news/samsung-is-planning-a-pro-health-and-fitness-wearable")
data = x.read()
data.decode("utf-8")
data = str(data)
#data = "Hello this is a test string asfej e f je33__0393"
results = re.split('\W+', data)
print(results)
