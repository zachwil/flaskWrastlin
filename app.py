#from crypt import methods
from flask import Flask, render_template, request, flash, redirect, url_for
import random

app = Flask(__name__)
app.secret_key ="poopman69"



@app.route("/")
def index():
    flash("Welcome to wrastlin! You ready to enter the squared circle or are you a candy-ass jabroni?!")
    return render_template("index.html")
#@app.route("/promo", methods = ["POST", "GET"])


@app.route("/greet", methods = ["POST", "GET"])
def get_computer_move():
    options = ["rock", "paper", "scissors"]
    return options[random.randint(0,2)]

def get_winner(player_choice, computer_choice):
    winner = "computer"

    if player_choice == computer_choice:
        winner = "tie"
    if player_choice == "rock" and computer_choice == "scissors":
        winner = "player"
    if player_choice == "scissors" and computer_choice == "paper":
        winner = "player"
    if player_choice == "paper" and computer_choice == "rock":
        winner = "player"

    return winner



def promo():
    
    
    
    player_choice = request.form.get("bitchName", "").upper()  # empty string is the default
    message=f"Rock, Paper, or Scissors Jabroni!? {player_choice}"
    return render_template("landing.html", bitch_message=message)
    



# just run 'python app.py' to run this way
if __name__ == "__main__":
    app.run(debug=True)