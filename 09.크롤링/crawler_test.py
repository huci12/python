'''
1.원하는 웹페이지에 접속하여 HTML 데이터를 받아 온다.
2.받아온 HTML 데이터를 분석 가능한 형태로 가공한다.
3.원하는 데이터를 추출한다.


'''

import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

#requests
response = requests.get("https://www.naver.com")

#print(response.status_code)
#print(response.headers)
#print(response.content)
#print(response.text)


#BeautifulSoup
bs = BeautifulSoup(response.text , "html.parser")
for img in bs.select("img") :
    print(img)
for a in bs.select("a") : 
    print(a)

#session = HTMLSession()
#response = session.get("https://www.naver.com")
#print(response.html.links)


