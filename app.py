from flask import Flask, request, jsonify, Response, session
from service.recipeService import *
from dao.recipeDao import *

app = Flask(__name__)

#0. 심사를 위한 health
@app.route("/health", methods=["GET"])
def health():
    return Response("OK", status=200)

#1. 메뉴추천
@app.route("/answerMenuRecommendation", methods=["POST"])
def answerMenuRecommendation():
    req = request.json
    menu = recommendMenu()
    session['menu'] = menu
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "menuName": menu
        }
    }
    return jsonify(res)
    
#2. 레시피 추천
@app.route("/answerRecipe", methods=["POST"])
def answerRecipe():
    req = request.json
    if 'MENU' not in req['action']['parameters'] and 'CHEF' not in req['action']['parameters']:
        if 'menu' in session:
            menu = session['menu']
            recipe = query_recipe_with_menu(menu) #이거 만들어야 됨
            res = {
                "version": "1.0",
                "resultCode": "OK",
                "output": {
                    "recipeName": recipe
                }
            }
        else:
            recipe = recommendRecipe()
            res = {
                "version": "1.0",
                "resultCode": "OK",
                "output": {
                    "recipeName": recipe
                }
            }
    elif 'CHEF' in req['action']['parameters']:
        chef = req['action']['parameters']['CHEF']['value']
        recipe = query_recipe_with_chef(chef); #이거 만들어야 됨
        res = {
            "version": "1.0",
            "resultCode": "OK",
            "output": {
                "CHEF": chef,
                "recipeName": recipe
            }
        }
    elif 'MENU' in req['action']['parameters']:
        menu = req['action']['parameters']['MENU']['value']
        recipe = query_recipe_with_menu(menu); #이거 만들어야 됨
        res = {
            "version": "1.0",
            "resultCode": "OK",
            "output": {
                "MENU": menu,
                "recipeName": recipe
            }
        }
    session['recipe'] = recipe
    return jsonify(res)

#3. 재료묻기
@app.route("/answerIngredients", methods=["POST"])
def answerIngredients():
    req = request.json
    if 'MENU' not in req['action']['parameters']:
        if 'menu' not in session:
            res = {
                "version": "1.0",
                "resultCode": "BAD"
            }
        else:
            menu = session['menu']
            recipe = recommendRecipeByMenu(menu) #이거 만들어야 됨
            session['recipe'] = recipe
            ingredients = recipe.ingredients
            res = {
                "version": "1.0",
                "resultCode": "OK",
                "output": {
                    "menu": menu,
                    "ingredients": recipe
                }
            }
    else:
        menu = req['action']['parameters']['MENU']['value']
        recipe = recommendRecipeByMenu(menu) #이거 만들어야 됨
        ingredients = recipe.ingredients
        res = {
            "version": "1.0",
            "resultCode": "OK",
            "output": {
                "menu": menu,
                "ingredients": recipe
            }
        }
    return jsonify(res)

#4. 스텝이동
@app.route("/answerNextStep", methods=["POST"])
def answerNextStep():
    req = request.json
    if 'recipe' not in session:
        res = {
            "version": "1.0",
            "resultCode": "BAD"
        }
    else:
        recipe = session['recipe']
        if 'state' not in req['action']['parameters'] and 'stepNo' in req['action']['parameters']:
            stepNo = req['action']['parameters']['stepNo']['value']
            session['stepNo'] = stepNo
            recipeStep = recipe.step[stepNo]
            res = {
                "version": "1.0",
                "resultCode": "OK",
                "output": {
                    "recipeStep": recipeStep,
                    "stepNo": stepNo 
                }
            }
        elif 'state' in req['action']['parameters'] and 'stepNo' not in req['action']['parameters']:
                state = req['action']['parameters']['state']['value']
                curStepNo = session['stepNo']+state
                recipeStep = recipe.step[curStepNo]
                session['stepNo'] = curStepNo
                res = {
                    "version": "1.0",
                    "resultCode": "OK",
                    "output": {
                        "recipeStep": recipeStep,
                        "stepNo": stepNo,
                        "state": state 
                    }
                }
    return jsonify(res);

#5. 좋아요 싫어요는 서버에서 할게 아니지?

if __name__ == '__main__':
    # app.run(host='ec2-13-125-180-243.ap-northeast-2.compute.amazonaws.com',port=5000)
    app.run(port=5000)

# #셰프명으로 레시피 랜덤추천
# @app.route("/recommendRecipeByChef", methods=["POST"])
# def recommendRecipeByChef():
#     req = request.json
#     chef = req['action']['parameters']['chef']['value']
#     result = {
#         "recipeId": tmpRecipe["id"],
#         "name": tmpRecipe["name"]
#         }
#     return jsonify(result);

# #레시피에서스텝찾기
# @app.route("/answerStepFromRecipeByStepNo", methods=["POST"])
# def answerStepFromRecipeByStepNo():
#     req = request.json
#     # step = req['action']['parameters']['step']['value']
#     step = 3;
#     result = {
#         "recipeId": tmpRecipe["id"],
#         "step": tmpRecipe["steps"][step],
#         "stepNo": step
#         }
#     return jsonify(result);

# #레시피에서재료찾기
# @app.route("/answerFromIngredientsFromRecipe", methods=["POST"])
# def answerFromIngredientsFromRecipe():
#     req = request.json
#     # recipe = req['action']['parameters']['recipe']['value']
#     result = {
#         "recipeId": tmpRecipe["id"],
#         "ingredients": tmpRecipe["ingredients"]
#         }
#     return jsonify(result);
