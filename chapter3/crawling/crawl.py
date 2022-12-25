import requests # 설치한 패키지인 request 가져오기
from bs4 import BeautifulSoup # 설치한 패키지인 BeautifulSoup 가져오기

res = requests.get('http://www.yes24.com/24/Category/BestSeller') # 해당 url의 데이터 가져오기
soup = BeautifulSoup(res.text, 'html.parser')
# res.text : yes24베스트셀러 url로부터 받은 데이터의 text값
# 'html.parser' : beautifulSoup이 약속해놓은 값으로, html 코드 분석해달라는 의미

# for i in range(1, 40+1):
#     selector = '#bestList > ol > li.num' + str(i) + ' > p:nth-child(3) > a'
    
#     if i == 19 or i == 20:
#         selector = '#bestList > ol > li.num' + str(i) + '_line > p:nth-child(3) > a'
    
#     title = soup.select_one(selector).text
#     print(title)

selector = '#bestList > ol > li > p:nth-child(3) > a'
titles = soup.select(selector)

for i in range(40):
    print(titles[i].text)

# for title in titles:
#    print(title.text)