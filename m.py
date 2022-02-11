from task1 import scrap_top_list
import os 
import json
import random,time
import requests
import pprint
from bs4 import BeautifulSoup
scraped=scrap_top_list()
url_list=[]
for i in scraped:
    url_list.append(i["url"])
    # print(url_list)
def scrap_movie_details(detail):
    random_sleep=random.randint(1,3)
    list=[]
    for i in detail:
        # print(i)
    
        id=i[33:]
        # print(id)
        if os.path.exists("/home/parveen/Desktop/web scraping/"+id+".json")==True:
            with open("/home/parveen/Desktop/web scraping/"+id+".json","r") as File:
                data=File.read()
                final=json.loads(data)
            list.append(final)
            # print(last)
        else:
            final={}
            time.sleep(random_sleep)
            LinkData=requests.get(i)
            soup=BeautifulSoup(LinkData.text,"html.parser")
            final["name"]=soup.find("h1").text
            main=soup.find("ul",class_="content-meta info")
            all=main.find_all("li",class_="meta-row clearfix")
            for i in all:
                final[" ".join((i.find("div",class_="meta-label subtle").text).split())]=" ".join((i.find("div",class_="meta-value").text).split())
                pprint.pprint(final)
            list.append(final)
            with open("/home/parveen/Desktop/web scraping/"+id+".json","w") as file:
                json.dump(final,file,indent=2)
    return list

scrap_movie_details(url_list)