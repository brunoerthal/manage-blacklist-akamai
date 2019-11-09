
"""
Created on Tue Nov  8 15:41:59 2019

@author: brunoerthal
"""

import requests
from akamai.edgegrid import EdgeGridAuth

def auth():
    uniqueID = '' #Unique ID - network List - Akamai
    baseurl = ''
    s = requests.Session()
    s.auth = EdgeGridAuth(
    client_token='',
    client_secret='',
    access_token='')
    return s, baseurl, uniqueID
    
