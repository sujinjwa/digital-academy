import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.local # database 선택하기 = local

# yes24 베스트셀러 40권 중 책 제목 긁어오는 코드
res = requests.get('http://www.yes24.com/24/Category/BestSeller')
soup = BeautifulSoup(res.text, 'html.parser')

for i in range(40):
    idx = str(i+1)
    if idx == '19' or idx == '20':
        idx = idx + '_line'
    
    selectorString = '#bestList > ol > li.num' + idx + '> p:nth-child(3) > a'
    title = soup.select_one(selectorString)

    # db에 'yes24' 라는 컬렉션 생성 및 데이터 입력
    db['yes24'].insert_one({'Title' : title.text})

# 컬랙션에 데이터 입력한 이후 데이터 조회
collection = db.yes24

rows = collection.find()

for row in rows:
    print(row)