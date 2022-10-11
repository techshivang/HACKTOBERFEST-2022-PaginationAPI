import requests
import json
baseURL = "https://dummyjson.com/products"

def fetch(url):
    try:
        req = requests.get(url=url)
        if(req.status_code == 200):
            data = req.text
            data = json.loads(data)
            return {"statusCode":200,"count":len(data["products"]),"result":data["products"]}
    except:
        return {"statusCode":400,"result":[]}

def get_paginated_list(data,url,page_number,limit):
    try:
        start = (page_number*limit)-(limit)
        if(start == 0 or start == 1):
            next_page = page_number + 1
            prev_link = ""
            next_link = url + "?page={}&limit={}".format(next_page,limit)
        else:
            next_page = page_number + 1
            prev_page = page_number - 1
            prev_link = url + "?page={}&limit={}".format(prev_page,limit)
            next_link = url + "?page={}&limit={}".format(next_page,limit)
        if(start == 0):
            result = data[start:(page_number*limit)]
        else:
            result = data[start-1:(page_number*limit)]
        return {"statusCode":200,"next_link":next_link,"prev_link":prev_link,"result":result}
            
    except Exception as e:
        print("Error :",e)
        return {"statusCode":400,"result":[]}

data = fetch(baseURL)
length = data["count"]
url="http://localhost:8000/products"
print(get_paginated_list(data=data["result"],url=url,page_number=2,limit=5))