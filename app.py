from flask import Flask, render_template, request, flash
import random

app = Flask(__name__)
app.secret_key ="poopman69"

@app.route("/")
def hello():
    return("Welcome to wrastlin, you little bitch!")
    