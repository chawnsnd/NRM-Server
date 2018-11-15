
mostly DB 

======================menu specification====================== 

menu_doc =  {"Id":menu.id, "Name":menu.name , "Chefs":menu.chefs}
menu.id : int 
menu.name : string
menu.chefs : [string, string, ...]

======================recipe specification====================== 

recipe_doc = {"Id":recipe.id, "Name":recipe.name, "Chefs":recipe.chefs, "steps":steps, "Recipe": recipe.recipe}

recipe.id: int 
recipe.name : string 
recipe.chefs : [string, string, ...]
recipe.recipe : [string, string, ... ]
recipe.steps : int 


======================user specification======================
user_doc = {"Id":user.id, "Name":user.name, "currentStep":user.step, "recipe":user.recipeID}

user.id : int
user.name :string
user.step : int
user.recipeID : string

======================question======================

for chef in chefs. A chef must have (menu, recipe) at once 

do we have to make chef collection ?? 
for example)

chef_doc = {"Id":chef.id, "Name":chef.name, "Steps":steps, "RecipeMenu":chef.recipeMenu}

chef.id: int 
chef.name : string 
chef.steps : int 
chef.recipeMenu : [(string,string), (string,string), ... ]





