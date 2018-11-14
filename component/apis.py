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
    MenuCol.insert({menus})
    return dumps({"type": "insert_menus", "response": "insertion/update success"})


def insert_recipes(recipes):
    global RecipeCol
    RecipeCol.insert({recipes})
    return dumps({"type": "insert_recipes", "response": "insertion/update success"})


def query_menus(keyWord):

    return dumps({"type": "query_menus", "response": "menus~"})


def query_recipes(keyWord):
    return dumps({"type": "query_recipes", "response": "recipes~"})


def query_menu(id):
    global MenuCol
    query = {"id": id}
    menu = MenuCol.find(query).limit(1)
    return dumps({"type": "query_menu", "response": menu})


def recommend_api(data,keyWord):
    recommendation =""
    if keyWord == "menu":
        recommendation = recommendMenu(data['menu'])
    else:
        recommendation = recommendRecipe(data['recipe'])
    return recommendation
