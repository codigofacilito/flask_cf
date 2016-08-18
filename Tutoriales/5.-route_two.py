from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index(): 
	return 'Hola Mundo'

@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>')
def params(name = 'valor por default', num = 0): 
	return 'Los parametros son : {} {}'.format(name, str(num))

if __name__ == '__main__':
	app.run(debug = True, port= 8000)