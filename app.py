from flask import Flask, request, jsonify, Response
from service.recipeService import *
from dao.recipeDao import *
from route.menu import *

app = Flask(__name__)
session ={}

def checkMenuExist():
    if 'menuName' in session:
        menuExist = "true"
    else:
        menuExist = "false"
    return menuExist

#0. 심사를 위한 health
@app.route("/health", methods=["GET"])
def health():
    return Response("OK", status=200)

#1. 메뉴추천
@app.route("/answerMenuRecommendation", methods=["POST"])
def answerMenuRecommendation():
    recipe = recommendRecipe()
    session['menuName'] = recipe['menu']
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "menuNameWhenAnswerMenu":session['menuName']
        }
    }
    return jsonify(res)

#2. 레시피추천
#2.1. 키워드 있을 때
#2.1.1. 메뉴 키워드
@app.route("/answerRecipeByMenu", methods=["POST"])
def answerRecipeByMenu():
    req = request.json
    menuName = req['action']['parameters']['menuNameWhenAnswerRecipe']['value']
    recipe = getRecipeByMenu(menuName) #이거 만들어야 됨
    session['recipeName'] = recipe['name']
    session['chefName'] = recipe['chef']
    session['menuName'] = menuName
    session['step'] = recipe['steps'][0]
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "recipeNameWhenAnswerRecipe": session['recipeName'],
            "stepWhenAnswerRecipe": session['step']
        }
    }
    return jsonify(res)

#2.1.2. 셰프키워드
@app.route("/answerRecipeByChef", methods=["POST"])
def answerRecipeByChef():
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "booleanMenuExistWhenAnswerRecipe": checkMenuExist(),
        }
    }
    return jsonify(res)
#2.1.2.1. 서버에 메뉴 있을 때
@app.route("/answerRecipeByChefIfServerMenuExist", methods=["POST"])
def answerRecipeByChefIfServerMenuExist():
    req = request.json
    chefName = req['action']['parameters']['chefNameWhenAnswerRecipe']['value']
    menuName = session['menuName']
    recipe = getRecipeByMenuAndChef(menuName, chefName)
    session['recipeName'] = recipe['name']
    session['chefName'] = recipe['chef']
    session['menuName'] = recipe['menu']
    session['step'] = recipe['steps'][0]
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "recipeNameWhenAnswerRecipe": session['recipeName'],
            "stepWhenAnswerRecipe": session['step']
        }
    }
    return jsonify(res)
#2.1.2.2. 서버에 메뉴 없을 때
@app.route("/answerRecipeByChefIfServerMenuNone", methods=["POST"])
def answerRecipeByChefIfServerMenuNone():
    req = request.json
    chefName = req['action']['parameters']['chefNameWhenAnswerRecipe']['value']
    recipe = getRandomRecipeByChef(chefName)
    session['recipeName'] = recipe['name']
    session['chefName'] = recipe['chef']
    session['menuName'] = recipe['menu']
    session['step'] = recipe['steps'][0]
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "recipeNameWhenAnswerRecipe": session['recipeName'],
            "stepWhenAnswerRecipe": session['step']
        }
    }
    return jsonify(res)
#2.1.3. 메뉴&셰프키워드
@app.route("/answerRecipeByMenuAndChef", methods=["POST"])
def answerRecipeByMenuAndChef():
    req = request.json
    chefName = req['action']['parameters']['chefNameWhenAnswerRecipe']['value']
    menuName = req['action']['parameters']['menuNameWhenAnswerRecipe']['value']
    recipe = getRecipeByMenuAndChef(menuName, chefName)
    session['recipeName'] = recipe['name']
    session['chefName'] = recipe['chef']
    session['menuName'] = recipe['menu']
    session['step'] = recipe['steps'][0]
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "recipeNameWhenAnswerRecipe": session['recipeName'],
            "stepWhenAnswerRecipe": session['step']
        }
    }
    return jsonify(res)
#2.1. 키워드 없을 때
@app.route("/answerRecipeWithoutKeyWord", methods=["POST"])
def answerRecipeWithoutKeyWord():
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "booleanMenuExistWhenAnswerRecipe": checkMenuExist(),
        }
    }
    return jsonify(res)
#2.1.1. 서버에 메뉴 있을 때
@app.route("/answerRecipeIfServerMenuExists", methods=["POST"])
def answerRecipeIfServerMenuExists():
    menuName = session['menuName']
    recipe = getRandomRecipeByMenu(menuName)
    session['recipeName'] = recipe['name']
    session['chefName'] = recipe['chef']
    session['menuName'] = recipe['menu']
    session['step'] = recipe['steps'][0]
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "recipeNameWhenAnswerRecipe": session['recipeName'],
            "stepWhenAnswerRecipe": session['step']
        }
    }
    return jsonify(res)
