import requests
from bs4 import BeautifulSoup
import re
import pprint
import json
def pickel_information():
    url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    url_1=requests.get(url)
    soup=BeautifulSoup(url_1.text,"html.parser")
    # print(soup)
    main_data=soup.find("div",class_="_3RA-")
    main_div=main_data.find_all("div",class_="_1fje")
    pickle_name=[]
    pickle_price=[]
    pickle_link=[]
    pickle_image=[]
    pickle_position=[]
    count=0
    for div in main_div:
        all=div.find_all("div",class_="_2i1r")
        for i in all:
            name=i.find("div",class_="_2PhD").text
            namename=re.split("(\d+)",name)
            # pickle_name.append(namename[0])

            name=namename[0]
            n=name.replace("(","")
            pickle_name.append(n)
        # print(pickle_name)
            price=i.find("div",class_="_1kMS").get_text()
            pickle_price.append(price)
            # print(pickle_price)
            link=i.find("a",class_="_8vVO")['href']
            urls=url+link
            pickle_link.append(urls)
            img=i.find("div",class_="_3nWP")
            # g=img.find("div",class_="")
            for i in img:
                pickle_image.append(i["src"])
                count=count+1
            pickle_position.append(count)
    # print(pickle_position)
                
    Top_list=[]
    dict={"pickle_position":"","pickle_name":"","pickle_price":"","pickle_image":"","pickle_link":""}
    for i in range(0,len(pickle_price)):
        dict["pickle_name"]=(pickle_name[i])
        dict["pickle_position"]=(pickle_position[i])
        dict["pickle_price"]=(pickle_price[i])
        dict["pickle_link"]=(pickle_link[i])
        dict["pickle_image"]=(pickle_image[i])
        
        Top_list.append(dict.copy())
        with open("pickle.json","w") as f:
            json.dump(Top_list,f,indent=4)
    # return Top_list

    pprint.pprint(Top_list)
pickel_information()