import json
import pprint
def language_analysis():
  language_list=open("task5.json") 
  list=json.load(language_list)
  
  
  # # print(list)
  list1=[]
  dict={}
  for i in list:
    if i["Original Language:"] not in list1:
      list1.append(i["Original Language:"])
  # print(list1)
      dict={}
      list2=[]
      for g in list1:
        i=0
        count=0
        while i<len(list):
          if g==list[i]["Original Language:"]:
            count=count+1
          i=i+1
        dict.update({g:count})
      list2.append(dict)
  pprint.pprint(list2)
  with open ("task6.json","w") as f:
    json.dump(list2,f,indent=4)
language_analysis()