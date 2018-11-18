#!/usr/bin/env python3
import numpy as np
import json
import matplotlib.pyplot 
from random import randint
from dao.recipeDao import query_menu,query_recipe, query_recipes_all

#use recipeDao only
def recommendMenu():
    RecipesInDB = query_recipes_all()
    recommended = RecipesInDB[randint(0,len(RecipesInDB)-1)]
    return recommended['menu']


def recommendRecipe():
    RecipesInDB = query_recipes_all()
    recommendedRecipe = RecipesInDB[randint(0,len(RecipesInDB)-1)]
    return recommendedRecipe['name']

def nextStep(recipeId,stepNo):
    recipe = query_recipe(recipeId)
    recipeSize = len(recipe)
    stepNo+=1
    if stepNo >=recipeSize:
        return False , 0
    step = recipe[stepNo]
    return step , stepNo

def previousStep(recipeId,stepNo):
    recipe = query_recipe(recipeId)
    stepNo-=1
    if stepNo < 0:
        return False , 0
    step = recipe[stepNo]
    return step , stepNo

def numberStep(recipeId,stepNo):
    recipe = query_recipe(recipeId)
    if stepNo <0 or stepNo >= len(recipe):
        return False
    step = recipe[stepNo]
    return step , stepNo
