from flask import Flask
app = Flask(__name__)
@app.route('/')
def add():
    return "Hello"
if __name__ == '__main__':
    app.run(debug=True,host='13.37.228.209',port=5000)




