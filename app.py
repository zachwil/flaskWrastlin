#from crypt import methods
from flask import Flask, render_template, request, flash, redirect, url_for
import random

app = Flask(__name__)
app.secret_key ="poopman69"

@app.route("/")
def index():
    flash("Welcome to wrastlin, you little bitch! You ready to enter the squared circle or are you a candy-ass jabroni?!")
    return render_template("index.html")
#@app.route("/promo", methods = ["POST", "GET"])


@app.route("/greet", methods = ["POST", "GET"])
def promo():
    flash("THIS IS THE SECOND PAGE NOW, YOU LITTLE BITCH")
    return render_template("landing.html")
    #return 'test'

    