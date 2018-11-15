#!/usr/bin/env python3.6

# WS server example that synchronizes state across clients

import asyncio
import json
import logging
import websockets
import pymongo
import sys
from bson.json_util import dumps
from algorithmModule import recommendMenu, recommendRecipe
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["NRMDB"]
MenuCol = mydb["TestMenuCollection"]
RecipeCol = mydb["TestRecipeCollection"]


def insert_menus(menus):
    global MenuCol
    
    if menus is None:
        print("Failed (no menu)")
        return dumps({"type":"insert_menus","response":"insertion/update fail"})

    for menu in menus:
        criteria = {"id":menus['id']}
        setChefs= {"$set" : {"chefs":menu['chefs']}}
        addChefs = {"$push": {"chefs":{"$each":menu['chefs']}}}
        menu_doc = MenuCol.find_one(criteria)
        
        #check chefs if exists
        if menu_doc:
            #update chefs
            if not 'chefs' in menu_doc:
                MenuCol.update_one(criteria,setChefs,True)
                continue
            if menu['chefs'] is None: 
                MenuCol.update_one(criteria,setChefs,True)
            else:
                #skip if all elements in chefs are in menu , update all if not
                if all(chef in menu['chefs'] for chef in menu_doc['chefs']):
                    continue
                MenuCol.update_one(criteria,addChefs)
            continue
        
        MenuCol.insert(menu)

    return dumps({"type": "insert_menus", "response": "insertion/update success"})


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
        
        RecipeCol.insert(recipe)

    return dumps({"type": "insert_menus", "response": "insertion/update success"})


def query_menus(keyWord):
    return dumps({"type": "query_menus", "response": "menus~"})


def query_recipes(keyWord):
    return dumps({"type": "query_recipes", "response": "recipes~"})


def query_menu(id):
    global MenuCol
    query = {"id": id}
    menu = MenuCol.find(query).limit(1)
    return dumps({"type": "query_menu", "response": menu})

def query_recipe(id):
    global RecipeCol
    query = {"id": id}
    recipe = RecipeCol.find(query).limit(1)
    return dumps({"type": "query_recipe", "response": recipe})


def recommend_api(data,keyWord):
    recommendation =""
    if keyWord == "menu":
        recommendation = recommendMenu(data['menu'])
    else:
        recommendation = recommendRecipe(data['recipe'])
    return recommendation
