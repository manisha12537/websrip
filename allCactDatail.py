import json
import pprint
def movie():
    j=open("allCast.json")
    k=json.load(j)

    # print(k)
    l=open("task5.json")
    m=json.load(l)
    dict={}
    list=[]
    list1=[]
    for i in k: 
        for j in m:
            dict["cast:"]=i
            list.append(dict)
            list.append(j)
    list1.append(list)
    # m.append(dict)
    with open("allCastDaitail.json","w")as file :
        json.dump(list1,file,indent=4)
    # pprint.pprint(list1   )
    return m
movie() 