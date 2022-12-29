import datetime
from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo

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

    guests = mongo.db.wedding.find()
    
    
    return render_template('index.html', diff=diff, guests=guests)

if __name__ == '__main__':
    app.run()