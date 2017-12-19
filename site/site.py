from flask import Flask, render_template
app = Flask(__name__)
#https://www.raspberrypi-spy.co.uk/2017/07/create-a-basic-python-web-server-with-flask/

@app.route("/")
def index():
	data=[]
	return render_template('index.html', data=data)
  
if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)