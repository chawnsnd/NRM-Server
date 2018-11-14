#!/usr/bin/env python3.6

# WS server example that synchronizes state across clients

import asyncio
import json
import logging
import websockets
import pymongo
import sys
from bson.json_util import dumps
from component.apis import *

logging.basicConfig()

STATE = {'value': 0}
LONLAT = {'a_lonlat': None, 'b_lonlat': None}
USERS = set()

# START DB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["NRMDB"]
mycol = mydb["TestMenuCollection"]


# CHECK DB CONNECTION
dblist = myclient.list_database_names()
if "NRMDB" in dblist:
    print("NRMDB connected")
else:
    print("NO DATABASE")


# SAMPLE CODE
# print(myclient.list_database_names())
# collist = mydb.list_collection_names()
# print(mycol.find_one())

async def notify_state(message):
    if USERS:       # asyncio.wait doesn't accept an empty list
        await asyncio.wait([user.send(message) for user in USERS])

async def register(websocket):
    print("Client Connected")
    USERS.add(websocket)

async def unregister(websocket):
    print("Client disconnected")
    USERS.remove(websocket)

async def serve_api(websocket, path):
    global mycol
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        # await websocket.send(query_square_bound())
        async for message in websocket:
            data = json.loads(message)
            #do command
            command = data['command']
            if command == "connect()":
                print("Client Connected")
            elif command == "insert_menus":
                await notify_state("menusinsert")
            elif command =="insert_recipes":
                await notify_state("recipesinsert")
            elif command == "query_menus":
                await notify_state("menusquery")
            elif command =="query_recipes":
                await notify_state("recipesquery")
    finally:
        await unregister(websocket)

asyncio.get_event_loop().run_until_complete(websockets.serve(serve_api, 'localhost', 49152))
asyncio.get_event_loop().run_forever()
