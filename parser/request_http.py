# -*- coding: UTF-8 -*-
import urllib.request
from xml.dom.minidom import *
import re
start_url = []
try:
  man = urllib.request.urlopen("https://www.cia.gov/sitemap.xml")
except urllib.error.URLError:

    start_url.append('https://www.cia.gov/')
else:
    xml = parse(man)
    name = xml.getElementsByTagName('loc')
    for node in name:
       start_url.append(node.childNodes[0].nodeValue)
       #print (node.childNodes[0].nodeValue)
