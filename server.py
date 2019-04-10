from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect

import os

import json
app = Flask(__name__)

@app.route("/text-render")
def hello_world():
	return "Hello World"

@app.route("/json-ex")
def json_example():
	exAr = [1, {"alex": "junior", "school": "Milton Academy"}, True]
	return json.dumps(exAr)

@app.route("/")
def index():
	return render_template("index.html",name="alex")

@app.route("/say-hello/<name>")
def say_hello_url_param(name=None):
	return render_template("index.html",name=name)


@app.route("/say-hello-form", methods=["GET", "POST"])
def say_hello_form():
	if request.method == "POST":
		name = request.form["name"]
		print "Found the name: " + name
		return render_template("index.html",name=name)
	else:
		return redirect("/")




@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

