#!/usr/bin/env python3
import numpy as np
import json
from random import randint
from dao.recipeDao import *

#use recipeDao only

def recommendRecipe():
    RecipesInDB = query_recipes_all()
    recommendedRecipe = RecipesInDB[randint(0,len(RecipesInDB)-1)]
    return recommendedRecipe


def numberStepByMenu(recipeMenu,stepNo):
    recipe = query_recipe_with_menu(recipeMenu)
    if stepNo <0 or stepNo >= len(recipe):
        return False , 0
    step = recipe['steps'][stepNo]
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

def getRecipeByMenuAndChef(recipeMenu, chef):
    recipe = query_recipe_with_menu_and_chef(recipeMenu,chef)
    if recipe is None:
        return False
    return recipe