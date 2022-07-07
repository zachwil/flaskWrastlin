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


@app.route("/greet", methods = ["POST", "GET"])
def promo():
    # skip the game if it's a GET request
    if request.method == "GET":
        message = "Rock, Paper, or Scissors Jabroni!?"
        return render_template("landing.html", bitch_message=message)

    # Find the winner
    player_choice = request.form.get("rpsPlayerChoice", "")  # empty string is the default
    computer_choice = get_computer_move()
    winner = get_winner(player_choice, computer_choice)
    
    # Build the output string
    message = (
        "Player Choice: " + player_choice.upper() 
        + ", Computer Choice: " + computer_choice.upper() 
        + ", Result: " + winner.upper() + ("" if winner == "tie" else " WINS!!!!")
    )
    return render_template("landing.html", bitch_message=message)
    



# just run 'python app.py' to run this way
if __name__ == "__main__":
    app.run(debug=True)