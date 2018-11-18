======================NRM DB data specification====================== 

recipe_doc ={
                "id":recipe.id, 
                "name":recipe.name, 
                "chef":recipe.chef,
                "menu":recipe.menu, 
                "steps":recipe.steps
                "ingredients" :recipe.ingredients
            }

recipe.id: int 
recipe.name : string 
recipe.chef : string
recipe.menu : string
recipe.steps : [string, string, ... ]
recipe.ingredients : [string, string, ...]
