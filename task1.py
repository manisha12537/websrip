from bs4 import BeautifulSoup
import requests
import re
import json
import pprint

def scrap_top_list():
    url="https://www.rottentomatoes.com/top/bestofrt/"
    sample=requests.get(url)
    soup=BeautifulSoup(sample.text,"html.parser")
    main_div=soup.find("table",class_="table")

    movie_ranks=[]
    movie_names=[]
    no_of_reviews=[]
    movie_urlss=[]
    movie_ratings=[]
    year_of_realease=[]

    tr=main_div.find_all("tr")
    for i in tr[1:]:
        movie_rank=i.find("td",class_="bold").text
        movie_ranks.append(movie_rank)

        movie_name=i.find("a",class_="unstyled articleLink").text.strip()
        name=movie_name
        movie_name=re.split('(\d+)',name)
        year_of_realease.append(movie_name[-2])

        names=movie_name[0]
        namename=names.replace("(","")
        movie_names.append(namename)

        movie_review=i.find("td",class_="right hidden-xs").get_text()
        no_of_reviews.append(movie_review)

        movie_rating=i.find("span",class_="tMeterScore").get_text()
        movie_ratings.append(movie_rating)
    

        url=i.find("a",class_="unstyled articleLink")["href"]
        movie_url="https://www.rottentomatoes.com"+url
        movie_urlss.append(movie_url)
   

    Top_movies=[]
    details={'position':'','Rating':'','Name':'','year':"",'url':'','movie_Review':''}
    for i in range(0,len(movie_ranks)):
        details['position']=str(movie_ranks[i])
        details['Rating']=str(movie_ratings[i])
        details['Name']=str(movie_names[i])
        details['year']=str(year_of_realease[i])
        details['url']=str(movie_urlss[i])
        details['movie_Review']=str(no_of_reviews[i])
        Top_movies.append(details.copy())
        print(Top_movies)
    with open("task1.json","w")as f:
        json.dump(Top_movies,f,indent=4)
    return(Top_movies)

    
    # pprint.pprint(Top_movies)
# scrap_top_list()

