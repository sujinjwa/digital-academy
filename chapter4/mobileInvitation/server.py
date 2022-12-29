import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now() # now : 현재 날짜, 시간 정보
    wedding = datetime.datetime(2023, 2, 18, 0, 0, 0) # 결혼식 날짜
    diff = (wedding - now).days

    return render_template('index.html', diff=diff)

if __name__ == '__main__':
    app.run()