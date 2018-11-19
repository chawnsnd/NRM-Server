#!/usr/bin/env python3
import numpy as np
import json
# import matplotlib.pyplot 
from random import randint
from dao.recipeDao import *

#use recipeDao only
def recommendMenu():
    RecipesInDB = query_recipes_all()
    print(RecipesInDB)
    recommended = RecipesInDB[randint(0,len(RecipesInDB)-1)]
    return recommended['menu']

def recommendRecipeName():
    RecipesInDB = query_recipes_all()
    recommendedRecipe = RecipesInDB[randint(0,len(RecipesInDB)-1)]
    return recommendedRecipe['name']

def recommendRecipe():
    RecipesInDB = query_recipes_all()
    recommendedRecipe = RecipesInDB[randint(0,len(RecipesInDB)-1)]
    return recommendedRecipe

def nextStepById(recipeId,stepNo):
    recipe = query_recipe_with_id(recipeId)
    recipeSize = len(recipe)
    stepNo+=1
    if stepNo >=recipeSize:
        return False , 0
    step = recipe[stepNo]
    return step , stepNo

def previousStepById(recipeId,stepNo):
    recipe = query_recipe_with_id(recipeId)
    stepNo-=1
    if stepNo < 0:
        return False , 0
    step = recipe[stepNo]
    return step , stepNo

def numberStepById(recipeId,stepNo):
    recipe = query_recipe_with_id(recipeId)
    if stepNo <0 or stepNo >= len(recipe):
        return False , 0
    step = recipe[stepNo]
    return step , stepNo

def getIngredientsById(recipeId):
    ingredients = query_ingredients_with_id(recipeId)
    if ingredients is None:
        return False
    return ingredients


def numberStepByMenu(recipeMenu,stepNo):
    recipe = query_recipe_with_menu(recipeMenu)
    if stepNo <0 or stepNo >= len(recipe):
        return False , 0
    step = recipe[stepNo]
    return step , stepNo

def getIngredientsByMenu(recipeMenu):
    ingredients = query_ingredients_with_menu(recipeMenu)
    if ingredients is None:
        return False
    return ingredients

def getRecipeNameByMenu(recipeMenu):
    recipeName = query_recipeName_with_menu(recipeMenu)
    if recipeName is None:
        return False
    return recipeName

def getRecipeNameByChef(recipeChef):
    recipeName = query_recipeName_with_chef(recipeChef)
    if recipeName is None:
        return False
    return recipeName

def getRecipeNameByMenuAndChef(recipeMenu, chef):
    recipeName = query_recipeName_with_menu_and_chef(recipeMenu,chef)
    if recipeName is None:
        return False
    return recipeName

def getRecipeByMenu(recipeMenu):
    recipe = query_recipe_with_menu(recipeMenu)
    if recipe is None:
        return False
    return recipe

def getRecipeByChef(recipeChef):
    recipe = query_recipe_with_chef(recipeChef)
    if recipe is None:
        return False
    return recipe

def getRandomRecipeByChef(recipeChef):
    recipes = list(query_recipes_with_chef(recipeChef))
    if recipes is None:
        return False
    recipe = recipes[randint(0,len(recipes)-1)]
    return recipe

def getRecipeByMenuAndChef(recipeMenu, chef):
    recipe = query_recipe_with_menu_and_chef(recipeMenu,chef)
    if recipe is None:
        return False
    return recipe