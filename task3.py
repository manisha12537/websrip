import json
import pprint
def group_by_decade():
    declist=[]
    with open("/home/parveen/Desktop/web scraping/task2.json") as jsfile:
        dic=json.load(jsfile)
        # print(dic)
        for i in dic.keys():
            # print(i)
            mod=int(i)%10    # 9097%10=7
            dec=int(i)-mod   # 9097-7=9090
            if dec not in declist:
                declist.append(dec)
    with open("/home/parveen/Desktop/web scraping/task1.json") as jsfile:
        dic=json.load(jsfile)
        # print(dic)
    moviedec={}
    for i in declist:
        moviedec[i]=[]
        range=i+9
        for index in dic:
            if int(index["year"])>=i and int(index["year"])<=range:
                moviedec[i].append(index)
    with open("task3.json","w") as f:
        json.dump(moviedec,f,indent=4)            
    # return(moviedec)
        pprint.pprint(moviedec)
group_by_decade()

