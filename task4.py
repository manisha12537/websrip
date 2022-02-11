import requests
from bs4 import BeautifulSoup
import json
import pprint



def scrap_movie_details():
    # random_sleep=random.randint(1,3)
    movie_url="https://www.rottentomatoes.com/m/it_happened_one_night"
    # time.sleep(random_sleep)p=
    page=requests.get(movie_url)
    soup=BeautifulSoup(page.text,"html.parser")

    main_div=soup.find("h1",class_="scoreboard__title").get_text()
    
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
    with open("task4.json","w") as f:
        json.dump(top_movie_details,f,indent=4)
    pprint.pprint(top_movie_details)
scrap_movie_details()