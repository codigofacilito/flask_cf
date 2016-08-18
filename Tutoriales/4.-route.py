from flask import Flask
from flask import request

app = Flask(__name__)

#http://localhost:8000/params
#http://localhost:8000/params?params1=Param_number_one&params2=Param_number_two
@app.route('/')
def index(): 
	return 'Hola Mundo'

@app.route('/params')
def params(): 
	param1 = request.args.get('params1', 'valor por default.')
	param2 = request.args.get('params2', 'valor por default.')
	return 'El parametro es : {} , {}'.format(param1, param2)

if __name__ == '__main__':
	app.run(debug = True, port= 8000)