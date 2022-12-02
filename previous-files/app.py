import sqlite3
import base64
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
    # this is a function that i defined below, it is assigned to the data
    # variable and then passed to the index.html
    all_data = get_db()
    # the all_data below is what is reference in index.html, the name has to be the same
    return all_data
        # render_template("index.html", recipes = recipes, ingredients = ingredients)

@app.route("/all-recipes")
def all_recipes():
    all_data = get_all_recipes()
    rec_names = all_data[0]
    rec_levels = all_data[1]
    rec_durations = all_data[2]
    rec_instructions = all_data[3]
    ingr_quantities = all_data[4]
    ingr_units = all_data[5]
    ingr_preps = all_data[6]
    ingr_names = all_data[7]

    dicti = dict(zip(rec_names, ingr_names, ingr_preps))

    return dicti
    # render_template("all-recipes.html",
    #                        rec_names=rec_names,
    #                        rec_levels=rec_levels,
    #                        rec_durations=rec_durations,
    #                        rec_instructions=rec_instructions,
    #                        ingr_quantities=ingr_quantities,
    #                        ingr_units=ingr_units,
    #                        ingr_preps=ingr_preps,
    #                        ingr_names=ingr_names)


# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect('recipes.db')
#         cursor = db.cursor()
#         cursor.execute("select ingredient_name from ingredient")
#         all_ingredients = cursor.fetchall()
#         all_ingredients = [str(val[0]) for val in all_ingredients]
#         cursor.execute("select recipe_name from recipe")
#         all_recipes = cursor.fetchall()
#         all_recipes = [str(val[0]) for val in all_recipes]
#     return all_ingredients, all_recipes

def remove_duplicates(list):
    list = list(dict)


def get_all_recipes():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect('recipes.db')
        cursor = db.cursor()
        cursor.execute("""SELECT DISTINCT * FROM recipe 
                        INNER JOIN level ON recipe.level_id = level.level_id
                        INNER JOIN recipe_ingredient ON recipe.recipe_id = recipe_ingredient.recipe_id
                        INNER JOIN ingredient ON ingredient.ingredient_id = recipe_ingredient.ingredient_id
                        """)
        all_data = cursor.fetchall()
        recipe_names = [str(col[1]) for col in all_data]
        # recipe_img = [str(col[3]) for col in all_recipes]
        recipe_levels = [str(col[7]) for col in all_data]
        duration_min = [str(col[4]) for col in all_data]
        instructions = [str(col[5]) for col in all_data]
        ingr_quantity = [str(col[11]) for col in all_data]
        ingr_unit = [str(col[12]) for col in all_data]
        ing_prep = [str(col[13]) for col in all_data]
        recipe_ingredients = [str(col[15]) for col in all_data]
        all_data = [recipe_names, recipe_levels, duration_min, instructions, ingr_quantity, ingr_unit, ing_prep, recipe_ingredients]

    return all_data


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# app.jinja_env.globals.update(encode_file=encode_file)


if __name__ == '__main__':
    app.run()
