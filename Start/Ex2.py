from flask import Flask
app = Flask(__name__)

@app.route('/')
def WWE():
	return 'Welcome WWE Universe'

@app.route('/TLC/')
def TLC():
   	return 'Welcome To TLC 2018\nDo Not Try This At Home' 

@app.route('/TLC/<match>')
def hello_name(match):
	return 'Its %s!' % match

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=2002 , debug = True)

