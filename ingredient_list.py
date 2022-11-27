

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

ingredients = sorted(ingredients)

connection = sqlite3.connect("recipes.db")
cursor = connection.cursor()

cursor.execute("create table ingredients (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
cursor.execute("create table recipes (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, img BLOB, level TEXT, duration_min INTEGER, servings INTEGER, instructions TEXT)")

for i in range(len(ingredients)):
  cursor.execute("insert into ingredients (name) values (?)",[ingredients[i]])
  print("added ", ingredients[i])

cursor.executemany("insert into recipes (name, level, duration_min, servings, instructions) values (?,?,?,?,?)", recipes)
print("added ", recipes)


connection.commit()
connection.close()