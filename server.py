# RFC2324 at Hacker School
from flask import Flask, request
import random
#import Brew


hot_beverages = ('coffee','tea','hot cocoa','yerba mate', 'spiced cider')

# init the web server
app = Flask(__name__)

# init the hardware control
#io = Brew(100,16)

@app.route('/',methods=['GET','BREW','POST'])
def index():	
	
	res_body = ""
	your_hot_beverage = hot_beverages[random.randint(0,len(hot_beverages)-1)]

	# handle brew and post
	if request.method == 'BREW' or request.method == 'POST':

		if request.form['coffee-message-body'] == "start":
			res_body = "Brewing " + your_hot_beverage
		
		elif request.form['coffee-message-body'] == "stop":
			res_body = "Ok, stopping the brewing process"
		
		else:
			res_body ="Nope"
	
	# handle get
	elif request.method == 'GET':
		res_body = "Sorry, you've got to get your own coffee :-p"
	
	# handle others
	else:
		res_body = "Not yet implemented"

	return res_body,418

 
if __name__ == '__main__':
	app.run()