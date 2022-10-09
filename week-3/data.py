import urllib.request as request
import json
import re
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response) # 利用json模組處理 json 資料格式
# 將公司名稱列表出來
clist=data["result"]["results"]

with open("data.csv",mode="w",encoding="utf-8") as file:
    for company in clist:
        xdate=company["xpostDate"]
        http=company["file"]
        xpostDate=xdate.split('/')
        https=re.split("jpg|JPG",http)
        if xpostDate[0]>="2015":                  
            file.write(company["stitle"]+","+company["address"][5]+company["address"][6]+company["address"][7]+","+company["longitude"]+","+
                company["latitude"]+","+https[0]+"jpg"+"\n")   
    
    
         
            
        
