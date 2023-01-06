import sqlite3
import pandas as pd

con = sqlite3.connect("data/recipes.db")
cur = con.cursor()
cur.execute("CREATE TABLE RECIPE(id,name,description,category,nationality,primary_ingredient,secondary_ingredient,is_vegetarian,prep_time,cook_time,serves,calories,carbs,fat,sugar,ingredients,directions,image,source)")

directions = '''1. Wrap your tortillas in a damp paper towel and put in a the microwave for 15 seconds (this will make them more pliable for folding)
	a. This step can be skipped with flour tortillas
2. Rinse your beans to remove the goo from the canning
3. Add your beans and green chiles to a bowl
4. Break your cheese into small chunks and add to the bowl
5. Mix thoroughly
	a. Optional: squish a couple handfuls of the beans in your hand to release the starch and help the entire mixture stick together
6. Make your slurry and microwave the mixture for a few seconds until somewhat gelatanous
7. Take your corn tortillas and add a strip of the mixture down the center
8. "Paint" the edge of the tortillas with your slurry and fold your tortilla over to seal it
	a. Make sure the seam side is down, to prevent it from opening again
9. Heat a film of olive oil over medium low heat in any frying pan or griddle
	a. Medium low is important as it prevents the tortillas from unsealing and helps the cheese to melt
10. Add your tortillas, seam side down, and let them sit until well-browned
11. Flip over your tortillas and brown the other side
12. Remove and serve
13. Optional tip: want a meat version? Maybe try cooking some seasoned, ground beef and adding it to the mixture!'''

ingreds = '''1. Black beans - 1 can (~15oz)
2. Green chiles - 4oz (canned preferred)
3. Melting cheese (cheddar, jack, etc.) - 4oz
4. Corn or flour tortillas 
5. Mexcian seasoning - to taste
6. Corn starch (for slurry) - 1tbsp'''

# data = [
#     (1, 'Flautas', 'Classic Mexican Flautus', 'Entree', 'Mexican', 'Beans', 'Chiles', 'TRUE', '10m', '10 min', 3,0,0,0,0,f'{ingreds}',f'{steps}'),
    
# ]
# cur.executemany("INSERT INTO RECIPE VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
# con.commit()

new_names = [
    'Teriyaki Chicken',
    'Meatballs',
    'Crunchwrap Supreme',
    'Pink Pickled Onions',
    'Simple Chicken Pan Sauce',
    'French Toast',
    'Christmas Crinkle Cookie',
    'Peanut Butter Blossoms',
    'Broccoli Beef',
    'Chicken Flatbread Wrap',
]

new_desc = [
    'Pan-fried chicken tossed in a thick ginger, garlic, and soy sauce.',
    'Large, easy meatballs with breadcrumbs, oregano, and parmesan; covered in your favorite tomato sauce.',
    'Richer, fresher, tastier, homemade version of Taco Bell\'s Crunchwrap Supreme.',
    'Simply tangy side/condiment that goes great on a sub or in a summer salad.',
    'A quick and easy pan sauce to add flavor to your chicken and de-stick your pan.',
    'Thick, flavorful french toast; the perfect way to start anyone\'s morning.',
    'Soft, rich, chocolatey cookie, dusted with powdered sugar. Perfect for the holiday season.',
    'A classic, soft, peanut butter cookie crowned with a softened hershey kiss.',
    'Simple, quick and savory; this broccoli beef is the perfect weeknight dinner.',
    'A chicken flatbread stuffed to the brim with tasty ingredients and topped with a delicious, yogurt-based, dill sauce.',
]

