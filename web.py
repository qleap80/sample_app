from flask import Flask, render_template  #render function used to run the html page
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html') #The file should be located in the same folder

app.run(debug=True) #Debug mode. Do not need to restart the server for debugging


