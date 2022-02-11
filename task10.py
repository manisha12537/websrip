from task1 import scrap_top_list
import json
import pprint
scrap=scrap_top_list()
def get_movie_detail_list():
    file=open("task5.json")
    load_file=json.load(file)
    director_list=[]
    language_list=[]
    director_dic={}
    for i in load_file:
        if i["Original Language:"] not in director_list:
            director_list.append(i["Original Language:"])
        if i["Director:"] not in language_list:
            language_list.append(i["Director:"])
    for j in language_list:
        director_dic[j]={}
        for k in director_list:
        # print(director_dic)
            for i in range(len(scrap)):
                director_dic[j][k]=0
    pprint.pprint(director_dic)
                
movie_detail=get_movie_detail_list()









# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3={}
# for i,k in d1.items():
#     for j,l in  d2.items():
#         if k==l:
#             d3[i]=(k+l)
#             d4={}
#             for d in (d1,d2,d3):
#                 d4.update(d)
# print(d4)



    























# def analse_language_and_director(movie_list):
#     director_dic={}
#     for movie in movie_list:
#         for director in movie["Director:"]:
#             director_dic[director]={}
#     for i in range(len(movie_list)):
#         for director in director_dic:
#             if director in movie_list[i]["Director:"]:
#                 for language in movie_list[i]["Original Language"]:
#                     director_dic[director][language]=0
#     print(director_dic)
# director_by_language=analse_language_and_director(movie_detail)

# print(director_by_language)