new_ingreds = [
    '''1Tbsp. - Cornstarch
2 scallions
1 - 0.5" piece ginger, peeled, finely grated
5 - garlic cloves, finely grated
½ - cup low-sodium soy sauce
1/4 - cup (packed) dark brown sugar
1 - Tbsp. apple cider vinegar
3 - Tbsp. vegetable oil
1½ - lb. skinless, boneless chicken thighs or breasts, thinly sliced against the grain into bite-size strips
Kosher salt, freshly ground pepper
Toasted sesame seeds and steamed white rice (for serving)''',
    '''3 -  Tbsp. extra-virgin olive oil, plus more for baking sheet
2 - large eggs
1½ - cup panko (Japanese breadcrumbs) (102g)
½ - cup milk
2 - tsp. Diamond Crystal or ¾ tsp. Morton kosher salt
1 1/2 - tsp. garlic powder
1 1/2 - tsp. oregano
Freshly ground black pepper
2 - oz. Parmesan, finely grated (about ½ cup), plus more for serving
1 - lb. ground beef (20% fat) or other ground meat
Warm homemade or store-bought tomato sauce and torn basil leaves (for serving)
''',
    '''Seasoned Beef
• 1 lb (454 g) 85/15 ground beef
• 6 g Salt
• 1 TBSP All Purpose Cumin Spice Mix
• Pinch of MSG (optional)
• 10 g Tomato Paste
• 30 g Beef Broth
All-Purpose Cumin Spice Mix
• 1 TBSP Ground Cumin
• 1/2 TBSP Chili Powder
• 1/2 TBSP Smoked Paprika
• 1/2 TBSP Garlic powder
• 1/2 TBSP Onion powder
Crunch Wrap Components
• Corn Tortilla (baked or fried)
• Large Burrito Size Flour Tortilla
• Pepper Jack Cheese, grated
• Diced Tomatoes (salted)
• Shredded Lettuce
• Sour Cream
• Green Cholula or Hot sauce of choice
• Lime Juice
• Pickled Onions
''',
    '''	1. Red onion - 1, thinly sliced
2. White vinegar - enough to halfway cover the onions in a container
3. Salt - 1 tsp
4. Sugar - 1 tsp (or to taste)
5. Lime juice - 1/2 tbsp
6. Water - 1 tbsp (optional)
7. Any spices you prefer
''',
    '''	1. Chicken stock/broth - 1 cup
	2. Cooking oil - 1/2 tbsp
	3. Butter - 2 tbsp
	4. Garlic cloves - 2, diced
	5. Shallot - 1, diced
	6. Any finisher to enhance flavor (chopped parsely/oregano/basil, sauces, herbs, citrus, etc.
	7. Cornstarch - as needed to thicken sauce
	8. Water - as needed to make slurry with cornstarch
	9. Salt - to taste
Black pepper - to taste''',
    '''6 - large eggs
¾ - cup heavy cream
¾ - cup whole milk
¼ - cup sugar
Pinch of kosher salt
6 - ¾-inch-thick slices challah, brioche, or Pullman loaf
2 - tablespoons unsalted butter, divided, plus more for serving
2 - tablespoons vegetable oil, divided
Pure maple syrup, jam, or powdered sugar (for serving)''',
    '''	• Softened butter - 8 tbsp (1/2 cup)
• Sugar - 1 3/4 cups
• Eggs - 3 large
• Vanilla extract - 1/2 tbsp
• Unsweetened chocolate - 1/2 cup (113 grams)
• Flour - 1 1/4 cup
• Baking powder - 1 1/2 tsp
• Salt - 1/2 tsp
• Confectioners sugar (for coating) - 4 tbsp''',
    '''	1. All-purpose flour - 1 3/4 cups
2. Baking soda - 3/4 tsp
3. Salt - 1/2 tsp
4. Creamy peanut butter - 3/4 cup
5. Brown sugar - 1 1/4 cup, firmly packed
6. Vanilla extract - 1 tsp
7. Eggs - 1, large
8. Milk - 3 tbsp
9. Crisco - 1/2 cup (could try butter)
10. Brach's chocolate stars or hershey kisses - 35''',
    '''For steak/marinade:
	1. Skirt steak - 1lb
	2. Soy sauce - 1 tsp
	3. Sesame oil - 1/2 tsp
	4. Corn starch - 1 tsp
	5. Baking soda - 1/2 tsp
	6. Salt - 1 tsp
	7. Garlic cloves - 3, minced
	8. Ginger - small chunk, minced (optional)
For sauce:
	1. Dark soy sauce - 1 tbsp
	2. Light soy sauce - 1 tbsp
	3. Oyster sauce - 2 tbsp
	4. Sugar - 1 tsp
Everything else:
	1. 4 stalks of broccolini or 3 stalks of broccoli
	2. Corn starch - 1/2 tsp
	3. Cold water - 1 tsp
''',
    '''Chicken Pita Roll Components
	• 1 chicken breast, cubed
	• 5 g (1 tsp) neutral oil
	• Sprinkle of salt
	• Sprinkle of oregano
	• Red pepper flakes, to taste
	• Freshly cracked black pepper, to taste
	• Pickled onions
	• Lettuce, thinly sliced
	• Tomato, thinly sliced
	• Feta cheese, crumbled
	• Lavash bread, or any flatbread
Low Cal Yogurt Herb Sauce
	• 100 g plain nonfat yogurt (like Siggis)
	• 20 g low-fat mayo
	• Dried dill, to taste
	• Dried oregano, to taste
	• Black pepper, to taste
    • Lemon juice, to taste''',
]

