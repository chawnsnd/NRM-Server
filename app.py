from flask import Flask, request, jsonify, Response
from service.recipeService import *
from dao.recipeDao import *
import os

app = Flask(__name__)

session = {}
sessionId = ""

def checkMenuExist():
    if 'menuName' in session:
        menuExist = "true"
    else:
        menuExist = "false"
    return menuExist

def checkRecipeExist():
    if 'recipeName' in session:
        recipeExist = "true"
    else:
        recipeExist = "false"
    return recipeExist

def checkStepExist():
    if 'step' in session:
        stepExist = "true"
    else:
        stepExist = "false"
    return stepExist

#세션유지되는지?
@app.before_request
def before_request():
    isNew = request.json['context']['session']['isNew']
    if isNew is True:
        session[sessionId] = {}

#0. 심사를 위한 health
@app.route("/health", methods=["GET"])
def health():
    sessionId = request.json['context']['session']['id']
    return Response("OK", status=200)

#1. 메뉴추천
@app.route("/answerMenuRecommendation", methods=["POST"])
def answerMenuRecommendation():
    sessionId = request.json['context']['session']['id']
    recipe = recommendRecipe()
    session[sessionId]['menuName'] = recipe['menu']
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "menuNameWhenAnswerMenu":session[sessionId]['menuName']
        }
    }
    return jsonify(res)

#2. 레시피추천
#2.1. 키워드 있을 때
#2.1.1. 메뉴 키워드
@app.route("/answerRecipeByMenu", methods=["POST"])
def answerRecipeByMenu():
    sessionId = request.json['context']['session']['id']
    req = request.json
    menuName = req['action']['parameters']['menuNameWhenAnswerRecipe']['value']
    recipe = getRecipeByMenu(menuName) #이거 만들어야 됨
    session[sessionId]['recipeName'] = recipe['name']
    session[sessionId]['chefName'] = recipe['chef']
    session[sessionId]['menuName'] = menuName
    session[sessionId]['step'] = recipe['steps'][0]
    session[sessionId]['stepNo'] = 0
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "recipeNameWhenAnswerRecipe": session[sessionId]['recipeName'],
            "stepWhenAnswerRecipe": session[sessionId]['step'],
            "stepNoWhenAnswerRecipe": session[sessionId]['stepNo']
        }
    }
    return jsonify(res)
#2.1.2. 셰프키워드
@app.route("/answerRecipeByChef", methods=["POST"])
def answerRecipeByChef():
    sessionId = request.json['context']['session']['id']
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
    sessionId = request.json['context']['session']['id']
    req = request.json
    chefName = req['action']['parameters']['chefNameWhenAnswerRecipe']['value']
    menuName = session[sessionId]['menuName']
    recipe = getRecipeByMenuAndChef(menuName, chefName)
    session[sessionId]['recipeName'] = recipe['name']
    session[sessionId]['chefName'] = recipe['chef']
    session[sessionId]['menuName'] = recipe['menu']
    session[sessionId]['step'] = recipe['steps'][0]
    session[sessionId]['stepNo'] = 0
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "recipeNameWhenAnswerRecipe": session[sessionId]['recipeName'],
            "stepWhenAnswerRecipe": session[sessionId]['step'],
            "stepNoWhenAnswerRecipe": session[sessionId]['stepNo']
        }
    }
    return jsonify(res)
#2.1.2.2. 서버에 메뉴 없을 때
@app.route("/answerRecipeByChefIfServerMenuNone", methods=["POST"])
def answerRecipeByChefIfServerMenuNone():
    sessionId = request.json['context']['session']['id']
    req = request.json
    chefName = req['action']['parameters']['chefNameWhenAnswerRecipe']['value']
    recipe = getRandomRecipeByChef(chefName)
    session[sessionId]['recipeName'] = recipe['name']
    session[sessionId]['chefName'] = recipe['chef']
    session[sessionId]['menuName'] = recipe['menu']
    session[sessionId]['step'] = recipe['steps'][0]
    session[sessionId]['stepNo'] = 0
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "recipeNameWhenAnswerRecipe": session[sessionId]['recipeName'],
            "stepWhenAnswerRecipe": session[sessionId]['step'],
            "stepNoWhenAnswerRecipe": session[sessionId]['stepNo']
        }
    }
    return jsonify(res)
