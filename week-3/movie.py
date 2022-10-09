from array import array
import urllib.request as req
def getData(url):
    # 建立一個Request 物件 , 附加 Request Headers 的資訊
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #解析原始碼，取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div",class_="title") #群找所有 class="title" 的 div 標籤
    for title in titles:
        if title.a!=None:
            if title.a.string[1]=="好" and title.a.string[2]=="雷": 
                with open("movie.txt",mode="a",encoding="utf-8") as file:
                    file.write(title.a.string+"\n")          
    nextlink=root.find("a",string="‹ 上頁")
    return(nextlink["href"])


def getData2(url):
    # 建立一個Request 物件 , 附加 Request Headers 的資訊
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #解析原始碼，取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div",class_="title") #群找所有 class="title" 的 div 標籤           
    for title in titles:
        if title.a!=None:
            if title.a.string[1]=="普" and title.a.string[2]=="雷":
                with open("movie.txt",mode="a",encoding="utf-8") as file:
                    file.write(title.a.string+"\n")  
    nextlink=root.find("a",string="‹ 上頁")
    return(nextlink["href"])


def getData3(url):
    # 建立一個Request 物件 , 附加 Request Headers 的資訊
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
    })
    
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #解析原始碼，取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div",class_="title") #群找所有 class="title" 的 div 標籤           
    for title in titles:
        if title.a!=None:
            if title.a.string[1]=="負" and title.a.string[2]=="雷":
                with open("movie.txt",mode="a",encoding="utf-8") as file:
                    file.write(title.a.string+"\n")  
    nextlink=root.find("a",string="‹ 上頁")
    return(nextlink["href"])

pageURL="https://www.ptt.cc/bbs/movie/index.html"
pageURL2="https://www.ptt.cc/bbs/movie/index.html"
pageURL3="https://www.ptt.cc/bbs/movie/index.html"
count=0
count2=0
count3=0

while count<10:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
while count2<10:
    pageURL2="https://www.ptt.cc"+getData2(pageURL2)      
    count2+=1
while count3<10:
    pageURL3="https://www.ptt.cc"+getData3(pageURL3)
    count3+=1