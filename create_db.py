import sqlite3


# IMAGES ISSUE
def decode_file(pathname):
  with open(pathname, 'rb') as file:
    data = file.read()
  return data


recipes = [
  ("Hummus",
   "easy",
   30,
   """Blend tahini and lemon juice in a food processor.; 
   Add olive oli, cumin, minced garlic and salt.;
   Blend again.;
   Drain and rinse chickpeas and add to food processor.;
   Blend with the rest of the ingredients.;
   Serve with veggies.""",
   """1 can chickpeas; 
   1/4 cup tahini;
   1/4 cup lemon juice;
   1 minced garlic clove; 
   2 tbsp olive oil;
   any veggies"""),

  ("Toast",
   "easy",
   20,
   """Cut a slice of bread.; 
   Spread cream cheese on the bread.;
   Place sun-dried tomatoes and rocket on top.;
   Slice the avocado half and place it on top.""",
   """1 slice sourdough loaf;
   1/2 avocado;
   1 cup rocket;
   1/2 cup sun-dried tomatoes;
   2tbsp cream cheese;
   1 tsp sesame seeds
   """),

  ("Veggie soup",
   "medium",
   140,
   """Cut all veggies into cubes.;
   Add all veggies to pot and bring to boil.;
   Cook on low heat for 90 minutes.;
   Add lentils.;
   Cook for half an hour.;
   Serve.
   """,
   """3 carrots; 
   1 celery stalk;
   1 cup washed lentils;
   1 onion;
   2 cloves garlic;
   1 tbsp ginger powder;
   2 tbsp turmeric;
   2 tsp salt
   """),

  ("Banana bread",
   "medium",
   90,
   """Preheat oven to 180°C.;
   In a large bowl mash bananas with fork.;
   Add in all wet ingredients.;
   In a separate bowl combine dry ingredients.;
   Stir in the dry ingredients into the wet.;
   Grease pan with coconut oil and place the mixture in.;
   Bake for 60 minutes.""",
   """3 ripe bananas; 
   3 tbsp date or maple syrup;
   120 ml coconut oil;
   20 ml oat milk;
   1 egg;
   1 tsp vanilla extract;
   120 g ground almonds;
   80 g oats;
   120 g walnuts;
   150 g dark chocolate chips;
   1 tbsp cinnamon;
   2 tsp baking powder;
   1 tsp baking soda;
   1/4 tsp salt
   """)
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

cursor.executemany("""INSERT INTO recipe (
        recipe_name, 
        level, 
        duration_min, 
        instructions, 
        ingredients) 
        VALUES (?,?,?,?,?
        )""", recipes)
print("added ", recipes)

connection.commit()
connection.close()