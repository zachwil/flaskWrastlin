# from crypt import methods
import json
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import random
import psycopg2

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


@app.route("/greet", methods=["POST", "GET"])
def promo():
    # skip the game if it's a GET request
    if request.method == "GET":
        message = "Rock, Paper, or Scissors Jabroni!?"
        return render_template("landing.html", bitch_message=message)

    # Find the winner
    player_choice = request.form.get(
        "rpsPlayerChoice", ""
    )  # empty string is the default
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
    results = None

    try:

        # postgres://:@:5432/

        connection = psycopg2.connect(
            user="uehgteyfculflr",
            password="b3f68ddbdd8768f2890d5a0c9194772c663d195dcd2246e81ae9c99444f1f80d",
            host="ec2-44-198-82-71.compute-1.amazonaws.com",
            port="5432",
            database="d3ngd0n2knndt7",
        )

        cursor = connection.cursor()

        print("Table Before updating record ")
        sql_select_query = """select * from matchresults"""
        cursor.execute(sql_select_query)
        record = cursor.fetchall()
        print(record)
        results = record

        # # Update single record now
        # sql_update_query = """Update mobile set price = %s where id = %s"""
        # cursor.execute(sql_update_query, (price, mobileId))
        # connection.commit()
        # count = cursor.rowcount
        # print(count, "Record Updated successfully ")

        # print("Table After updating record ")
        # sql_select_query = """select * from mobile where id = %s"""
        # cursor.execute(sql_select_query, (mobileId,))
        # record = cursor.fetchone()
        # print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    return jsonify(results)


def pee_hole_insertion(playerChoice, computerChoice, Winner):

    results = None

    try:

        # postgres://:@:5432/

        connection = psycopg2.connect(
            user="uehgteyfculflr",
            password="b3f68ddbdd8768f2890d5a0c9194772c663d195dcd2246e81ae9c99444f1f80d",
            host="ec2-44-198-82-71.compute-1.amazonaws.com",
            port="5432",
            database="d3ngd0n2knndt7",
        )

        cursor = connection.cursor()

        # print("Table Before updating record ")
        # sql_select_query = """select * from dingus"""
        # cursor.execute(sql_select_query)
        # record = cursor.fetchone()
        # print(record)
        # results = record

        # Update single record now
        postgres_insert_query = """ INSERT INTO matchresults (player_choice, computer_choice, winner, timestamper) VALUES (%s,%s,%s,now())"""
        record_to_insert = (playerChoice, computerChoice, Winner)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        # print("Table After updating record ")
        # sql_select_query = """select * from mobile where id = %s"""
        # cursor.execute(sql_select_query, (mobileId,))
        # record = cursor.fetchone()
        # print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    return jsonify(results)


# just run 'python app.py' to run this way
if __name__ == "__main__":
    app.run(debug=True)
