from bs4 import BeautifulSoup
import json
import requests
import pprint

def movie_cast(movie_url):
    list=[]
    data=requests.get(movie_url)
    soup=BeautifulSoup(data.text,"html.parser")
    main=soup.find_all("div",class_="panel-body content_body")
    sec=main[1].find("div",class_="castSection")
    # print(main)
    all=sec.find_all("div",class_="cast-item")
    # print(all)
    for i in all:
        list.append(i.find("span")["title"])
    with open("1MovieCast.json","w") as file:
        json.dump(list,file,indent=4)

    return list
pprint.pprint(movie_cast("https://www.rottentomatoes.com/m/it_happened_one_night"))





