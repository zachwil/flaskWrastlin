import os
import json
import webbrowser
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import random

from db import QUERY_DB

app = Flask(__name__)
app.secret_key = "poopman69"  # very important, matters a lot


@app.route("/")
def index():
    flash(
        "Welcome to wrastlin! You ready to enter the squared circle or are you a candy-ass jabroni?!"
    )
    return render_template("index.html")


# @app.route("/promo", methods = ["POST", "GET"])


def get_computer_move():
    options = ["rock", "paper", "scissors"]
    return options[random.randint(0, 2)]


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


@app.route("/greet/", methods=["POST", "GET"])
def promo():
    # skip the game if it's a GET request
    if request.method == "GET":
        message = "Rock, Paper, or Scissors Jabroni!?"
        return render_template("landing.html", bitch_message=message)

    # Find the winner
    player_choice = request.args.get("player_choice", "")
    computer_choice = get_computer_move()
    winner = get_winner(player_choice, computer_choice)

    # Build the output string
    message = (
        "Player Choice: "
        + player_choice.upper()
        + ", Computer Choice: "
        + computer_choice.upper()
        + ", Result: "
        + winner.upper()
        + ("" if winner == "tie" else " WINS!!!!")
    )
    pee_hole_insertion(player_choice, computer_choice, winner)
    return render_template("landing.html", bitch_message=message)


@app.route("/api", methods=["POST"])
def api_wrassle():
    data = json.loads(request.data)
    player_choice = data["rpsPlayerChoice"]
    computer_choice = get_computer_move()
    winner = get_winner(player_choice, computer_choice)
    resp = {
        "player_choice": player_choice,
        "computer_choice": computer_choice,
        "winner": winner,
    }
    return jsonify(resp)


@app.route("/peeHole")
def pee_hole():
    select_query = """select * from matchresults"""
    results = QUERY_DB().select(select_query)
    return jsonify(results)


def pee_hole_insertion(playerChoice, computerChoice, Winner):
    insert_query = """INSERT INTO matchresults (player_choice, computer_choice, winner, timestamper) VALUES (%s,%s,%s,now())"""
    query_vars = (playerChoice, computerChoice, Winner)
    success = QUERY_DB().insert(insert_query, query_vars)
    return jsonify({"success": success})


# just run 'python app.py' to run this way
if __name__ == "__main__":
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new("http://127.0.0.1:5000/")
    app.run(debug=True)
