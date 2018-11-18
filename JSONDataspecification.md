======================NRM DB data specification====================== 

recipe_doc ={
                "Id":recipe.id, 
                "Name":recipe.name, 
                "Chef":recipe.chef,
                "Menu":recipe.menu, 
                "steps":recipe.steps
            }

recipe.id: int 
recipe.name : string 
recipe.chef : string
recipe.menu : string
recipe.steps : [string, string, ... ]
