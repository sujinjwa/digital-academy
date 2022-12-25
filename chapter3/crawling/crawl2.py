import requests # 설치한 패키지인 request 가져오기
from bs4 import BeautifulSoup # 설치한 패키지인 BeautifulSoup 가져오기

res = requests.get('http://www.yes24.com/24/Category/BestSeller') # 해당 url의 데이터 가져오기
soup = BeautifulSoup(res.text, 'html.parser')
# res.text : yes24베스트셀러 url로부터 받은 데이터의 text값
# 'html.parser' : beautifulSoup이 약속해놓은 값으로, html 코드 분석해달라는 의미

bookSelector = '#bestList > ol > li > p:nth-child(3) > a'
books = soup.select(bookSelector)
for i in range(3):
    url = books[i]['href'] # 각 a 태그의 href 가져오기

    bookRes = requests.get('http://www.yes24.com' + url) # 각 책의 세부페이지의 데이터 가져오기
    bookSoup = BeautifulSoup(bookRes.text, 'html.parser') # 각 세부페이지의 html 코드 분석하여 저장

    soldAmountSelector = '#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_ratingArea > span.gd_sellNum'
    soldAmount = bookSoup.select_one(soldAmountSelector) # 판매지수 데이터 selector값으로 찾기

    print('책 제목: ' + str(books[i].text))
    print('판매지수: ' + str(soldAmount.text[-15:-8])) # 판매지수의 text 값에서 판매지수를 나타내는 부분만 slice 하여 가져오기
    print('----------------')