#2.1.2. 서버에 메뉴 없을 때
@app.route("/answerRecipeIfServerMenuNone", methods=["POST"])
def answerRecipeIfServerMenuNone():
    recipe = recommendRecipe()
    session['recipeName'] = recipe['name']
    session['chefName'] = recipe['chef']
    session['menuName'] = recipe['menu']
    session['step'] = recipe['steps'][0]
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "recipeNameWhenAnswerRecipe": session['recipeName'],
            "stepWhenAnswerRecipe": session['step']
        }
    }
    return jsonify(res)

#3. 재료안내
#3.1. 키워드가 없을 때
@app.route("/answerIngredientsWithoutKeyWord", methods=["POST"])
def answerIngredient():
    if 'recipeName' in session:
        res = {
            "version": "1.0",
            "resultCode": "OK",
            "output": {"sessionState": "recipeExists"}
        }
    elif 'menuName' in session:
        res = {
            "version": "1.0",
            "resultCode": "OK",
            "output": {"sessionState": "menuExists"}
        }
    else:
        res = {
            "version": "1.0",
            "resultCode": "OK",
            "output": {"sessionState": "none"}
        }
    return jsonify(res)
    # return "서버 세션에 재료나 레시피가 있는지?"
#3.1.1. 서버에 메뉴까지 있을 때
@app.route("/answerIngredientsIfServerMenuExists", methods=["POST"])
def answerIngredientsIfServerMenuExists():
    menuName = session['menuName']
    recipe = getRandomRecipeByMenu(menuName)
    session['recipeName'] = recipe['name']
    session['chefName'] = recipe['chef']
    session['menuName'] = recipe['menu']
    ingredients = " ".join(str(x) for x in recipe['ingredients'])
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "ingredientsIfServerMenuExists" : ingredients
        }
    }
    return jsonify(res)
#3.1.2. 서버에 레시피까지 있을 때
@app.route("/answerIngredientsIfServerRecipeExists", methods=["POST"])
def answerIngredientsIfServerRecipeExists():
    recipeName = session['recipeName']
    recipe = getRecipeByRecipe(recipeName)
    session['recipeName'] = recipe['name']
    session['chefName'] = recipe['chef']
    session['menuName'] = recipe['menu']
    ingredients = " ".join(str(x) for x in recipe['ingredients'])
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "ingredientsIfServerRecipeExists" : ingredients
        }
    }
    return jsonify(res)
#3.2. 키워드가 있을 때
#3.2.1. 키워드가 레시피일 때
@app.route("/answerIngredientsByRecipe", methods=["POST"])
def answerIngredientsByRecipe():
    return "키워드로 받은 레시피의 재료//준비중인 기능??"
#3.2.2. 키워드가 메뉴일 때
@app.route("/answerIngredientsByMenu", methods=["POST"])
def answerIngredientsByMenu():
    req = request.json
    menuName = req['action']['parameters']['menuNameWhenAnswerIngredient']['value']
    recipe = getRandomRecipeByMenu(menuName)
    session['recipeName'] = recipe['name']
    session['chefName'] = recipe['chef']
    session['menuName'] = recipe['menu']
    ingredients = " ".join(str(x) for x in recipe['ingredients'])
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "ingredientsWhenMenuExists" : ingredients
        }
    }
    return jsonify(res)


# #4. 스텝이동
# @app.route("/answerNextStep", methods=["POST"])
# def answerNextStep():
#     req = request.json
#     if 'recipe' not in session:
#         res = {
#             "version": "1.0",
#             "resultCode": "BAD"
#         }
#     else:
#         recipe = session['recipe']
#         if 'state' not in req['action']['parameters'] and 'stepNo' in req['action']['parameters']:
#             stepNo = req['action']['parameters']['stepNo']['value']
#             session['stepNo'] = stepNo
#             recipeStep = recipe.step[stepNo]
#             res = {
#                 "version": "1.0",
#                 "resultCode": "OK",
#                 "output": {
#                     "recipeStep": recipeStep,
#                     "stepNo": stepNo 
#                 }
#             }
#         elif 'state' in req['action']['parameters'] and 'stepNo' not in req['action']['parameters']:
#                 state = req['action']['parameters']['state']['value']
#                 curStepNo = session['stepNo']+state
#                 recipeStep = recipe.step[curStepNo]
#                 session['stepNo'] = curStepNo
#                 res = {
#                     "version": "1.0",
#                     "resultCode": "OK",
#                     "output": {
#                         "recipeStep": recipeStep,
#                         "stepNo": stepNo,
#                         "state": state 
#                     }
#                 }
#     return jsonify(res)

#5. 좋아요 싫어요는 서버에서 할게 아니지?

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host='ec2-13-125-180-243.ap-northeast-2.compute.amazonaws.com',port=5000)
    # app.run(port=5000)