#2.1.3. 메뉴&셰프키워드
@app.route("/answerRecipeByMenuAndChef", methods=["POST"])
def answerRecipeByMenuAndChef():
    sessionId = request.json['context']['session']['id']
    req = request.json
    chefName = req['action']['parameters']['chefNameWhenAnswerRecipe']['value']
    menuName = req['action']['parameters']['menuNameWhenAnswerRecipe']['value']
    recipe = getRecipeByMenuAndChef(menuName, chefName)
    session[sessionId]['recipeName'] = recipe['name']
    session[sessionId]['chefName'] = recipe['chef']
    session[sessionId]['menuName'] = recipe['menu']
    session[sessionId]['step'] = recipe['steps'][0]
    session[sessionId]['stepNo'] = 0
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "recipeNameWhenAnswerRecipe": session[sessionId]['recipeName'],
            "stepWhenAnswerRecipe": session[sessionId]['step'],
            "stepNoWhenAnswerRecipe": session[sessionId]['stepNo']
        }
    }
    return jsonify(res)
#2.1. 키워드 없을 때
@app.route("/answerRecipeWithoutKeyWord", methods=["POST"])
def answerRecipeWithoutKeyWord():
    sessionId = request.json['context']['session']['id']
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
    sessionId = request.json['context']['session']['id']
    menuName = session[sessionId]['menuName']
    recipe = getRandomRecipeByMenu(menuName)
    session[sessionId]['recipeName'] = recipe['name']
    session[sessionId]['chefName'] = recipe['chef']
    session[sessionId]['menuName'] = recipe['menu']
    session[sessionId]['step'] = recipe['steps'][0]
    session[sessionId]['stepNo'] = 0
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "recipeNameWhenAnswerRecipe": session[sessionId]['recipeName'],
            "stepWhenAnswerRecipe": session[sessionId]['step'],
            "stepNoWhenAnswerRecipe": session[sessionId]['stepNo']
        }
    }
    return jsonify(res)
#2.1.2. 서버에 메뉴 없을 때
@app.route("/answerRecipeIfServerMenuNone", methods=["POST"])
def answerRecipeIfServerMenuNone():
    sessionId = request.json['context']['session']['id']
    recipe = recommendRecipe()
    session[sessionId]['recipeName'] = recipe['name']
    session[sessionId]['chefName'] = recipe['chef']
    session[sessionId]['menuName'] = recipe['menu']
    session[sessionId]['step'] = recipe['steps'][0]
    session[sessionId]['stepNo'] = 0
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "recipeNameWhenAnswerRecipe": session[sessionId]['recipeName'],
            "stepWhenAnswerRecipe": session[sessionId]['step'],
            "stepNoWhenAnswerRecipe": session[sessionId]['stepNo']
        }
    }
    return jsonify(res)

#3. 재료안내
#3.1. 키워드가 없을 때
@app.route("/answerIngredientsWithoutKeyWord", methods=["POST"])
def answerIngredient():
    sessionId = request.json['context']['session']['id']
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
    sessionId = request.json['context']['session']['id']
    menuName = session[sessionId]['menuName']
    recipe = getRandomRecipeByMenu(menuName)
    session[sessionId]['recipeName'] = recipe['name']
    session[sessionId]['chefName'] = recipe['chef']
    session[sessionId]['menuName'] = recipe['menu']
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
    sessionId = request.json['context']['session']['id']
    recipeName = session[sessionId]['recipeName']
    recipe = getRecipeByRecipe(recipeName)
    session[sessionId]['recipeName'] = recipe['name']
    session[sessionId]['chefName'] = recipe['chef']
    session[sessionId]['menuName'] = recipe['menu']
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
    sessionId = request.json['context']['session']['id']
    return "키워드로 받은 레시피의 재료//준비중인 기능??"
