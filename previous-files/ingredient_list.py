

import sqlite3

ingredients = [
  "apple",
  "banana",
  "dill",
  "egg",
  "avocado",
  "flour",
  "granola",
  "honey",
  "lemon",
  "onion",
  "potato",
  "rosemary",
  "salt",
  "thyme",
  "vinegar",
  "watermelon",
  "pear",
  "cucumber",
  "garlic",
  "carrot",
  "eggplant",
  "rice",
  "lentils",
  "lime",
  "broth",
  "mushrooms",
  "orange",
  "lettuce",
  "cheese",
  "cilantro"
]


def decode_file(pathname):
  with open(pathname, 'rb') as file:
    data = file.read()
  return data


recipes = [
  ("Hummus", decode_file("static/files/img-db/avo-bread.jpg"), 1, 30, "1. Blend chickpea and Tahini \n2. Add lemon juice."),
  ("Toast", decode_file("/Users/Karo/Documents/My Photo.png"), 1, 20, "1. Cut a slice of bread. \n2. Place sun-dried tomatoes, avocado and rocket on top.")
]

recipe_ingredients = [
  (2, 5, 1/2, None, "sliced"),
  (2, 2, 2, "tbsp", "grated"),
  (2, 8, 2, "cups", "shredded"),
  (2, 9, 2, "cups", "shredded"),
]

levels = [
  "easy",
  "medium",
  "hard"
]


ingredients = sorted(ingredients)

connection = sqlite3.connect("recipes.db")
connection.execute("PRAGMA foreign_keys = 1")
cursor = connection.cursor()

cursor.execute("DROP TABLE recipe_ingredient")
cursor.execute("DROP TABLE recipe")
cursor.execute("DROP TABLE level")
cursor.execute("DROP TABLE ingredient")

cursor.execute("""CREATE TABLE ingredient (
      ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT, 
      ingredient_name TEXT
)""")

# levels table has to be created before recipe is created, otherwise I get an integrity error (FK constraint failed)
cursor.execute("""CREATE TABLE level (
      level_id INTEGER PRIMARY KEY AUTOINCREMENT,
      level_name TEXT
)""")

cursor.execute("""CREATE TABLE recipe (
      recipe_id INTEGER PRIMARY KEY AUTOINCREMENT, 
      recipe_name TEXT, 
      recipe_img BLOB,
      level_id INTEGER, 
      duration_min INTEGER, 
      instructions TEXT,
      FOREIGN KEY (level_id) REFERENCES level(level_id)
)""")

cursor.execute("""CREATE TABLE recipe_ingredient (
      recipe_ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
      recipe_id INTEGER, 
      ingredient_id INTEGER,
      quantity INTEGER, 
      unit TEXT, 
      prep TEXT,
      FOREIGN KEY (recipe_id) REFERENCES recipe(recipe_id)
      FOREIGN KEY (ingredient_id) REFERENCES ingredient(ingredient_id)
)""")


for i in range(len(ingredients)):
  cursor.execute("insert into ingredient (ingredient_name) values (?)",[ingredients[i]])
  print("added ", ingredients[i])

for i in range(len(levels)):
  cursor.execute("insert into level (level_name) values (?)", [levels[i]])
  print("added ", levels[i])

cursor.executemany("INSERT INTO recipe (recipe_name, recipe_img, level_id, duration_min, instructions) VALUES (?,?,?,?,?)", recipes)
print("added ", recipes)

cursor.executemany("INSERT INTO recipe_ingredient (recipe_id, ingredient_id, quantity, unit, prep) VALUES (?,?,?,?,?)", recipe_ingredients)
print(recipe_ingredients)

connection.commit()
connection.close()