IndexDict={
    '1':'PID',
    '2':'COMMAND',
    '3':'%CPU',
    '4':'TIME',
    '5':'#TH',
    '6':'#WQ',
    '7':'#PORT',
    '8':'MEM',
    '9':'PURG',
    '10':'CMPRS',
    '11':'PGRP',
    '12':'PPID',
    '13':'STATE',
    '14':'BOOSTS'
}
with open('ryy','r') as f:
    FileOutPutList=f.read().split('\n')

IndexList=[]
ResultList=[]

for key in IndexDict:
    IndexList.append(FileOutPutList[0].find(IndexDict[key]))


for j in range(1,(len(FileOutPutList)-1)):
    ResultList_temp=[]
    IndexList.append(len(FileOutPutList[j]))
    IndexList.sort(reverse=False)
    for i in range(len(IndexList)-1):
        ResultList_temp.append(FileOutPutList[j][IndexList[i]:IndexList[i+1]].strip(' '))
    ResultList.append(ResultList_temp)
    IndexList.pop()
print(ResultList)



