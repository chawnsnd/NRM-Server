#!/usr/bin/env python3.6

# WS server example that synchronizes state across clients

import asyncio
import json
import logging
import websockets
import pymongo
import sys
from bson.json_util import dumps
from service.recipeService import recommendMenu, recommendRecipe
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["NRMDB"]
RecipeCol = mydb["TestRecipeCollection"]


def insert_recipes(recipes):
    global RecipeCol
    
    if recipes is None:
        print("Failed (no recipe)")
        return dumps({"type":"insert_recipes","response":"insertion/update fail"})

    for recipe in recipes:
        criteria = {"id":recipes['id']}
        setChefs= {"$set" : {"chefs":recipe['chefs']}}
        addChefs = {"$push": {"chefs":{"$each":recipe['chefs']}}}
        recipe_doc = RecipeCol.find_one(criteria)
        
        #check chefs if exists
        if recipe_doc:
            #update chefs
            if not 'chefs' in recipe_doc:
                RecipeCol.update_one(criteria,setChefs,True)
                continue
            if recipe['chefs'] is None: 
                RecipeCol.update_one(criteria,setChefs,True)
            else:
                #skip if all elements in chefs are in recipe , update all if not
                if all(chef in recipe['chefs'] for chef in recipe_doc['chefs']):
                    continue
                RecipeCol.update_one(criteria,addChefs)
            continue

    return RecipeCol.insert(recipe) 


def query_menus(keyWord):
    
    return RecipeCol.find({"name":keyWord}).limit(1)


def query_menu(id):
    global RecipeCol
    query = {"id": id}
    return RecipeCol.find(query).limit(1)[0]['menu']

def query_recipe(id):
    global RecipeCol
    query = {"id": id}
    return RecipeCol.find(query).limit(1)[0]['steps']


def recommend_api(data,keyWord):
    recommendation =""
    if keyWord == "menu":
        recommendation = recommendMenu(data['menu'])
    else:
        recommendation = recommendRecipe(data['recipe'])
    return recommendation
