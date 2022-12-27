from pymongo import MongoClient # mongoClient와 연결하기

client = MongoClient('mongodb://localhost:27017/')

db = client.local # 데이터베이스에 연결하기
collection = db.fastCampus # 컬렉션에 연결하기

user = {'name': 'Sujin', 'age': 23, 'gender': 'woman'}

collection.insert_one(user)

print(collection.find_one({'name':'Sujin'}))
# data = {'name': 'Sujin Jo',
#         'age': 23,
#         'gender': 'woman'}

# datas = db.datas
# data_id = datas.insert_one(data).inserted_id
# print(data_id)