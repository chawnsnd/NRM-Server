#!/usr/bin/env python3
import numpy as np
import json
import matplotlib.pyplot 
from random import randint
from dao.recipeDao import *

#use recipeDao only
def recommendMenu():
    RecipesInDB = query_recipes_all()
    print(RecipesInDB)
    recommended = RecipesInDB[randint(0,len(RecipesInDB)-1)]
    return recommended['menu']


def recommendRecipe():
    RecipesInDB = query_recipes_all()
    recommendedRecipe = RecipesInDB[randint(0,len(RecipesInDB)-1)]
    return recommendedRecipe['name']

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
    
