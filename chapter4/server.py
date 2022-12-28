from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<b>Hello, World!!!</b>"

@app.route("/sujin")
def hello_Sujin():
    return "<p>Hello, Sujin!!!</p>"

if __name__ == '__main__':
    app.run()