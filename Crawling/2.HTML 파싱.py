"""
날짜 : 2023/01/16
이름 : 이민혁
내용 : 파이썬 HTML 파싱 실습하기

"""

import requests as req
from bs4 import BeautifulSoup as bs

# 페이지 요청
url = "http://chhak.click/parsing/sample2.html"
html = req.get(url).text

print(html)

# 문서객체 생성
dom = bs(html, 'html-parser')

# 문서 파싱
tit = dom.hmtl.body.h1.text
txt = dom.select_one('#txt').text
lis = dom.select('ul > li')


print('tit : ',tit)
print('txt : ',txt)

for li in lis:
    print('li text : ',li.text)

