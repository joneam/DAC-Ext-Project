from flask import Flask, render_template, request, flash
import urllib.request, json
import os

app = Flask(__name__)

@app.route("/")
def get_axie_info():
    
    url = "https://graphql-gateway.axieinfinity.com/graphql={}".format(os.environ.get("AXIE_API_KEY"))
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template ("index.html", axies=dict["results"])

@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/axieID", methods=["POST", "GET"])
def axieID():
	flash("You have entered Axie ID " + str(request.form['id_input']))
	return render_template("index.html")
	
if __name__ == "__main__":
    app.run(debug=True)