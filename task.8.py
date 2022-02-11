import json
from task1 import scrap_top_list
import os
import requests
from bs4 import BeautifulSoup
top_movies=scrap_top_list()
def scrap_movie_details(movie_url):
    # print(movie_url)
    movie_id=""
    for id in movie_url[33:]:
        if "/" not in id:
            movie_id+=id
        else:
            break
    file_name=movie_id+".json"

    text=None
    if os.path.exists("/home/parveen/Desktop/web scraping/"+file_name):
        # print("hello")
        f=open("/home/parveen/Desktop/web scraping/"+file_name)
        text=f.read()
        return(text)    
    if text is None:
        # print("sorry")
        page=requests.get(movie_url)
        soup=BeautifulSoup(page.text,"html.parser")

        main_div=soup.find("score-board",class_="scoreboard").h1.get_text()
        movie_detail=soup.find("ul",class_="content-meta info")


        k=movie_detail.find_all("li",class_="meta-row clearfix")
        language=k[1].find("div",class_="meta-value").text
        director=k[2].find("div",class_="meta-value").get_text().strip()
        release_date=k[5].find("div",class_="meta-value").get_text().strip()
        runtime=k[6].find("div",class_="meta-value").get_text().strip()
        genre=k[0].find("div",class_="meta-value").get_text().split()

        
        top_movie_details=[]
        details={"movie_name":"","language":"","genre":"","director":"","release_date":"","runtime":""}
        details["movie_name"]=main_div
        details["language"]=language
        details["genre"]=genre
        details["director"]=director
        details["runtime"]=runtime
        details["release_date"]=release_date
        top_movie_details.append(details)
        file1=open("/home/parveen/Desktop/web scraping/"+file_name,"w")
        json.dump(details,file1,indent=4)
        # file1.write(raw)
        
    return(top_movie_details)
url1=top_movies[0]["url"]
movie_detail=scrap_movie_details(url1)
print(movie_detail)

