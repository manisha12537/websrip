import json
import pprint
def language_analysis():
  language_list=open("/home/parveen/Desktop/web scraping/task5.json") 
  list=json.load(language_list)
  
  
  # print(list)
  list1=[]
  dict={}
  for i in list:
    if i["Genre:"] not in list1:
      list1.append(i["Genre:"])
      # print(list1)
      dict={}
      list2=[]
      for g in list1:
        i=0
        count=0
        while i<len(list):
          if g==list[i]["Genre:"]:
            count=count+1
          i=i+1
        dict[g]=count
      list2.append(dict)
  pprint.pprint(list2)
  with open ("task11.json","w") as f:
    json.dump(list2,f,indent=4)
language_analysis()