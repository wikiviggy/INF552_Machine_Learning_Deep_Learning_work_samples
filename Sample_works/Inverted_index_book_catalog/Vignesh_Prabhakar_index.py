# -*- coding: utf-8 -*-
"""DM_HW_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11DswRaytAJqpX6VjpkCMW4jVGZG3ON5w
"""

from lxml import etree
import re
import sys

fd = open(sys.argv[1])

tree = etree.parse(fd)
punct = '!"$%&()*,./:;<=>?@[\]^_`{|}~'
kwd_desc_split={}
for element in tree.xpath("//book"):
  attr1 =element.attrib['id']
  kwds_desc= element.find('description').text
  kwds_desc = re.sub('['+punct+']', '', kwds_desc)
  kwd_desc_split[attr1]=(kwds_desc.split())
  #author=element.find('author').text

kwd_auth_split={}
for element in tree.xpath("//book"):
  attr1 =element.attrib['id']
  kwds_auth= element.find('author').text
  kwds_auth = re.sub('['+punct+']', '', kwds_auth)
  kwd_auth_split[attr1]=kwds_auth.split()  

kwd_title_split={}
for element in tree.xpath("//book"):
  attr1 =element.attrib['id']
  kwds_title= element.find('title').text
  kwds_title = re.sub('['+punct+']', '', kwds_title)
  kwd_title_split[attr1]=kwds_title.split()  
  
kwd_genre_split={}
for element in tree.xpath("//book"):
  attr1 =element.attrib['id']
  kwds_genre= element.find('genre').text
  kwds_genre = re.sub('['+punct+']', '', kwds_genre)
  kwd_genre_split[attr1]=kwds_genre.split()  
  

kwd_desc_split['bk110'][1] = '.NET'


xml = '<?xml version="1.0" encoding="UTF-8" ?>\n<invindex>\n' 

for i in kwd_title_split.keys(): 
  for j in range(0,len(kwd_title_split[i])):
   
          xml=xml + '<keyword content ="'+kwd_title_split[i][j]+'">\n<book id ="'+i+'">\n<title>'+(" ".join(kwd_title_split[i]))+'</title>\n</book>\n</keyword>\n'

for i in kwd_auth_split.keys(): 
  for j in range(0,len(kwd_auth_split[i])):
   
          xml=xml + '<keyword content ="'+kwd_auth_split[i][j]+'">\n<book id ="'+i+'">\n<author>'+(" ".join(kwd_auth_split[i]))+'</author>\n</book>\n</keyword>\n'

for i in kwd_genre_split.keys(): 
  for j in range(0,len(kwd_genre_split[i])):
   
          xml=xml + '<keyword content ="'+kwd_genre_split[i][j]+'">\n<book id ="'+i+'">\n<genre>'+(" ".join(kwd_genre_split[i]))+'</genre>\n</book>\n</keyword>\n'

for i in kwd_desc_split.keys(): 
  for j in range(0,len(kwd_desc_split[i])):
   
          xml=xml + '<keyword content ="'+kwd_desc_split[i][j]+'">\n<book id ="'+i+'">\n<description>'+(" ".join(kwd_desc_split[i]))+'</description>\n</book>\n</keyword>\n'

xml=xml+'</invindex>\n'

file = open(sys.argv[2], "w")
file.write("%s" % xml)
file.close()
