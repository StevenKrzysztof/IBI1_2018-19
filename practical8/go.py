# -*- coding: utf-8 -*-
"""
Created on Sun May 12 21:10:45 2019

@author: 王梓洋
"""

import xml.dom.minidom
import pandas as pd
import re

filePath='C:/Users/王梓洋/.spyder-py3'
fileName='go_obo.xml'
resName='autophagosome.xlsx'
file='C:/Users/王梓洋/.spyder-py3/go_obo.xml'
res='C:/Users/王梓洋/.spyder-py3/autophagosome.xlsx'

DOMTree = xml.dom.minidom.parse('C:/Users/王梓洋/.spyder-py3/go_obo.xml')
collection = DOMTree.documentElement
genes = collection.getElementsByTagName("term")

def Child(id,resultSet):
    for gene in genes:
        parents = gene.getElementsByTagName('is_a')
        classification = gene.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data == id:
                resultSet.add(classification)
                Child(classification, resultSet)
            
        


       
df = pd.DataFrame(columns=['id','name','definition','childnodes'])

re_compile= re.compile(r'autophagosome')
for gene in genes:
    defstr = gene.getElementsByTagName('defstr')[0].childNodes[0].data
    if re_compile.search(defstr):
        id = gene.getElementsByTagName('id')[0].childNodes[0].data
        name = gene.getElementsByTagName('name')[0].childNodes[0].data
        resultSet = set()
        Child(id, resultSet)
        df = df.append(pd.DataFrame({'id':[id],'name':[name],'definition':[defstr],'childnodes':[len(resultSet)]}))
#id = GO and its sequence number, len() counts for the childnodes
        print(id,len(resultSet))
df.to_excel(res,index=False)