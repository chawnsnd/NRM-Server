from flask import Flask, request, jsonify, Response
from service.recipeService import *
from dao.recipeDao import *
import os

app = Flask(__name__)

session = {}
sessionId = ""

def checkMenuExist():
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    if 'menuName' in session[sessionId]:
        menuExist = "true"
    else:
        menuExist = "false"
    return menuExist

def checkRecipeExist():
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    if 'recipeName' in session[sessionId]:
        recipeExist = "true"
    else:
        recipeExist = "false"
    return recipeExist

def checkStepExist():
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    if 'step' in session[sessionId]:
        stepExist = "true"
    else:
        stepExist = "false"
    return stepExist

@app.before_first_request
def before_first_request():
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    session[sessionId] = {}

#0. 심사를 위한 health
@app.route("/health", methods=["GET"])
def health():
    return Response("OK", status=200)

#1. 메뉴추천
@app.route("/answerMenuRecommendation", methods=["POST"])
def answerMenuRecommendation():
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    try:
        recipe = recommendRecipe()
    except:
        res = {
            "version": "1.0",
            "resultCode": "error_db_none",
        }
        return jsonify(res)
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
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    req = request.json
    menuName = req['action']['parameters']['menuNameWhenAnswerRecipe']['value']
    try:
        recipe = getRecipeByMenu(menuName) #이거 만들어야 됨
    except:
        res = {
            "version": "1.0",
            "resultCode": "error_db_none",
        }
        return jsonify(res)
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
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
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
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    req = request.json
    chefName = req['action']['parameters']['chefNameWhenAnswerRecipe']['value']
    menuName = session[sessionId]['menuName']
    try:
        recipe = getRecipeByMenuAndChef(menuName, chefName)
    except:
        try:
            recipe = getRecipeByChef(chefName)
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
        except:
            res = {
                "version": "1.0",
                "resultCode": "error_db_none",
            }
            return jsonify(res)
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
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    req = request.json
    chefName = req['action']['parameters']['chefNameWhenAnswerRecipe']['value']
    try:
        recipe = getRandomRecipeByChef(chefName)
    except:
        res = {
            "version": "1.0",
            "resultCode": "error_db_none",
        }
        return jsonify(res)
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
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    req = request.json
    chefName = req['action']['parameters']['chefNameWhenAnswerRecipe']['value']
    menuName = req['action']['parameters']['menuNameWhenAnswerRecipe']['value']
    try:
        recipe = getRecipeByMenuAndChef(menuName, chefName)
    except:
        res = {
            "version": "1.0",
            "resultCode": "error_db_none",
        }
        print(res)
        return jsonify(res)
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
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
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
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    try:
        menuName = session[sessionId]['menuName']
    except:
        res = {
            "version": "1.0",
            "resultCode": "error_db_none",
        }
        return jsonify(res)
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
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    try:
        recipe = recommendRecipe()
    except:
        res = {
            "version": "1.0",
            "resultCode": "error_db_none",
        }
        return jsonify(res)
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
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    if 'recipeName' in session[sessionId]:
        res = {
            "version": "1.0",
            "resultCode": "OK",
            "output": {"sessionState": "recipeExists"}
        }
    elif 'menuName' in session[sessionId]:
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
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    menuName = session[sessionId]['menuName']
    try:
        recipe = getRandomRecipeByMenu(menuName)
    except:
        res = {
            "version": "1.0",
            "resultCode": "error_db_none",
        }
        return jsonify(res)
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
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    recipeName = session[sessionId]['recipeName']
    try:
        recipe = getRecipeByRecipe(recipeName)
    except:
        res = {
            "version": "1.0",
            "resultCode": "error_db_none",
        }
        return jsonify(res)
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
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    return "키워드로 받은 레시피의 재료//준비중인 기능??"
#3.2.2. 키워드가 메뉴일 때
@app.route("/answerIngredientsByMenu", methods=["POST"])
def answerIngredientsByMenu():
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    req = request.json
    menuName = req['action']['parameters']['menuNameWhenAnswerIngredient']['value']
    try:
        recipe = getRandomRecipeByMenu(menuName)
    except:
        res = {
            "version": "1.0",
            "resultCode": "error_db_none",
        }
        return jsonify(res)
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
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
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
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    recipeName = session[sessionId]['recipeName']
    oldStepNo = session[sessionId]['stepNo']
    try:
        step, newStepNo = previousStep(recipeName, oldStepNo)
    except:
        res = {
            "version": "1.0",
            "resultCode": "error_db_none",
        }
        return jsonify(res)
    session[sessionId]['step'] = step
    session[sessionId]['stepNo'] = newStepNo
    res = {
            "version": "1.0",
            "resultCode": "OK",
            "output": {
                "stepWhenPreviousStep": step,
                "stepNoWhenPreviousStep": newStepNo
            }
        }
    return jsonify(res)


#5. 스텝이동(다음)
@app.route("/moveNextStep", methods=["POST"])
def moveNextStep():
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
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
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    recipeName = session[sessionId]['recipeName']
    oldStepNo = session[sessionId]['stepNo']
    try:
        step, newStepNo = nextStep(recipeName, oldStepNo)
    except:
        res = {
            "version": "1.0",
            "resultCode": "error_db_none",
        }
        return jsonify(res)
    session[sessionId]['step'] = step
    session[sessionId]['stepNo'] = newStepNo
    res = {
            "version": "1.0",
            "resultCode": "OK",
            "output": {
                "stepWhenNextStep": step,
                "stepNoWhenNextStep": newStepNo
            }
        }
    return jsonify(res)

#6. 스텝이동(숫자지정)
@app.route("/moveStepByStepNo", methods=["POST"])
def moveStepByStepNo():
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
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
    isNew = request.json['context']['session']['isNew']
    sessionId = request.json['context']['session']['id']
    if isNew is True:
        session[sessionId] = {}
    req = request.json
    reqStepNo = int(req['action']['parameters']['stepNoWhenRequestStepByStepNo']['value']) - 1
    recipeName = session[sessionId]['recipeName']
    try:
        step, newStepNo = numberStep(recipeName, reqStepNo)
    except:
        res = {
            "version": "1.0",
            "resultCode": "error_db_none",
        }
        return jsonify(res)
    session[sessionId]['step'] = step
    session[sessionId]['stepNo'] = newStepNo
    res = {
            "version": "1.0",
            "resultCode": "OK",
            "output": {
                "stepWhenStepByStepNo": step,
                "stepNoWhenStepByStepNo": newStepNo
            }
        }
    return jsonify(res)

#5. 좋아요 싫어요는 서버에서 할게 아니지?

if __name__ == '__main__':
    app.secret_key = str(os.urandom(16))
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='ec2-13-125-180-243.ap-northeast-2.compute.amazonaws.com',port=5000)
    # app.run(port=5000)