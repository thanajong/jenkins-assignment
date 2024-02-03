from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Index"

@app.route("/getcode")
def hello():
    return "Hello, World!"

@app.route("/plus/<num1>/<num2>")
def plus(num1,num2):
    return str(int(num1)+int(num2))

if __name__ == '__main__':
      app.run()
