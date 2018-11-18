#!/usr/bin/env python3.6

# WS server example that synchronizes state across clients

import asyncio
import json
import logging
import websockets
import pymongo
import sys
from bson.json_util import dumps
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["NRMDB"]
RecipeCol = mydb["TestRecipeCollection"]


def insert_recipes(recipes):
    global RecipeCol
    
    if recipes is None:
        print("Failed (no recipe)")
        return False

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
        RecipeCol.insert(recipe) 
    return True


def query_menu(id):
    global RecipeCol
    query = {"id": id}
    result = RecipeCol.find(query).limit(1)[0]['menu']
    return result

def query_recipe_step_no(id,stepNo):
    global RecipeCol
    query = {"id": id}
    result = RecipeCol.find(query).limit(1)[0]['steps'][stepNo]
    return result

def query_recipe(id):
    global RecipeCol
    query = {"id": id}
    result = RecipeCol.find(query).limit(1)[0]['steps']
    return result

def query_recipes_all():
    global RecipeCol
    result = list(RecipeCol.find({}))
    return result