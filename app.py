from flask import Flask, render_template, request, flash
import random

app = Flask(__name__)
app.secret_key ="poopman69"

@app.route("/")
def hello():
    flash("Welcome to wrastlin, you little bitch! You ready to enter the squared circle or are you a candy-ass jabroni?!")
    return render_template("index.html")
    