from flask import Flask

app = Flask(__name__)#new instance, 

@app.route('/')#wrap or decorators
def index(): 
	return 'Hola mundo'#return a single String

app.run()#star the server in the port 5000