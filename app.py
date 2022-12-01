import sqlite3
import pandas as pd
import re
import random
from flask import Flask, session, render_template, request, g, url_for

app = Flask(__name__)
app.secret_key = "asfubre845*^&%uvdjshd*&uikjsd><;.f"


def encode_file(filename):
    with open(filename, 'wb') as file:
        data = file.write(filename)
    return data


@app.route("/")
def index():
    return all_recipes()


@app.route("/all-recipes")
def all_recipes():
    data = create_row_lists()
    return render_template("all-recipes.html", data=data)


@app.route("/about")
def about():
    return render_template("about.html")


def create_row_lists():
    connection = sqlite3.connect("recipes.db")
    df = pd.read_sql("""SELECT DISTINCT * FROM recipe""", connection)

    row_list = []
    for index, rows in df.iterrows():
        my_list = [rows.recipe_id, rows.recipe_name, rows.recipe_img, rows.level, rows.duration_min, rows.instructions, rows.ingredients]
        row_list.append(my_list)

    return row_list


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run()