#3.2.2. 키워드가 메뉴일 때
@app.route("/answerIngredientsByMenu", methods=["POST"])
def answerIngredientsByMenu():
    sessionId = request.json['context']['session']['id']
    req = request.json
    menuName = req['action']['parameters']['menuNameWhenAnswerIngredient']['value']
    recipe = getRandomRecipeByMenu(menuName)
    session[sessionId]['recipeName'] = recipe['name']
    session[sessionId]['chefName'] = recipe['chef']
    session[sessionId]['menuName'] = recipe['menu']
    ingredients = " ".join(str(x) for x in recipe['ingredients'])
    res = {
        "version": "1.0",
        "resultCode": "OK",
        "output": {
            "ingredientsWhenMenuExists" : ingredients
        }
    }
    return jsonify(res)

#4. 스텝이동(이전)
@app.route("/movePreviousStep", methods=["POST"])
def movePreviousStep():
    sessionId = request.json['context']['session']['id']
    res = {
            "version": "1.0",
            "resultCode": "OK",
            "output": {
                "booleanStepExistWhenMovePreviousStep": checkStepExist()
            }
        }
    return jsonify(res)
#4.1. 서버에 스텝이 있을 경우
@app.route("/movePreviousStepIfServerStepExists", methods=["POST"])
def movePreviousStepIfServerStepExists():
    sessionId = request.json['context']['session']['id']
    recipeName = session[sessionId]['recipeName']
    oldStepNo = session[sessionId]['stepNo']
    step, newStepNo = previousStep(recipeName, oldStepNo)
    session[sessionId]['step'] = step
    session[sessionId]['stepNo'] = newStepNo
    res = {
            "version": "1.0",
            "resultCode": "OK",
            "output": {
                "stepWhenPreviousStep": step
            }
        }
    return jsonify(res)


#5. 스텝이동(다음)
@app.route("/moveNextStep", methods=["POST"])
def moveNextStep():
    sessionId = request.json['context']['session']['id']
    res = {
            "version": "1.0",
            "resultCode": "OK",
            "output": {
                "booleanStepExistWhenMoveNextStep": checkStepExist()
            }
        }
    return jsonify(res)
#5.1. 서버에 스텝이 있을 경우
@app.route("/moveNextStepIfServerStepExists", methods=["POST"])
def moveNextStepIfServerStepExists():
    sessionId = request.json['context']['session']['id']
    recipeName = session[sessionId]['recipeName']
    oldStepNo = session[sessionId]['stepNo']
    step, newStepNo = nextStep(recipeName, oldStepNo)
    session[sessionId]['step'] = step
    session[sessionId]['stepNo'] = newStepNo
    res = {
            "version": "1.0",
            "resultCode": "OK",
            "output": {
                "stepWhenNextStep": step
            }
        }
    return jsonify(res)

#6. 스텝이동(숫자지정)
@app.route("/moveStepByStepNo", methods=["POST"])
def moveStepByStepNo():
    sessionId = request.json['context']['session']['id']
    res = {
            "version": "1.0",
            "resultCode": "OK",
            "output": {
                "booleanRecipeExistWhenMoveStepByStepNo": checkRecipeExist()
            }
        }
    return jsonify(res)
#6.1. 서버에 레시피가 있는 경우
@app.route("/moveStepByStepNoIfServerRecipeExists", methods=["POST"])
def moveStepByStepNoIfServerRecipeExists():
    sessionId = request.json['context']['session']['id']
    req = request.json
    reqStepNo = int(req['action']['parameters']['stepNoWhenRequestStepByStepNo']['value']) - 1
    recipeName = session[sessionId]['recipeName']
    step, newStepNo = numberStep(recipeName, reqStepNo)
    session[sessionId]['step'] = step
    session[sessionId]['stepNo'] = newStepNo
    res = {
            "version": "1.0",
            "resultCode": "OK",
            "output": {
                "stepWhenStepByStepNo": step
            }
        }
    return jsonify(res)

#5. 좋아요 싫어요는 서버에서 할게 아니지?

if __name__ == '__main__':
    app.secret_key = str(os.urandom(16))
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host='ec2-13-125-180-243.ap-northeast-2.compute.amazonaws.com',port=5000)
    # app.run(port=5000)