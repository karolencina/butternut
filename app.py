import sqlite3
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "asfubre845*^&%uvdjshd*&uikjsd><;.f"


@app.route("/")
def index():
    # this is a function that i defined below, it is assigned to the data
    # variable and then passed to the index.html
    ingredients, recipes = get_db()
    # the all_data below is what is reference in index.html, the name has to be the same
    return render_template("index.html", recipes = recipes, ingredients = ingredients)


@app.route("/add_items", methods=["POST"])
def add_items():
    return request.form["select_items"]


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('recipes.db')
        cursor = db.cursor()
        cursor.execute("select name from ingredients")
        all_ingredients = cursor.fetchall()
        all_ingredients = [str(val[0]) for val in all_ingredients]
        cursor.execute("select name from recipes")
        all_recipes = cursor.fetchall()
        all_recipes = [str(val[0]) for val in all_recipes]
    return all_ingredients, all_recipes

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()
