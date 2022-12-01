import sqlite3


# IMAGES ISSUE
def decode_file(pathname):
  with open(pathname, 'rb') as file:
    data = file.read()
  return data


recipes = [
  ("Hummus", "easy", 30, "1. Blend chickpea and Tahini.; 2. Add lemon juice.", "1 can chickpeas; 1 garlic clove; 0.5 tsp olive oil"),
  ("Toast", "easy", 20, "1. Cut a slice of bread.; 2. Place sun-dried tomatoes, avocado and rocket on top.", "1/2 avocado; 40g cream cheese"),
  ("Veggie soup", "medium", 60, "1. Chop all veggies.; 2. Add all veggies to pot and bring to boil.", "3 carrots; 1 celery")
]

connection = sqlite3.connect("recipes.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS recipe")

cursor.execute("""CREATE TABLE recipe (
      recipe_id INTEGER PRIMARY KEY AUTOINCREMENT, 
      recipe_name TEXT, 
      recipe_img BLOB,
      level INTEGER, 
      duration_min INTEGER, 
      instructions TEXT,
      ingredients TEXT
)""")

cursor.executemany("INSERT INTO recipe (recipe_name, level, duration_min, instructions, ingredients) VALUES (?,?,?,?,?)", recipes)
print("added ", recipes)

connection.commit()
connection.close()