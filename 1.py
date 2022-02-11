from bs4 import BeautifulSoup
import requests
import re
import pprint 
def scrap_top_list():
    url="https://www.rottentomatoes.com/top/bestofrt/"
    sample=requests.get(url)
    soup=BeautifulSoup(sample.text,"html.parser")
    main_div=soup.find_all("table",class_="table")
    print(main_div)
    print(main_div)
    movie_ranks=[]
    movie_names=[]
    no_of_reviews=[]
    movie_urlses=[]
    movie_ratings=[]
    year_of_realease=[]
    for tr in main_div:
        for i in tr.find_all('tr')[1:]:
            movie_rank=i.find("td",class_="bold").text
            movie_ranks.append(movie_rank)
        #             print(movie_rank)
    # scrap_top_list()
            movie_name=i.find("a",class_="unstyled articleLink").text.strip()
            name=movie_name
            movie_name=re.split('(\d+)',name)
            year_of_realease.append(movie_name[-2])
#             print(year_of_realease)
# scrap_top_list()


            names=movie_name[0]
            namename=names.replace("(","")
            movie_names.append(namename)
    # print(movie_names)
        # scrap_top_list()
            movie_review=i.find("td",class_="right hidden-xs").get_text()
            no_of_reviews.append(movie_review)
        # print(no_of_reviews)
            movie_rating=i.find("span",class_="tMeterScore").get_text()
            movie_ratings.append(movie_rating)
        #         print(movie_ratings)
        # scrap_top_list()
            movie_rating=i.find("span",class_="tMeterScore").get_text()
            movie_ratings.append(movie_rating)
            # print(movie_ratings)

            url=i.find("a",class_="unstyled articleLink")["href"]
            movie_url="https://www.rottentomatoes.com"+url
            movie_urlses.append(movie_url)
            # pprint.pprint(movie_urlses)

    Top_movies=[]
    details={'position':'','Rating':'','Name':'','year':"",'url':'','movie_Review':''}
    for i in range(0,len(movie_ranks)):
        details['position']=str(movie_ranks[i])
        details['Rating']=str(movie_ratings[i])
        details['Name']=str(movie_names[i])
        details['year']=str(year_of_realease[i])
        details['url']=str(movie_urlses[i])
        details['movie_Review']=str(no_of_reviews[i])
        Top_movies.append(details.copy())
    pprint.pprint(Top_movies)
scrap_top_list()


# p=10
# q=20
# p=p*q//4
# q=p+q**3
# print(p,q)





# list1 = [2, -7, 5, -64, -14]
# i=0
# c=0
# d=0
# while i<len(list1):
#     if list1[i]>1:
#         c=c+1
#     else:
#         d=d+1
#     i=i+1
# print("positiv",c)
# print("nagative",d)



# list=[[{"datail":["manisha","neha","m"]},{"a":3,"b":8},{"datail":[7,9,3]}]]
# for i in list:
#     for j in i[list]:
#         print(j)



    