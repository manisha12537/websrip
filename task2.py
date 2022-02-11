from  task1 import scrap_top_list
import json
import pprint

scrapped=scrap_top_list()

def group_by_year(movie):
    years=[]
    for i in movie:
        year=i["year"]
        # print(year)
    
        if year not in years:
            years.append(year)
   
    movie_dict={i:[]for i in years}
    # print(movie_dict)
    for i in movie:
        year=i["year"]
        for x in movie_dict:
            if str(x)==str(year):
        # print(year)
                movie_dict[x].append(i)
                # print(movie_dict)
    with open("task2.json","w") as f:
        json.dump(movie_dict,f,indent=4)
    pprint.pprint(movie_dict)
    return (movie_dict)
group_by_year(scrapped)



