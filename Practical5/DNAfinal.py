DNA="ATGCTTCAGAAAGGTCTTACG"
DNA=list(DNA)
myDict={}
for word in DNA:
    if word in myDict:
        myDict[word]+=1
    else:
        myDict[word]=1
myDict
text=input(myDict)
import matplotlib.pyplot as plt
labels='A', 'T', 'C', 'G'
A=myDict['A']
T=myDict['T']
C=myDict['C']
G=myDict['G']
sizes=[A,T,C,G]
explode=(0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show 