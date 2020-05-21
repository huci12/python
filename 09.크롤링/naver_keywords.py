import requests

from bs4 import BeautifulSoup
import time

def time_function(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = f(*args,**kwargs)
        end_time = time.time() -start_time
        print("{} {} time {}".format(f.__name__,args[1],end_time))
    return wrapper

@time_function
def r_find_all(url , parser):
    r = requests.get(url)
    if r.ok :
        bs = BeautifulSoup(r.text,parser)
        #print(bs)
        lists = bs.select(".list_weather > li")
        
        for li in lists :
            areaName = li.find("span" ,{"class": "txt_part"}).get_text()
            temper = li.find("span" ,{"class": "txt_temper"}).get_text()
            status = li.find("strong").get_text()
            print("지역 : {} | 날씨 : {} | 온도 : {}".format(areaName,status,temper))

@time_function           
def r_select(url,parser):
    r = requests.get(url)
    if r.ok :
        bs = BeautifulSoup(r.text,parser)
        lists = bs.select(".list_weather > li")
        for li in lists :
            areaName = li.find("span" ,{"class": "txt_part"}).get_text()
            temper = li.find("span" ,{"class": "txt_temper"}).get_text()
            status = li.find("strong").get_text()
            print("지역 : {} | 날씨 : {} | 온도 : {}".format(areaName,status,temper))


# 아래 주소가 메인페이지 내부에서 호출되는 실시간 검색어 데이터를 넘겨주는 주소
# request.get("주소").json() 을 하면 데이터를 json 형태로 받아올 수 있습니다.
# 아래 주소를 직접 브라우저에서 접속해보시기 바랍니다.
def getNaverKeyWords() : 
    json = requests.get('https://www.naver.com/srchrank?frm=main').json()

    ranks = json.get("data")
    print("NAVER의 검색 랭킹")
    for r in ranks :
        #각 데이터는 rank , keyword , keyword_synomyms
        rank = r.get("rank")
        keyword = r.get("keyword")
        print(rank, keyword)

#naver가 이제 바뀌었기 때문에 다음의 날씨 정보로 가져오자

print("다음에서 가져온 날씨 정보")

r_find_all("https://www.daum.net","html.parser")

r_select("https://www.daum.net" , "lxml")

