import requests
from bs4 import BeautifulSoup
import json
def ecommerce_information():
    url="https://webscraper.io/test-sites"
    get_requests=requests.get(url)
    soup=BeautifulSoup(get_requests.text,"html.parser")
    div=soup.find_all("div",class_="col-md-7 pull-right")

    ecommerce_name=[]
    ecommerce_link=[]
    name_count=[]
    count=0

    for i in div:
        link=i.find("h2",class_="site-heading").a["href"]  
        links="https://webscraper.io/test-sites"+link
        ecommerce_link.append(links)

        name=i.find("h2",class_="site-heading").get_text().strip()
        ecommerce_name.append(name)
        
        count=count+1
        name_count.append(count)
    list=[]
    dict={"name_count":"","ecommerce_name":"","ecommerce_link":""}
    for i in range(0,len(name)):
        dict["name_count"]=name_count[i]
        dict["ecommerce_name"]=str(ecommerce_name[i])
        dict["ecommerce_link"]=str(ecommerce_link[i])
        # dict["name_count"]=name_count[i]

        list.append(dict.copy())
        with open("ecommerce.json","w")as f:
            json.dump(list,f,indent=4)
    # pprint.pprint(list)
ecommerce_information()




