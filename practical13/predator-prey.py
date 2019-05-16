# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:19:13 2019

@author: 王梓洋
"""
import os
'''
os.system('C:/Users/王梓洋/.spyder-py3/practical13.py')


def xml_to_cps():
    import os
    import xml.dom.minidom
    
    # first, convert xml to cps 
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")
    
    # now comes the painful part. Just copy and paste this ok
    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w")
    cpsTree.writexml(cpsFile)
    cpsFile.close()
    
y=xml_to_cps()
'''

os.system('‪D:\zju intl\ICMB\COPASI 4.24.197\bin\CopasiSE.exe C:/Users/王梓洋/.spyder-py3/predator-prey.cps')

import numpy
import re 
import matplotlib.pyplot as plt
result = open('C:/Users/王梓洋/.spyder-py3/modelResults.csv','r')
result = result.readlines()
name = []
resultdata = []
count = 0
for line in result:
    if count == 0:
        name = re.split(r',+',line)
        count=1                
    else:
        time = re.split(r',+',line)
        del(time[0])        
        resultdata.append(time)
     

results = numpy.array(resultdata)

results = results.astype(numpy.float)

plt.plot(results[:,0],label='Predator')
plt.plot(results[:,1],label='Prey')
plt.xlabel('time')
plt.ylabel('population size')
plt.title('Time course')
plt.legend()
plt.show()

plt.plot(results[:,0],results[:,1])
plt.xlabel('predator population')
plt.ylabel('Prey population')
plt.title('Limit circle')
plt.show()

#------------question 5------------------#
import xml.dom.minidom
import re
import random
file='D:\zju intl\IBI\github steven\IBI1_2018-19\practical13\predator-prey.xml'
DOMTree = xml.dom.minidom.parse('D:\zju intl\IBI\github steven\IBI1_2018-19\practical13\predator-prey.xml')
collection = DOMTree.documentElement
parameters = collection.getElementsByTagName("parametername")
parameterall = ['k predator breeds', 'k predator dies', 'k prey breeds', 'k prey dies']
for parameter in parameters:
    for k in parameterall:
# use elementtree to find parametername 
# Element.set(key, value) to change elements:k predator breeds, k predator dies, k prey breeds, k prey dies.
# choose value by yourself for the 4 elements.
# ElementTree.write('filename.xml') to write new xml file
# use pyplot to make plot

import numpy
import re 
import matplotlib.pyplot as plt
# result = open new file
result = result.readlines()
name = []
resultdata = []
count = 0
for line in result:
    if count == 0:
        name = re.split(r',+',line)
        count=1                
    else:
        time = re.split(r',+',line)
        del(time[0])        
        resultdata.append(time)
     

results = numpy.array(resultdata)

results = results.astype(numpy.float)

plt.plot(results[:,0],label='Predator (b=0.02, d=0.4)')
plt.plot(results[:,1],label='Prey (b=0.1, d=0.02)')
plt.xlabel('predator population')
plt.ylabel('prey population')
plt.title('limit cycle')
plt.legend()
plt.show()

#------------question 6-----------------#

file='D:\zju intl\IBI\github steven\IBI1_2018-19\practical13\predator-prey.xml'
DOMTree = xml.dom.minidom.parse('D:\zju intl\IBI\github steven\IBI1_2018-19\practical13\predator-prey.xml')
collection = DOMTree.documentElement
genes = collection.getElementsByTagName("parametername")

time = 0
while time <= 99:
    # use elementtree to find parametername 
    # Element.set(key, value) to change elements:k predator breeds, k predator dies, k prey breeds, k prey dies.
    value=[random.randint(0,1) for _ in range(4)]
    #value[0] for predator breeds ; value[1] for predator dies ; value[2] for prey breeds ; value[3] for pre dies
    # ues random.randint to choose a random number for the 4 elements.

    time = time + 1
    
# plot as before for 100 times.