new_steps = [
    '''Step 1
Whisk 1 Tbsp. cornstarch and ⅓ cup water in a small bowl until cornstarch is dissolved. Set slurry aside. Start rice (to be ready by serving).

Step 2
Remove dark green parts from 2 scallions and thinly slice on a diagonal; set aside for serving. Thinly slice white and pale green parts of scallions and transfer to a medium bowl. Add one 1" piece ginger, peeled, finely grated, 5 garlic cloves, finely grated, ½ cup low-sodium soy sauce, ¼ cup (packed) dark brown sugar, and 1 Tbsp. apple cider vinegar and whisk to combine. Set sauce aside. 

Step 3
Heat 3 Tbsp. vegetable oil in a large skillet over medium-high. Add 1½ lb. skinless, boneless chicken thighs or breasts, thinly sliced against the grain into bite-size strips, in an even layer and season with kosher salt and freshly ground pepper. Cook, undisturbed, until mostly cooked through and golden underneath, about 3 minutes. Toss and continue to cook until completely cooked through, about 1 minute more. Transfer to a plate. 

Step 4
Pour reserved sauce into same skillet and reduce heat to medium. Bring to a boil, stirring constantly and scraping up browned bits. Stir slurry to combine if it has separated and add to skillet. Cook, stirring often, until sauce is thick and glossy, about 3 minutes. Return chicken to pan and toss to coat. Remove pan from heat. Top chicken teriyaki with toasted sesame seeds and reserved scallion greens. Serve with steamed white rice. 
''',
    '''Step 1
Place rack in top third of oven; preheat to 425°. Lightly brush a large rimmed baking sheet with oil. Using a sturdy wooden spoon, vigorously stir eggs, panko, milk, salt, garlic powder, oregano, several cranks of pepper, 2 oz. Parmesan, and remaining 3 Tbsp. oil in a medium bowl until nearly a smooth paste. Let the mixture rest for 10 minutes. Mix in one-quarter of meat (combining just a small amount of meat first makes it easier to incorporate the rest without overmixing). Add remaining meat and mix well to thoroughly combine, but don’t overwork it. Using oiled hands, form into 8 large meatballs and place on prepared baking sheet.

Step 2
Bake meatballs until well-browned underneath, about 15 minutes. Using a stiff metal spatula, pry up and turn over meatballs (they may want to stick a bit). Bake until browned on second side and an instant-read thermometer inserted into the center of each one registers 160°, 5–7 minutes.

Step 3
Divide meatballs among plates and spoon some sauce over. Top with basil and more Parmesan.
''',
    '''1. Mix the spice mix in a container. Set a pan over medium-high heat. Once hot, add the beef, salt, Cumin Spice Mix, a pinch of MSG, and a squirt of tomato paste. Using a potato masher crush the beef up into pebbles. Once browned and cooked through, turn the heat off. Stir in the beef broth. and set aside until ready to use.
2. Prep the crunch wrap components. Spritz the Corn tortilla with baking spray and crisp under the broiler or in a pan. Grate the pepper jack cheese, dice and salt the tomatoes, and shred the lettuce. Add the Sour cream to a small bowl with the green Cholula sauce and a spritz of lime juice. Mix together.
3. To assemble, first place the flour tortilla in the pan with the cheese in the center. Once the cheese has started to melt, remove it from the pan. Using the size of the corn tortilla as a guide, place a pile of seasoned beef in the center then add a drizzle of the spicy sour cream. Place the crispy corn tortilla over the top of the beef. Spread sour cream on the corn tortilla, then add the tomatoes, lettuce, and pickled onions.
4. Be careful not to overfill it or it will be tough to fold. Fold the flour tortilla towards the center in a circle around the corn tortilla. Place the folded side face down in a pan and crisp the bottom before flipping and crisping the top.
''',
    '''	1. Place onions in a sealable container
2. Fill with vinegar until onions are halfway submerged
3. Add all other ingredients and mix
4. Seal and put in fridge for 24 hours
5. Ready to serve
Good for 2 weeks''',
    '''	1. After your chicken has been cooked and removed from the pan, add the cooking oil, garlic, and shallot and begin sauteeing (roughly 1 minutes).
2. Add half of your stock/broth, increase the heat to medium, and reduce liquid to about half.
3. Once reduced, add rest of the liquid and butter, stir until melted
4. Now, if the sauce isn't at your desired thickness, add small quantities of your cornstarch slurry, stirring between adding, until the desired thickness is achieved
Add salt, pepper, and any finishers to your sauce, stir in, then serve.''',
    '''Step 1
Preheat oven to 250°. Lightly beat eggs, cream, milk, sugar, and salt in a large shallow baking dish (a lasagna pan is perfect). Add bread, turn to coat, then press down gently on bread until you feel it start to soak up custard mixture—this is key for a luscious, not dry, texture. Let soak, 10 minutes.

Step 2
Flip bread and soak on second side, pressing down gently from time to time, until bread is saturated but not soggy, another 10 minutes or so.

Step 3
Heat 1 Tbsp. butter and 1 Tbsp. oil in a large skillet over medium heat. When foaming subsides, carefully lift 3 slices of bread from custard, letting excess drip back into dish, and cook in skillet until golden brown and center of toast springs back when pressed, about 2 minutes per side. Transfer toast to a wire rack set inside a rimmed baking sheet and keep warm in oven while you cook remaining slices of bread with 1 Tbsp. butter and remaining 1 Tbsp. oil.

Step 4
Serve French toast with butter, maple syrup, jam, and/or powdered sugar.
''',
    '''	1. Preheat oven to 350
2. In a large bowl, beat butter and sugar with a whisk until fluffy. Add the eggs and vanilla and whisk thoroughly, 2-3 minutes.
3. Melt the chocolate in the microwave or on the stove, be careful not to burn. Pour melted chocolate into the bowl and mix well with a spatula.
4. Combine the flour, baking powder, and salt and add to the bowl. Mix well with a spatula until the dough is cohesive. Place a cover on the dough and refrigerate the dough for at least 1 hour. The dough can keep in the fridge for several days.
    ○ Note: In my tests, I found the ideal temperature of the dough for rolling is 50 to 55 F. If it is too cold, leave it on the counter for a bit before rolling.
5. When ready to bake, preheat the oven to 350 degrees. Using a scoop, portion the dough into 20-gram pieces. Roll the dough into 1 inch balls and toss in the sifted confectioner's sugar. Place on a parchment-lined cookie sheet and bake for 10 minutes. The tops of cookies will crack or crinkle. After 10 minutes, check the temperature, it should be between 175 F and 185 F. They will be soft and gooey, let cool completely on the baking sheet so they firm up.
6. Store in an airtight container. These keep really well and are kind of better the next day. For a bonus treat, try making an ice cream cookie sandwich with mint chocolate chip ice cream.
''',
    '''	1. Preheat oven to 375F and line a baking sheet with parchment paper.
2. Whisk together brown sugar, peanut butter, shortening, egg, milk, and vanilla until smooth and fluffy; set aside.
3. Stir together flour, baking soda, and salt.
4. Slowly add dry ingredients, mixing until just combined.
5. Form dough into ~1.5" balls.
6. Place on baking sheets 1.5" apart, very very slightly flatten with fork in criss-cross pattern, and bake for 8 minutes or until set and slightly browned.
7. Remove wrapping from chocolates.
8. Remove from baking shit and quickly press one piece of chocolate into each cookie, with slight twist.
9. Let rest for a 10 minutes before trying to move from baking sheet. Then, whether moved or not, let them cool completely.
''',
    '''	1. Cut skirt steak into 2-3 inch strips with the grain of the meat
2. Then cut inch long strips against the grain at a diagonal angle
3. Add beef to a bowl, then add soy sauce, sesame oil, corn starch, baking soda, and salt
4. Thoroughly mix ingredients together, being rough with the meat to tenderize it
5. Let marinade for 15 minutes
6. Cut stems of broccoli at an angle, every 2 inches from the bottom, until the florets separate from the stalk
    a. If the stems are especially thick, consider peeling the stems to thin them out
7. Half/quarter/etc. the florets at necessary to make them all the same size
8. Put broccoli in a microwave safe bowl, with a thin layer of water, and put in the microwave for 2-3 minutes
    a. The goal is to soften the broccoli a bit, not fully cook it
9. For the sauce, mix the two soy sauces, oyster sauce, and sugar together in a bowl
10. In a separate, small bowl, mix the water and corn starch to form a slurry
11. After meat has marinaded, pre heat your pan or wok on high heat and add some cooking oil
12. Add the beef to your bowl and spread it out, maximizing surface area
13. Flip and toss meat every 30 seconds or so
14. Once no pink is remaining, add garlic and ginger (optional) and continue stirring
15. Once beef is almost fully cooked, add sauce and mix it throughout the meat
16. Add broccoli and slurry and continue mixing together until broccoli is the desired texture
17. Plate and serve''',
    '''Make the sauce: In a bowl, combine all sauce ingredients and mix until smooth. Adjust acid and seasonings to taste.

Assemble wrap & serve: Spread 1/3 of the sauce onto a lavash bread. ****Next come in with 150 grams of chicken, sliced tomatoes, lettuce, and pickled onions. Lastly, crumble over 10 grams of feta cheese before wrapping that together.
I use aluminum foil so I can wrap it up tight, and make ready-to-go extras for later.

Notes & Variations
Feel free to add any other veggies, sauces, or extras into the wrap. You do you.
Possible Variations:
	1. Try a different protein to mix it up!
    2. Use different spices and flavor profiles in the marinade and yogurt sauce if desired.''',
]
Recipes = (
    'Teriyaki Chicken',
    'Meatballs',
    'Crunchwrap Supreme',
    'Pink Pickled Onions',
    'Simple Chicken Pan Sauce',
    'French Toast',
    'Christmas Crinkle Cookie',
    'Peanut Butter Blossoms',
    'Broccoli Beef',
    'Chicken Flatbread Wrap',)
