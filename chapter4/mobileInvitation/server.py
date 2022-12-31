import datetime
from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
import math

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/local'
# 'mongodb://localhost:27017' 주소의 mongoDB에 'locla' 이름의 데이터베이스 사용하겠다는 의미
mongo = PyMongo(app)

@app.route('/write', methods=['POST'])
def write():
    # name = request.form['name']
    # content = request.form['content']
    name = request.form.get('name')
    content = request.form.get('content')

    # mongo.db['wedding'].insert_one({'~'})
    mongo.db.wedding.insert_one({'name': name, 'content': content})
    return redirect('/')

@app.route('/')
def index():
    now = datetime.datetime.now() # now : 현재 날짜, 시간 정보
    wedding = datetime.datetime(2023, 2, 18, 0, 0, 0) # 결혼식 날짜
    diff = (wedding - now).days

    page = int(request.args.get('page', 1)) # 사용자가 요청한 주소에 'page'라는 data 있으면 가지고 오고, 없으면 1을 가져오기
    limit = 3
    skip = (page - 1) * limit

    # skip값만큼 스킵한 이후 limit값만 가지고 오기
    guests = mongo.db.wedding.find().limit(limit).skip(skip)
    # count_documents : 조건에 일치하는 documents 개수 가지고 오기
    countOfAllGuests = mongo.db.wedding.estimated_document_count()
    maxPage = math.ceil(countOfAllGuests / limit)

    pages = list(range(1, maxPage + 1))

    return render_template(
        'index.html', 
        diff=diff, 
        guests=guests, 
        pages=pages,
        countOfAllGuests = countOfAllGuests)

if __name__ == '__main__':
    app.run()