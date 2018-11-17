#!/usr/bin/env python3
import numpy as np
import json
import matplotlib.pyplot 
from random import randint
from dao.recipeDao import query_menu,query_recipe, query_recipe_step, query_recipes

#use recipeDao only
def recommendMenu():
    RecipesInDB = query_recipes('all')
    recommended = RecipesInDB[randint(0,len(RecipesInDB))]
    return recommended['menu']


def recommendRecipe():
    RecipesInDB = query_recipe
    recommendedRecipe = RecipesInDB
    return recommendedRecipe

def nextStep(recipeId,stepNo):
    recipe = query_recipe_step(recipeId)
    step = recipe[stepNo]
    stepNo+=1
    if stepNo >=len(recipe):
        stepNo = 0
    return step , stepNo
