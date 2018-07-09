from flask import Flask
app = Flask(__name__)

@app.route('/hello/')
def hello():
   return 'Hello!' 

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=2001, debug = True)
