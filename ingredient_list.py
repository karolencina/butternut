

import sqlite3

ingredients = [
  "apple",
  "banana",
  "dill",
  "egg",
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

recipes = [
  ("Hummus", 1, 30, "1. Blend chickpea and Tahini \n2. Add lemon juice."),
  ("Toast", 1, 20, "1. Cut a slice of bread. \n2. Place sun-dried tomatoes, avocado and rocket on top.")
]

levels = [
  ("easy"),
  ("medium"),
  ("hard")
]


ingredients = sorted(ingredients)

connection = sqlite3.connect("recipes.db")
connection.execute("PRAGMA foreign_keys = 1")
cursor = connection.cursor()

cursor.execute("create table ingredients (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")

# levels table has to be created before recipe is created, otherwise I get an integrity error (FK constraint failed)
cursor.execute("""CREATE TABLE level (
      level_id INTEGER PRIMARY KEY AUTOINCREMENT,
      level_name TEXT
)""")

cursor.execute("""CREATE TABLE recipe (
      recipe_id INTEGER PRIMARY KEY AUTOINCREMENT, 
      recipe_name TEXT, 
      level_id INTEGER NOT NULL, 
      duration_min INTEGER, 
      instructions TEXT,
      FOREIGN KEY (level_id) REFERENCES level(level_id)
)""")





for i in range(len(ingredients)):
  cursor.execute("insert into ingredients (name) values (?)",[ingredients[i]])
  print("added ", ingredients[i])

for i in range(len(levels)):
  cursor.execute("insert into level (level_name) values (?)", [levels[i]])
  print("added ", levels[i])

cursor.executemany("INSERT INTO recipe (recipe_name, level_id, duration_min, instructions) VALUES (?,?,?,?)", recipes)
print("added ", recipes)


connection.commit()
connection.close()