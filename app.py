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

@app.route("/all-recipes")
def all_recipes():
    data = get_all_data()
    return render_template("all-recipes.html", connections = data)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('recipes.db')
        cursor = db.cursor()
        cursor.execute("select ingredient_name from ingredient")
        all_ingredients = cursor.fetchall()
        all_ingredients = [str(val[0]) for val in all_ingredients]
        cursor.execute("select recipe_name from recipe")
        all_recipes = cursor.fetchall()
        all_recipes = [str(val[0]) for val in all_recipes]
    return all_ingredients, all_recipes


def get_all_data():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('recipes.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM recipe_ingredient")
        all_connections = cursor.fetchall()
        all_connections = [str(val[0]) for val in all_connections]
    return all_connections


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()
