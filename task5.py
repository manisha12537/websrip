# from  task1 import scrap_top_list
# import json
# import requests
# from bs4 import BeautifulSoup
# import pprint

# scrapped=scrap_top_list()
# def get_movie_list_detail(movie):
    
#     i=0
#     years=[]
    
#     while i<len(movie):
#         year=movie[i]["url"]
#         k=year
#         # print(k)
#     #     # i=i+1
#         p=requests.get(k)
#         # print(k)
#         soup=BeautifulSoup(p.text,"html.parser")
        
#         movie_detail=soup.find("ul",class_="content-meta info")      
#         movie_find=movie_detail.find_all("li",class_="meta-row clearfix")
#         # print(movie_find)
#         data={}
#         for k in movie_find:
#         #     print(j)
      
#             data[k.find("div",class_="meta-label subtle").text]=k.find("div",class_="meta-value").text.strip().replace("\n","")
#         years.append(data)
#         i=i+1
#     #     #     pprint.pprint(list)
#         with open("task5.json","w") as f:
#            json.dump(years,f,indent=4)
#         pprint.pprint(years)
# get_movie_list_detail(scrapped)






from  task1 import scrap_top_list
import json
import requests
from bs4 import BeautifulSoup
import pprint

scrapped=scrap_top_list()
def get_movie_list_detail(movie):
    
    i=0
    years=[]
    
    while i<len(movie):
        # print(i)
        # i=i+1
        year=movie[i]["url"]
        k=year
        # print(k)
        # i=i+1
        
        p=requests.get(k)
        # print(p)                                                                                                                                                                                                                  
        soup=BeautifulSoup(p.text,"html.parser")
        
        movie_detail=soup.find("ul",class_="content-meta info")      
        movie_find=movie_detail.find_all("li",class_="meta-row clearfix")
        # print(movie_find)
        data={}
        for k in movie_find:
        #     print(j)
      
            data[k.find("div",class_="meta-label subtle").text.strip().replace(" " ," ").replace("\n"," ")]=k.find("div",class_="meta-value").text.strip().replace(" "," ").replace("\n"," ")
        years.append(data)
        i=i+1
        #     pprint.pprint(list)
        with open("task5.json","w") as f:
           json.dump(years,f,indent=4)
        pprint.pprint(years)
get_movie_list_detail(scrapped)