new_data = [
	(1, 'Flautas', 'Classic Mexican Flautus', 'Entree', 'Mexican', 'Beans', 'Chiles', True, 10, 10, 3,0,0,0,0,f'{ingreds}',f'{directions}','/static/images/recipes/flautas.jpg','Adam Ragusea'),
	(2,f'{new_names[0]}',f'{new_desc[0]}','Entree','Japanese','Chicken','Ginger',False,10,15,3,0,0,0,0,f'{new_ingreds[0]}',f'{new_steps[0]}','/static/images/recipes/teriyaki_chicken.webp','https://www.bonappetit.com/recipe/teriyaki-chicken-recipe'),
	(3,f'{new_names[1]}',f'{new_desc[1]}','Entree','Italian','Beef','Panko',False,15,30,4,0,0,0,0,f'{new_ingreds[1]}',f'{new_steps[1]}','/static/images/recipes/meatballs.webp','https://www.bonappetit.com/recipe/meatball-recipe'),
	(4,f'{new_names[2]}',f'{new_desc[2]}','Entree','American','Beef','Cumin spice mix',False,20,15,2,0,0,0,0,f'{new_ingreds[2]}',f'{new_steps[2]}','/static/images/recipes/crunchwrap_supreme.jpg','https://www.ethanchlebowski.com/cooking-techniques-recipes/taco-bells-crunchwrap-supreme-at-home'),
	(5,f'{new_names[3]}',f'{new_desc[3]}','Side','Mexican','Onions','Vinegar',True,10,1440,5,0,0,0,0,f'{new_ingreds[3]}',f'{new_steps[3]}','','Adam Ragusea'),
	(6,f'{new_names[4]}',f'{new_desc[4]}','Sauce','','Chicken Stock','Shallot',False,10,5,3,0,0,0,0,f'{new_ingreds[4]}',f'{new_steps[4]}','',''),
	(7,f'{new_names[5]}',f'{new_desc[5]}','Breakfast','French','Bread','Eggs',False,20,5,3,0,0,0,0,f'{new_ingreds[5]}',f'{new_steps[5]}','/static/images/recipes/french_toast.webp','https://www.bonappetit.com/recipe/classic-french-toast'),
	(8,f'{new_names[6]}',f'{new_desc[6]}','Dessert','American','Chocolate','Powdered sugar',False,75,15,30,0,0,0,0,f'{new_ingreds[6]}',f'{new_steps[6]}','/static/images/recipes/crinkle_cookies.jpg','https://www.ethanchlebowski.com/cooking-techniques-recipes/my-favorite-christmas-cookie-the-christmas-crinkle'),
	(9,f'{new_names[7]}',f'{new_desc[7]}','Dessert','American','Peanut butter','Chocolate',False,15,10,30,0,0,0,0,f'{new_ingreds[7]}',f'{new_steps[7]}','','Mom'),
	(10,f'{new_names[8]}',f'{new_desc[8]}','Entree','Chinese','Beef','Broccoli',False,30,15,3,0,0,0,0,f'{new_ingreds[8]}',f'{new_steps[8]}','',''),
	(11,f'{new_names[9]}',f'{new_desc[9]}','Entree','American','Chicken','Yogurt',False,15,20,2,0,0,0,0,f'{new_ingreds[9]}',f'{new_steps[9]}','','https://www.ethanchlebowski.com/cooking-techniques-recipes/chicken-flatbread-wrap'),
]

cur.executemany("INSERT INTO RECIPE VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", new_data)
con.commit()

df = pd.read_sql_query("SELECT * FROM RECIPE", con)
df['name']
