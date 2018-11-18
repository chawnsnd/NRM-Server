======================service API specification====================== 

#use recipeDao only
def recommendMenu(): 메뉴 추천 
    param : null
    res : menu  {{string}}

def recommendRecipe():
    param : null
    res : recipeName {{string}}

def nextStep(recipeId,stepNo):
    param : recipeId {{int}},stepNo{{int}}
    res : recipeStep {{string}}, stepNo {{int}}

def previousStep(recipeId,stepNo):
    param : recipeId {{int}},stepNo{{int}}
    res : recipeStep {{string}}, stepNo {{int}}
    
def numberStep(recipeId,stepNo):
    param : recipeId {{int}},stepNo{{int}}
    res : recipeStep {{string}}, stepNo {{int}}