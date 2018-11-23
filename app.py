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

#0. 심사를 위한 allRecipe
@app.route("/allRecipe", methods=["GET"])
def allRecipe():
    return jsonify({
    "_id" : ObjectId("5bf4dc37aa33c8cb75d5ed83"),
    "ROW_NUM" : 1.0,
    "SUMRY" : "육수로 지은 밥에 야채를 듬뿍 넣은 영양만점 나물비빔밥!",
    "NATION_NM" : "한식",
    "TY_NM" : "밥",
    "COOKING_TIME" : "60분",
    "CALORIE" : "580Kcal",
    "menu" : "나물비빔밥",
    "name" : "추억의 나물비빔밥",
    "chef" : "최현석",
    "steps" : [ 
        "양지머리로 육수를 낸 후 식혀 기름을 걷어낸 후, 불린 쌀을 넣어 고슬고슬하게 밥을 짓습니다.", 
        "안심은 불고기 양념하여 30분간 재워 국물 없이 구워 한 김 식으면 한입 크기로 자릅니다.", 
        "청포묵은 고기와 비슷한 크기로 잘라 끓는 물에 데쳐내고 계란은 노른자와 흰자를 분리해 지단부쳐 곱게 채썹니다.", 
        "콩나물과 숙주, 미나리는 데쳐서 국간장과 참기름으로 간하고, 고사리와 도라지는 참기름을 두른 프라이팬에 살짝 볶아놓습니다.", 
        "밥을 참기름으로 무쳐 그릇에 담고 준비한 재료를 고루 얹습니다."
    ],
    "ingredients" : [ 
        "쌀 4컵,", 
        "안심 200g,", 
        "콩나물 20g,", 
        "청포묵 1/2모,", 
        "미나리 20g,", 
        "소금 약간,", 
        "국간장 약간,", 
        "다진파 약간,", 
        "다진마늘 약간,", 
        "참기름 약간,", 
        "고추장 1/2큰술,", 
        "설탕 약간,", 
        "숙주 20g,", 
        "도라지 20g,", 
        "고사리 20g,", 
        "계란 1개,", 
        "양지머리 100g,"
    ],
    "id" : 1.0
},{
    "_id" : ObjectId("5bf4dc37aa33c8cb75d5ed84"),
    "ROW_NUM" : 2.0,
    "SUMRY" : "정월대보름에 먹던 오곡밥! 영양을 한그릇에 담았습니다.",
    "NATION_NM" : "한식",
    "TY_NM" : "밥",
    "COOKING_TIME" : "60분",
    "CALORIE" : "338Kcal",
    "chef" : "최현석",
    "menu" : "오곡밥",
    "name" : "요즘핫한 오곡밥",
    "steps" : [ 
        "찹쌀과 멥쌀은 깨끗이 씻어 건져 놓습니다.", 
        "차수수는 붉은 물이 안 나올 때까지 깨끗이 씻어 놓습니다.", 
        "콩은 불려서 일어 건져놓고, 팥은 삶아서 건져놓고 삶은 물은 받아 놓습니다.", 
        "차조는 씻어서 잘 일은 후 건져놓습니다.", 
        "차조를 뺀 모든 재료를 고루 섞어 밥솥에 앉혀 놓고 팥 삶은 물에 소금(1/3작은술 정도)을 넣은 밥물을 붓는데, 밥물은 보통 짓는 밥물보다 20% 적게 붓습니다.", 
        "밥이 끓기 시작하면 차조를 고루 얹어 뜸을 들입니다."
    ],
    "ingredients" : [ 
        "멥쌀 1컵,", 
        "찹쌀 2컵,", 
        "수수 1컵,", 
        "차조 1컵,", 
        "콩 1/2컵,", 
        "팥 1/2컵,", 
        "소금 약간,"
    ],
    "id" : 2.0
},{
    "_id" : ObjectId("5bf4dc37aa33c8cb75d5ed85"),
    "ROW_NUM" : 3.0,
    "SUMRY" : "잡채밥 한 그릇이면 오늘 저녁 끝! 입 맛 없을 때 먹으면 그만이지요~",
    "NATION_NM" : "중국",
    "TY_NM" : "밥",
    "COOKING_TIME" : "30분",
    "CALORIE" : "520Kcal",
    "chef" : "최현석",
    "menu" : "잡채밥",
    "name" : "단짠단짠 잡채밥",
    "steps" : [ 
        "당면은 따뜻한 물에 불려 적당한 길이로 자릅니다.", 
        "고기와 버섯, 채소는 모두 채썹니다.", 
        "달군 팬에 기름을 두르고 고기와, 버섯, 당근, 고추, 호박을 볶다가 숨이 죽으면 부추를 넣습니다.", 
        "다진 파, 마늘, 생강을 넣고 소금과 통후추, 진간장을 넣어 간을 한 다음 당면을 넣어 볶아줍니다.", 
        "뜨거운 밥을 그릇에 담고 잡채를 얹어 냅니다."
    ],
    "ingredients" : [ 
        "당면 50g,", 
        "돼지고기 100g,", 
        "표고버섯 2장,", 
        "호박 1/4개,", 
        "당근 1/2개,", 
        "부추 30g,"
    ],
    "id" : 3.0
},{
    "_id" : ObjectId("5bf4dc37aa33c8cb75d5ed86"),
    "ROW_NUM" : 4.0,
    "SUMRY" : "다이어트에 으뜸인 콩나물밥. 밥 물 넣을때 평소보다 적게 넣는거 잊지마세요!",
    "NATION_NM" : "한식",
    "TY_NM" : "밥",
    "COOKING_TIME" : "40분",
    "CALORIE" : "401Kcal",
    "chef" : "백종원",
    "menu" : "콩나물밥",
    "name" : "단짠단짠 콩나물밥",
    "steps" : [ 
        "쌀은 미리 씻어 불려놓고 콩나물은 씻어 소금물에 살짝 데쳐 놓습니다.", 
        "쇠고기는 곱게 다져 파, 마늘, 진간장으로 양념하여 볶습니다.", 
        "콩나물 삶은 물을 냄비에 붓고 쌀을 앉혀 밥을 짓다가 끓으면 삶은 콩나물과 쇠고기를 얹어 뜸들입니다", 
        "뜸이 들면 고루 섞어 그릇에 담고 양념장과 함께 냅니다."
    ],
    "ingredients" : [],
    "id" : 4.0
},{
    "_id" : ObjectId("5bf4dc37aa33c8cb75d5ed87"),
    "ROW_NUM" : 5.0,
    "SUMRY" : "집에서도 쉽게 만들어 맛있게 먹을 수 있답니다. 어려워 마시고 만들어 보세요~!",
    "NATION_NM" : "한식",
    "TY_NM" : "떡/한과",
    "COOKING_TIME" : "60분",
    "CALORIE" : "259Kcal",
    "chef" : "백종원",
    "menu" : "약식",
    "name" : "단짠단짠 약식",
    "steps" : [ 
        "흰 설탕에 물을 붓고 끓이다가 거품이 일면서 한 부분부터 타기 시작하면 불을 끕니다.", 
        "압력솥에 물기 뺀 쌀을 담고 분량의 흑설탕, 간장, 참기름, 식물성기름, 계핏가루를 넣고 ①에서 만든 카라멜소스를 부어 물이들게 고루 섞습니다.", 
        "②에 밤, 대추, 잣을 넣고 섞습니다.", 
        "물 3컵을 붓고 센불로 가열하다가 끓기 시작하면 중불로 줄여 30분 지난뒤 불을 끄고 남은 열로 뜸들입니다."
    ],
    "ingredients" : [ 
        "찹쌀 3컵,", 
        "흑설탕 1컵,", 
        "계핏가루 1/2큰술,", 
        "깐밤 200g,", 
        "대추 50g,", 
        "잣 1큰술,", 
        "물엿 적당량,", 
        "식물성기름 3큰술,", 
        "흰설탕 1컵,", 
        "간장 1/3컵,", 
        "물 4컵,"
    ],
    "id" : 5.0
},{
    "_id" : ObjectId("5bf4dc37aa33c8cb75d5ed88"),
    "ROW_NUM" : 6.0,
    "SUMRY" : "호박죽 한 그릇이면 하루가 든든하답니다.",
    "NATION_NM" : "한식",
    "TY_NM" : "밥",
    "COOKING_TIME" : "30분",
    "CALORIE" : "115Kcal",
    "chef" : "백종원",
    "menu" : "호박죽",
    "name" : "추억의 호박죽",
    "steps" : [ 
        "청동호박은 반을 갈라 씨를 빼고 껍질을 벗깁니다.", 
        "찹쌀은 깨끗이 씻어 불렸다가 가루로 빻습니다.", 
        "팥은 씻어 일어 물을 넣고 한소끔 끓으면 첫물은 버리고 다시 물을 부어 푹 끓입니다.", 
        "호박은 1cm 두께로 썰어 냄비에 담고 물과 설탕을 넣어 푹 끓입니다.", 
        "호박이 푹 무르면 찹쌀가루를 물에 풀어 넣고 팥도 함께 넣어 끓입니다.", 
        "다 끓으면 설탕, 소금으로 간합니다."
    ],
    "ingredients" : [ 
        "청동호박 1/2개,", 
        "팥 1컵,", 
        "찹쌀 2컵,", 
        "물 10컵,", 
        "설탕 약간,", 
        "소금 약간,"
    ],
    "id" : 6.0
},{
    "_id" : ObjectId("5bf4dc37aa33c8cb75d5ed89"),
    "ROW_NUM" : 7.0,
    "SUMRY" : "검은깨를 갈아서 만든 고소함이 가득한 흑임자죽. 남녀노소 모두 사랑하는 맛!",
    "NATION_NM" : "한식",
    "TY_NM" : "밥",
    "COOKING_TIME" : "25분",
    "CALORIE" : "450Kcal",
    "chef" : "이연복",
    "menu" : "흑임자죽",
    "name" : "요즘핫한 흑임자죽",
    "steps" : [ 
        "쌀은 충분히 불려서 소쿠리에 건져 놓습니다.", 
        "깨는 깨끗이 일어 건져서 고소한 향이 나도록 볶습니다.", 
        "분쇄기에 쌀과 깨를 따로따로 넣어 물을 조금씩 넣어가며 갈아 고운 체에 밭칩니다.", 
        "밑이 두터운 냄비에 곱게 간 쌀과 물을 부어 나무주걱으로 저으며 끓입니다.", 
        "냄비가 뜨거워 지면 갈은 깨를 조금씩 부어 멍울지지 않도록 가끔 저어주며 끓입니다.", 
        "확 끓어오르면 불을 약하게 줄이고 잘 섞이도록 서서히 끓입니다."
    ],
    "ingredients" : [ 
        "쌀 1컵,", 
        "흑임자 1/2컵,", 
        "물 6컵,", 
        "소금 약간,", 
        "설탕 약간,"
    ],
    "id" : 7.0
},{
    "_id" : ObjectId("5bf4dc37aa33c8cb75d5ed8a"),
    "ROW_NUM" : 8.0,
    "SUMRY" : "향긋한 카레향이 너무 좋지요. 누구나 좋아하는 만들기도 간편한 음식입니다.",
    "NATION_NM" : "동남아시아",
    "TY_NM" : "밥",
    "COOKING_TIME" : "30분",
    "CALORIE" : "650Kcal",
    "chef" : "이연복",
    "menu" : "카레라이스",
    "name" : "단짠단짠 카레라이스",
    "steps" : [ 
        "쇠고기와 채소는 도톰하게 깍뚝썰기하여 버터에 볶습니다.", 
        "카레는 찬물 2컵에 물을 조금씩 넣어가며 풀어놓습니다.", 
        "①의 냄비에 완두를 넣고 물을 자작하게 붓고 끓이다가 ②를 붓고 더 끓입니다.", 
        "국물이 되직하게 졸면 우유를 붓고 소금과 후춧가루로 간을 맞춥니다.", 
        "따뜻한 밥위에 완성된 카레를 넉넉히 얹어냅니다."
    ],
    "ingredients" : [ 
        "쇠고기 200g,", 
        "감자 2개,", 
        "양파 1개,", 
        "당근 1/2개,", 
        "완두콩 4큰술,", 
        "카레 70g,", 
        "우유 1/2컵,", 
        "밥 4공기,", 
        "소금 약간,", 
        "통후추 약간,"
    ],
    "id" : 8.0
},{
    "_id" : ObjectId("5bf4dc37aa33c8cb75d5ed8b"),
    "ROW_NUM" : 9.0,
    "SUMRY" : "각종 채소를 계란 속에 꼭꼭 숨겨 편식하는 아이들도 맛있게 먹어요~",
    "NATION_NM" : "서양",
    "TY_NM" : "밥",
    "COOKING_TIME" : "30분",
    "CALORIE" : "630Kcal",
    "chef" : "이연복",
    "menu" : "오므라이스",
    "name" : "세상간편한 오므라이스",
    "steps" : [ 
        "청피망, 홍피망, 양파, 오이, 당근은 잘게 다져 준비합니다.", 
        "프라이팬에 버터를 두르고 당근, 양파를 볶다가 양파가 투명해지면 남은 야채 재료를 넣고 볶습니다.", 
        "찬밥을 넣어 야채와 잘 섞은 후 소금, 후춧가루로 간을 약하게 맞춥니다.", 
        "계란을 멍울 없이 풀어 소금, 후춧가루로 간하고, 반쯤 익으면 계란 중앙에 밥을 놓고 잘 감싸서 접시에 담습니다.", 
        "다시마와 멸치로 다시국물을 만들어 체에 거른 후 프라이팬에 육수 2컵을 넣고 쌈장을 잘 풀어 끓여줍니다.", 
        "팔팔 끓어오르면 전분가루를 넣어 농도를 되직하게 만든 후 오므라이스 위에 뿌려줍니다."
    ],
    "ingredients" : [ 
        "계란 3개,", 
        "양파 1/4개,", 
        "물 3컵,", 
        "당근 1/3개,", 
        "쌈장 3큰술,", 
        "후춧가루 약간,", 
        "소금 약간,", 
        "밥 2공기,", 
        "청피망 1/2개,", 
        "홍피망 1/2개,", 
        "오이 1/3개,", 
        "전분 약간,", 
        "멸치 한 줌,", 
        "다시마 1장,"
    ],
    "id" : 9.0
},
{
    "_id" : ObjectId("5bf4dc37aa33c8cb75d5ed8c"),
    "ROW_NUM" : 10.0,
    "SUMRY" : "쫀득쫀득한 수제비와 담백한 맛의 감자가 이뤄내는 하모니!",
    "NATION_NM" : "한식",
    "TY_NM" : "만두/면류",
    "COOKING_TIME" : "60분",
    "CALORIE" : "410Kcal",
    "chef" : "레이먼킴",
    "menu" : "감자수제비",
    "name" : "세상간편한 감자수제비",
    "steps" : [ 
        "밀가루에 소금과 따뜻한 물을 넣어 말랑하게 반죽하여 젖은 면보에 싸 냉장고에 30분간 넣어둡니다.", 
        "감자와 애호박은 도톰하게 반달썰기를 합니다.", 
        "실파는 4cm 길이로 자르고 홍고추는 어슷썹니다.", 
        "멸치는 장국을 끓여 국간장으로 간을 맞춥니다.", 
        "국물이 끓어오르면 감자를 넣고, 반쯤 익으면 수제비 반죽을 얇게 뜯어 넣습니다.", 
        "호박을 넣어 파랗게 익으면 홍고추와 실파, 참기름을 넣고 불을 끕니다."
    ],
    "ingredients" : [ 
        "밀가루 4컵,", 
        "감자 2개,", 
        "애호박 1/2개,", 
        "멸치 10마리,", 
        "실파 2뿌리,", 
        "홍고추 1개,", 
        "물 1컵,", 
        "양념장 적당량,", 
        "국간장 약간,", 
        "참기름 약간,", 
        "소금 약간,"
    ],
    "id" : 10.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed8d"),
    "ROW_NUM" : 11.0,
    "SUMRY" : "더운 여름, 살얼음 동동 띄운 시원한 냉면 한그릇 생각나시죠~",
    "NATION_NM" : "한식",
    "TY_NM" : "만두/면류",
    "COOKING_TIME" : "50분",
    "CALORIE" : "630Kcal",
    "chef" : "레이먼킴",
    "menu" : "냉면",
    "name" : "추억의 냉면",
    "steps" : [ 
        "쇠고기는 삶아 건져 편육으로 썰고 국물은 식혀 기름을 걷어 육수로 준비합니다.", 
        "동치미무는 길쭉하고 얇게 썰고 오이는 어슷썰어 소금에 20분 동안 절였다가 물기를 꼭 짜서 살짝 볶습니다.", 
        "배는 납작하게 썰고 계란은 삶아 반 가릅니다.", 
        "육수와 동치미국물을 섞어 소금과 설탕, 식초로 간을 맞춰 차게 둡니다.", 
        "냉면국수는 삶아 찬물에 비벼 빨듯이 헹굽니다.", 
        "대접에 면을 담고 편육과 무, 오이, 배, 계란을 얹은 후 육수를 부어 냅니다."
    ],
    "ingredients" : [ 
        "냉면 400g,", 
        "쇠고기 300g,", 
        "동치미국물 1개,", 
        "오이 1개,", 
        "배 1개,", 
        "계란 2개,", 
        "식초 2큰술,", 
        "설탕 1큰술,", 
        "소금 약간,", 
        "쇠고기육수 4컵,", 
        "동치미무 1개,"
    ],
    "id" : 11.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed8e"),
    "ROW_NUM" : 12.0,
    "SUMRY" : "시원한 동치미에 쫄깃한 국수를 말아서 만들어보세요.",
    "NATION_NM" : "한식",
    "TY_NM" : "만두/면류",
    "COOKING_TIME" : "30분",
    "CALORIE" : "400Kcal",
    "chef" : "레이먼킴",
    "menu" : "동치미막국수",
    "name" : "요즘핫한 동치미막국수",
    "steps" : [ 
        "쇠고기는 채썰어 분량의 재료로 갖은양념하여 약간 재웠다가 팬에 볶습니다.", 
        "오이는 가늘게 채썰어 소금에 절였다가 물기를 꼭 짜고 살짝 볶아 식힙니다.", 
        "동치미무는 반달모양으로 얄팍하게 썰어 깨소금과 참기름으로 무칩니다.", 
        "국수는 넉넉한 끓는 물에 삶아 찬물에 헹구어 건져 1인분씩 사리지어 놓습니다.", 
        "그릇에 국수를 담고 고기채, 오이채, 동치미무, 계란지단채, 붉은 고추채를 얹어 동치미 국물을 가만히 붓습니다"
    ],
    "ingredients" : [ 
        "국수 400g,", 
        "쇠고기 100g,", 
        "동치미무 1/4개,", 
        "계란 1개,", 
        "홍고추 1개,", 
        "소금 약간,", 
        "깨소금 약간,", 
        "참기름 1/2큰술,", 
        "동치미국물 8컵,", 
        "간장 1큰술,", 
        "설탕 1/4작은술,", 
        "통후추 약간,"
    ],
    "id" : 12.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed8f"),
    "ROW_NUM" : 13.0,
    "SUMRY" : "맛있게 담근 열무김치에 냉면을 말아 먹어 보세요~ 새콤달콤 끝내줍니다!",
    "NATION_NM" : "한식",
    "TY_NM" : "만두/면류",
    "COOKING_TIME" : "25분",
    "CALORIE" : "625Kcal",
    "chef" : "김풍",
    "menu" : "열무김치냉면",
    "name" : "단짠단짠 열무김치냉면",
    "steps" : [ 
        "열무는 다듬어 소금에 절여둡니다.", 
        "냄비에 물 1컵과 찹쌀가루 2큰술을 넣고 나무주걱으로 저어가며 약불에서 찹쌀풀을 쑵니다.", 
        "볼에 물 4컵과 고춧가루 4큰술을 풀고 찹쌀풀을 넣어 간을 맞춥니다.", 
        "③에 절인 열무와 어슷썬 고추, 채썬 파, 마늘, 생강을 넣고 버무려 열무김치를 담아 익힙니다.", 
        "알맞게 익은 열무김치에 식초, 설탕, 소금으로 간을 맞추어 차게 둡니다.", 
        "냉면을 삶아 그릇에 담고 열무김치를 부은 다음 겨자 갠 것을 곁들입니다."
    ],
    "ingredients" : [ 
        "열무 1/2단,", 
        "찹쌀가루 2큰술,", 
        "냉면 500g,", 
        "홍고추 1개,", 
        "청고추 1개,", 
        "대파 약간,", 
        "다진마늘 1작은술,", 
        "다진생강 1/2작은술,", 
        "고춧가루 4큰술,", 
        "식초 4큰술,", 
        "설탕 4큰술,", 
        "겨자 약간,", 
        "물 1컵,"
    ],
    "id" : 13.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed90"),
    "ROW_NUM" : 14.0,
    "SUMRY" : "갖가지 야채를 듬뿍 넣어서 만든 요리로 출출할 때 간식거리로 아주 좋답니다.",
    "NATION_NM" : "한식",
    "TY_NM" : "만두/면류",
    "COOKING_TIME" : "30분",
    "CALORIE" : "460Kcal",
    "chef" : "김풍",
    "menu" : "채소국수",
    "name" : "세상간편한 채소국수",
    "steps" : [ 
        "오이는 두께 0.3cm x 폭 0.3cm, 길이 5cm로 채썰어 소금에 절였다가 물기를 짭니다.", 
        "쇠고기는 두께와 폭이 0.3cm, 길이 5cm로 썰어 양념합니다.", 
        "표고도 물에 불려 쇠고기와 같은 크기로 채썰어 양념합니다.", 
        "부추는 잘 씻어 5cm 길이로 잘라둡니다.", 
        "계란은 노른자와 흰자를 분리하여 지단을 붙이고 채썰어 둡니다.", 
        "번철에 오이, 표고, 쇠고기순으로 볶습니다."
    ],
    "ingredients" : [ 
        "국수 200g,", 
        "표고버섯 3장,", 
        "오이 1/2개,", 
        "계란 1개,", 
        "부추 1/3단,", 
        "쇠고기 100g,", 
        "양념장 적당량,", 
        "상추 6장,", 
        "깻잎 15장,"
    ],
    "id" : 14.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed91"),
    "ROW_NUM" : 15.0,
    "SUMRY" : "해물로 시원한 국물에 국수를 말아 드셔보세요~",
    "NATION_NM" : "한식",
    "TY_NM" : "만두/면류",
    "COOKING_TIME" : "40분",
    "CALORIE" : "530Kcal",
    "chef" : "김풍",
    "menu" : "해물국수",
    "name" : "세상간편한 해물국수",
    "steps" : [ 
        "고기는 저며서 녹말가루, 계란흰자, 청주, 소금으로 양념합니다.", 
        "해물은 한 입 크기로 손질해 데칩니다.", 
        "채소는 얄팍하게 저며썹니다.", 
        "팬에 기름을 둘러 다진 마늘을 볶다가 고기를 넣어 볶습니다.", 
        "어느정도 익으면 멸치국물을 부어 끓이다가 해물과 채소를 넣고 간을 합니다.", 
        "삶은 국수에 ⑤의 해물장국을 부어냅니다."
    ],
    "ingredients" : [ 
        "국수 400g,", 
        "돼지고기 100g,", 
        "녹말 1큰술,", 
        "계란흰자 1개,", 
        "오징어 1/2마리,", 
        "새우 100g,", 
        "홍합 100g,", 
        "표고버섯 2개,", 
        "죽순 2개,", 
        "파 약간,", 
        "다진마늘 약간,", 
        "멸칫국물 8컵,", 
        "청주 약간,", 
        "소금 약간,"
    ],
    "id" : 15.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed92"),
    "ROW_NUM" : 16.0,
    "SUMRY" : "만두를 예쁘게 만들면 이쁜 딸을 낳는다고 하죠? 가족들과 오손도손 맛있는 만두국 만들어 드셔보세요~",
    "NATION_NM" : "한식",
    "TY_NM" : "만두/면류",
    "COOKING_TIME" : "40분",
    "CALORIE" : "540Kcal",
    "chef" : "이원일",
    "menu" : "만둣국",
    "name" : "세상간편한 만둣국",
    "steps" : [ 
        "김치는 소를 털고 송송 썰어 물기를 꼭 짜고 숙주는 삶아 물기를 뺍니다.", 
        "갈은 돼지고기나 갈은 쇠고기를 준비합니다.", 
        "두부는 수분을 완전히 제거합니다.", 
        "양파, 마늘, 대파는 곱게 다져놓습니다.", 
        "김치, 숙주, 갈은 고기, 다진 양파, 마늘, 대파에 참기름과 후춧가루, 소금으로 간을 합니다.", 
        "밀가루 반죽을 하여 얇게 민다음 지름이 6cm 정도 되게 하여 그 안에 ⑤에서 만든 만둣속을 넣습니다."
    ],
    "ingredients" : [ 
        "김치 1/2포기,", 
        "숙주 150g,", 
        "표고버섯 4장,", 
        "두부 1/2모,", 
        "만두피 40장,", 
        "육수 7컵,", 
        "쇠고기 40g,", 
        "다진파 1큰술,", 
        "다진마늘 1큰술,", 
        "소금 약간,", 
        "후춧가루 약간,", 
        "깨소금 약간,", 
        "간장 1큰술,", 
        "설탕 1큰술,", 
        "참기름 1큰술,"
    ],
    "id" : 16.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed93"),
    "ROW_NUM" : 17.0,
    "SUMRY" : "철분과 무기질이 풍부한 다시마로 피부건강을 지켜보세요~",
    "NATION_NM" : "한식",
    "TY_NM" : "국",
    "COOKING_TIME" : "20분",
    "CALORIE" : "63Kcal",
    "chef" : "이원일",
    "menu" : "다시마냉국",
    "name" : "추억의 다시마냉국",
    "steps" : [ 
        "다시마는 두텁고 광택이 있는 것으로 물에 씻어 젖은 행주로 여러 번 닦은 뒤 찬물 5컵에 담가 30분 정도 불렸다가 건져놓습니다.", 
        "오이는 소금으로 비벼 씻어 헹궈 가늘게 채썬 뒤 찬물에 잠시 담갔다가 건져놓습니다.", 
        "홍고추는 반으로 갈라 씨를 털어 곱게 채썹니다.", 
        "손질한 다시마를 돌돌 말아 가늘게 채썰어 달라붙지 않게 털어둡니다.", 
        "넓은 그릇에 다시마, 채썬 오이, 홍고추를 담고 다진 파와 마늘, 고춧가루, 깨소금, 소금으로 양념하여 차게 해둔 ①을 붓습니다."
    ],
    "ingredients" : [ 
        "다시마 2장,", 
        "오이 1/2개,", 
        "홍고추 1개,", 
        "다진파 1/2작은술,", 
        "다진마늘 1/4작은술,", 
        "소금 약간,", 
        "고춧가루 약간,", 
        "깨소금 약간,", 
        "물 5컵,"
    ],
    "id" : 17.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed94"),
    "ROW_NUM" : 18.0,
    "SUMRY" : "부드러운 두부로 맛나는 두부국을 끓여 단백함을 맛보세요.",
    "NATION_NM" : "한식",
    "TY_NM" : "국",
    "COOKING_TIME" : "40분",
    "CALORIE" : "120Kcal",
    "chef" : "이원일",
    "menu" : "두부국",
    "name" : "요즘핫한 두부국",
    "steps" : [ 
        "쇠고기는 얄팍하게 썰어 다진 마늘과 후춧가루, 진간장으로 조물조물 양념합니다.", 
        "양념한 고기를 냄비에 넣고 육수를 부어 끓이다가 고추장을 연하게 풀고 국간장이나 소금으로 간을 맞춥니다.", 
        "두부를 1cm 폭으로 길쭉하게 썰어 끓고 있는 국물에 쏟아 넣고 두부가 떠오를 때까지 끓입니다.", 
        "두부가 떠 오르면 채썬 파, 다진 마늘을 넣고 조금 더 끓입니다."
    ],
    "ingredients" : [ 
        "두부 1모,", 
        "쇠고기 100g,", 
        "파 1뿌리,", 
        "다진마늘 1큰술,", 
        "고추장 1큰술,", 
        "참기름 1작은술,", 
        "진간장 조금,", 
        "소금 조금,", 
        "후춧가루 조금,"
    ],
    "id" : 18.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed95"),
    "ROW_NUM" : 19.0,
    "SUMRY" : "국물이 정말 시원해서 속풀이 식단으로도 안성맞춤!",
    "NATION_NM" : "한식",
    "TY_NM" : "국",
    "COOKING_TIME" : "30분",
    "CALORIE" : "130Kcal",
    "chef" : "이원일",
    "menu" : "두부조개탕",
    "name" : "단짠단짠 두부조개탕",
    "steps" : [ 
        "모시조개는 소금물로 해감시킨 후 물을 붓고 끓이다가 모시는 건져내고 국물은 걸러 놓습니다.", 
        "콩나물은 다듬어 씻고 두부는 큼직하게 썰며, 붉은 고추는 어슷썰어 씨를 털고 실파는 4cm 길이로 썰어 놓습니다.", 
        "북어포는 물에 씻어 물기를 짠 뒤 소금과 후춧가루로 양념한 뒤 밀가루를 묻혀 계란을 푼 물에 섞습니다.", 
        "조개 삶아낸 국물에 다진 마늘을 넣고 끓이다가 손질한 콩나물을 넣습니다.", 
        "한소끔 끓으면 모시조개 두부, 붉은 고추, 실파를 넣고 계란물에 섞어 놓은 북어를 넣어 조금 더 끓이다가 소금, 후춧가루로 간을 합니다."
    ],
    "ingredients" : [ 
        "두부 1/2모,", 
        "콩나물 50g,", 
        "모시조개 200g,", 
        "북어 30g,", 
        "홍고추 1개,", 
        "실파 3뿌리,", 
        "밀가루 1큰술,", 
        "계란 1개,", 
        "마늘 1큰술,", 
        "소금 약간,", 
        "후춧가루 약간,"
    ],
    "id" : 19.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed96"),
    "ROW_NUM" : 20.0,
    "SUMRY" : "고향의 맛을 느낄 수 있는 무국. 밥한그릇 뚝딱이죠!",
    "NATION_NM" : "한식",
    "TY_NM" : "국",
    "COOKING_TIME" : "30분",
    "CALORIE" : "75Kcal",
    "chef" : "홍석천",
    "menu" : "무맑은국",
    "name" : "엄마손맛 무맑은국",
    "steps" : [ 
        "쇠고기는 2cm 길이로 도톰하게 저며썰고 무는 길이 3cm 정도씩 토막을 낸 뒤 반을 갈라 0.2cm 두께로 나박썰기를 합니다.", 
        "썰어놓은 쇠고기는 다진 마늘 1작은술과 국간장 1큰술, 후춧가루 약간으로 양념해 간이 골고루 배도록 조물조물 무칩니다.", 
        "냄비에 물 5컵을 붓고 팔팔 끓이다가 양념해 놓은 쇠고기를 넣고 고기가 익을 때까지 한소끔 끓입니다.", 
        "끓는 쇠고기 장국에 나박썬 무를 넣는다. 끓을 때 생기는 거품은 걷어냅니다.", 
        "무가 말갛게 익으면 국간장과 소금을 1:1의 비율로 넣어 간을 하고 다진 마늘과 실파를 넣어 조금 더 끓입니다."
    ],
    "ingredients" : [ 
        "쇠고기 120g,", 
        "무 400g,", 
        "실파 20g,", 
        "마늘 1작은술,", 
        "국간장 1큰술,", 
        "소금 1큰술,", 
        "참기름 약간,", 
        "후춧가루 약간,", 
        "물 5컵,"
    ],
    "id" : 20.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed97"),
    "ROW_NUM" : 21.0,
    "SUMRY" : "미역국은 철분이 풍부하게 함유된 음식이라 여자들에게 특히 좋은 음식이라 하지요.",
    "NATION_NM" : "한식",
    "TY_NM" : "국",
    "COOKING_TIME" : "30분",
    "CALORIE" : "95Kcal",
    "chef" : "홍석천",
    "menu" : "미역국",
    "name" : "엄마손맛 미역국",
    "steps" : [ 
        "찬물에 씻어 담가 충분히 불려 물기를 뺀 뒤 손으로 적당하게 잘라 놓습니다.", 
        "쇠고기는 연한 살코기만을 골라 곱게 다져 다진 마늘, 국간장, 참기름을 넣고 간이 배도록 고루 섞습니다.", 
        "냄비에 식용유를 두르고 양념한 쇠고기를 넣어 볶다가 고기가 익으면 손질한 미역을 넣고 같이 볶습니다.", 
        "미역이 푸른색을 띠게 볶아지면 분량의 물을 붓고 한소끔 끓인 뒤 다진 마늘을 넣고 국간장, 후춧가루로 간을 합니다."
    ],
    "ingredients" : [ 
        "미역 2컵,", 
        "다진쇠고기 150g,", 
        "마늘 1큰술,", 
        "식용유 약간,", 
        "후춧가루 약간,", 
        "국간장 2큰술,", 
        "참기름 2큰술,", 
        "물 10컵,"
    ],
    "id" : 21.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed98"),
    "ROW_NUM" : 22.0,
    "SUMRY" : "더운 여름, 새콤달콤 시원한 미역냉국으로 입맛을 살려보세요~",
    "NATION_NM" : "한식",
    "TY_NM" : "국",
    "COOKING_TIME" : "30분",
    "CALORIE" : "82Kcal",
    "chef" : "홍석천",
    "menu" : "미역냉국",
    "name" : "추억의 미역냉국",
    "steps" : [ 
        "미역은 줄기를 떼어 티를 골라낸 다음 찬물에 담가30분 정도 불립니다.", 
        "불린 미역을 깨끗이 씻어 손으로 잘게 찢은 다음 끓는 물에 재빨리 데쳐 물기를 빼놓습니다.", 
        "오이는 소금에 비벼 씻어 가늘게 채썰어 찬물에 잠깐 담가 건집니다.", 
        "대파 흰부분만 다듬어 씻은 다음 반으로 갈라 가늘게 채썹니다.", 
        "큰 그릇에 데친 미역을 담고 분량의 양념 재료를 넣어 무쳐줍니다.", 
        "양념한 미역에 맛이 배어들면 차갑게 준비한 미역 우린물을 붓고 채썬 오이와 대파를 넣고 차게 먹습니다."
    ],
    "ingredients" : [ 
        "불린미역 2컵,", 
        "오이 1/2개,", 
        "대파 1/2뿌리,", 
        "다진마늘 1/2작은술,", 
        "깨소금 약간,", 
        "소금 약간,", 
        "고춧가루 약간,", 
        "간장 2큰술,", 
        "물 10컵,"
    ],
    "id" : 22.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed99"),
    "ROW_NUM" : 23.0,
    "SUMRY" : "생태국에 콩나물을 넣어주면 시원함이 배가 됩니다.",
    "NATION_NM" : "한식",
    "TY_NM" : "국",
    "COOKING_TIME" : "30분",
    "CALORIE" : "110Kcal",
    "chef" : "박준우",
    "menu" : "생태국",
    "name" : "요즘핫한 생태국",
    "steps" : [ 
        "생태는 씻어 내장을 빼고 비늘을 긁은 뒤 다시 씻어 5cm 길이로 토막내어 소금을 살짝 뿌려둡니다.", 
        "콩나물은 뿌리를 떼고 무는 0.5cm 두께로 얄팍하게 나박썬다. 붉은 고추는 어슷썰어 씨를 털고 미나리는 줄기만 4cm 길이로 썹니다.", 
        "마지막에 씻은 쌀뜨물을 받아 냄비에 붓고 센불에서 끓이다가 손질한 생태를 넣습니다.", 
        "국물이 끓어 생태가 익으면 무와 콩나물을 넣고 뚜껑을 덮은채 한소끔 끓입니다.", 
        "거의 끓었을 때 붉은 고추와 다진 마늘, 미나리를 넣고 소금과 후춧가루로 간 한 뒤 더 끓이다가 미나리가 살짝 숨이 죽으면 불에서 내립니다."
    ],
    "ingredients" : [ 
        "생태 1마리,", 
        "미나리 50g,", 
        "콩나물 50g,", 
        "무 1/4개,", 
        "홍고추 1개,", 
        "마늘 2쪽,", 
        "쌀뜨물 10컵,", 
        "소금 약간,", 
        "후춧가루 약간,"
    ],
    "id" : 23.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed9a"),
    "ROW_NUM" : 24.0,
    "SUMRY" : "독특한 바질향이 연어에 쏘옥~ 올리브오일로 한층 부드러운 연어회랍니다.",
    "NATION_NM" : "이탈리아",
    "TY_NM" : "나물/생채/샐러드",
    "COOKING_TIME" : "30분",
    "CALORIE" : "120Kcal",
    "chef" : "박준우",
    "menu" : "연어까르파치오",
    "name" : "엄마손맛 연어까르파치오",
    "steps" : [ 
        "[연어준비] 신선한 연어는 깨끗하게 포를 3장 떠놓고 포 위에 레몬즙을 발라 놓는다.(미리 발라두면 색이 변하므로 페스토 소스바르기 직전에 한다)", 
        "양파는 잘게 다져 놓습니다.", 
        "양송이는 3mm 두께로 슬라이스 합니다.", 
        "차이브는 물에 담궈 살려놓습니다.", 
        "[페스토소스 만들기] 바질, 이태리파슬리, 잣, 엔초비, 마늘을 믹서에 넣고 올리브오일를 넣어 가며 살짝만 갈아 꺼내고, 올리브오일와 파르메쟌을 넣어 농도와 맛을 냅니다.", 
        "[양송이 샐러드 만들기] 양송이는 5mm두께로 썰어 다진 양파, 레몬주스, 올리브오일, 소금, 후춧가루로 맛을 냅니다."
    ],
    "ingredients" : [ 
        "연어 6조각,", 
        "후춧가루 약간,", 
        "레몬즙 40g,", 
        "소금 약간,", 
        "양파 1/2개,", 
        "양송이버섯 4개,", 
        "올리브오일 60g,", 
        "방울토마토 4개,", 
        "페스토소스 만드는법 참조,", 
        "모듬채소 약간,", 
        "차이브 4개,"
    ],
    "id" : 24.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed9b"),
    "ROW_NUM" : 25.0,
    "SUMRY" : "아삭아삭한 오이와 새콤달콤한 냉국의 조화!",
    "NATION_NM" : "한식",
    "TY_NM" : "국",
    "COOKING_TIME" : "20분",
    "CALORIE" : "82Kcal",
    "chef" : "박준우",
    "menu" : "오이냉국",
    "name" : "엄마손맛 오이냉국",
    "steps" : [ 
        "오이는 굵은 소금으로 박박 문질러 씻은 뒤 채썰거나 얇게 통썰기 합니다.", 
        "손질한 오이에 다진 파와 마늘, 고춧가루, 식초를 넣어 골고루 무쳐놓습니다.", 
        "물 4컵을 끓였다 식힌 뒤 설탕 1큰술과 간장, 식초 2큰술씩, 소금 약간을 넣고 나머지 6컵의 생수를 넣어 냉국물을 만듭니다.", 
        "상에 낼 때에는 양념해 놓은 오이에 차갑게 식힌 냉국물을 붓고 깨소금을 살짝 뿌립니다."
    ],
    "ingredients" : [ 
        "오이 2개,", 
        "파 1작은술,", 
        "다진마늘 1작은술,", 
        "간장 3큰술,", 
        "식초 3큰술,", 
        "설탕 1큰술,", 
        "깨소금 약간,", 
        "고춧가루 약간,", 
        "물 10컵,", 
        "대파 1대,", 
        "홍고추 1개,", 
        "물 4컵,", 
        "소금 약간,"
    ],
    "id" : 25.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed9c"),
    "ROW_NUM" : 26.0,
    "SUMRY" : "시원한 해산물 샐러드~ 상큼한 레몬과 와인을 넣은 드레싱으로 깔끔하게~",
    "NATION_NM" : "이탈리아",
    "TY_NM" : "나물/생채/샐러드",
    "COOKING_TIME" : "30분",
    "CALORIE" : "180Kcal",
    "chef" : "오세득",
    "menu" : "해산물샐러드",
    "name" : "엄마손맛 해산물샐러드",
    "steps" : [ 
        "[채소 준비] 양파, 샐러리, 당근을 채썰고 트레비소와 루콜라는 먹기좋은 크기고 자릅니다.", 
        "바질과 이태리파슬리를 다져놓습니다.", 
        "[해산물 준비] 모든 해산물은 깨끗이 씻어 준비합니다.", 
        "냄비에 물을 붓고 적당량의 소금을 넣고 끓인다. 물이 끓으면 해산물을 넣고 살짝 데쳐 꺼내놓는다. 채썰어 놓은 채소도 함께 살짝 데쳐 내어 체에 밭쳐둡니다.", 
        "익은 해산물은 알맞은 크기로 잘라놓고, 채소와 함께 버무려 냉장고에 차갑게 식힙니다.", 
        "[소스 만들기] 믹싱볼에 올리브오일, 레몬즙, 백포도주식초, 다진 바질, 다진 파슬리, 소금, 후춧가루를 넣고 잘 혼합하여 소스를 완성합니다."
    ],
    "ingredients" : [ 
        "삶은 문어살 80g,", 
        "갑오징어 80g,", 
        "꼴뚜기 80g,", 
        "중새우살 6개,", 
        "쭈꾸미 4개,", 
        "참소라살 60g,", 
        "모시조개 10개,", 
        "가리비 2개,", 
        "검은껍질홍합 10개,", 
        "가재새우 2개,", 
        "양파 60g,", 
        "샐러리 40g,", 
        "당근 40g,", 
        "루콜라 40g,", 
        "트레비소 4잎,", 
        "소스 ,"
    ],
    "id" : 26.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed9d"),
    "ROW_NUM" : 27.0,
    "SUMRY" : "재첩은 해감을 잘 한다음 사용하셔야 해요. 그래야 깔끔한 맛을 낼 수 있어요.",
    "NATION_NM" : "한식",
    "TY_NM" : "국",
    "COOKING_TIME" : "30분",
    "CALORIE" : "130Kcal",
    "chef" : "오세득",
    "menu" : "재첩국",
    "name" : "추억의 재첩국",
    "steps" : [ 
        "재첩은 맹물에 한나절 담가 해감시킨 뒤 깨끗이 문질러 씻어 소쿠리에 건져 놓습니다.", 
        "냄비에 물 4컵을 붓고 재첩을 넣어 입이 벌어지도록 끓입니다.", 
        "국물이 끓으면 4cm 길이로 부추를 썰어 넣고 소금으로 간을 하여 잠깐 더 끓인 후 내립니다."
    ],
    "ingredients" : [ 
        "재첩 10컵,", 
        "부추 20g,", 
        "물 4컵,", 
        "소금 약간,"
    ],
    "id" : 27.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed9e"),
    "ROW_NUM" : 28.0,
    "SUMRY" : "감자의 고소함과 도미의 담백함이 어울리는 너무나도 깔끔한 맛의 음식이예요.",
    "NATION_NM" : "이탈리아",
    "TY_NM" : "구이",
    "COOKING_TIME" : "60분",
    "CALORIE" : "225Kcal",
    "chef" : "오세득",
    "menu" : "구운감자와도미구이",
    "name" : "요즘핫한 구운감자와도미구이",
    "steps" : [ 
        "신선한 도미는 비늘을 제거하고 3장뜨기 하여 준비합니다. 감자는 야주 얇게 둥글게 썰어서 준비합니다.", 
        "방울토마토는 반을 잘라둡니다.", 
        "오븐용 종이를 바닥에 깔고 가운데에 올리브오일을 브러쉬를 이용해 잘 바른 후 슬라이스한 감자를 겹겹이 붙여 원형으로 돌려 깔고 위에 소금을 뿌립니다.", 
        "도미를 올리고 다진 향초를 뿌리고 방울토마토를 생선의 가장자리 부분에 놓습니다.", 
        "녹색과 검은색 올리브, 바질을 올리고 생선살 위에 와인을 조금 뿌립니다.", 
        "종이 가장자리에 노른자를 바르고 조금씩 접어 덮고 종이 양쪽은 사탕모양으로 뭉쳐 호일로 끈을 만들어 묶습니다. (종이위에 \"ㅍ\" 모양으로 노른자를 바릅니다. ㅍ모양의 한가운데 내용물이 들어가는것입니다)"
    ],
    "ingredients" : [ 
        "도미 300g,", 
        "감자 1개,", 
        "방울토마토 50g,", 
        "바질 10g,", 
        "블랙올리브 40g,", 
        "케이퍼 15g,", 
        "스위트마조람 20g,", 
        "올리브오일 50g,", 
        "화이트와인 50g,", 
        "계란노른자 적량,", 
        "오레가노 20g,", 
        "그린올리브 10g,"
    ],
    "id" : 28.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5ed9f"),
    "ROW_NUM" : 29.0,
    "SUMRY" : "고기와 버섯이 잘 어우러져 언제나 먹어도 질리지 않고 맛있어서 자주 생각나는 음식이죠~!",
    "NATION_NM" : "한식",
    "TY_NM" : "구이",
    "COOKING_TIME" : "40분",
    "CALORIE" : "320Kcal",
    "chef" : "오세득",
    "menu" : "쇠고기산적",
    "name" : "고급져요 쇠고기산적",
    "steps" : [ 
        "쇠고기는 적간으로 도톰하게 떠서 두드리듯 앞 뒤로 잔 칼집을 넣습니다.", 
        "분량의 갖은 재료를 섞어 고기를 넣고 무쳐 30분 정도 재워 둡니다.", 
        "느타리버섯은 끓는물에 데쳐 식혀서 물기를 꼭 짭니다.", 
        "실파는 6cm 길이로 자르고 느타라버섯은 잘게 찢어 놓습니다.", 
        "햇살담은간장, 파, 마늘, 참기름, 후춧가루로 버섯을 간이 배도록 무칩니다.", 
        "꼬치에 쇠고기, 실파, 느타리버섯을 순서대로 꿰고 마지막엔 쇠고기를 한번 더 꿰어줍니다."
    ],
    "ingredients" : [ 
        "쇠고기 600g,", 
        "햇살담은간장 1큰술,", 
        "실파 1단,", 
        "느타리버섯 300g,", 
        "마늘 약간,", 
        "후춧가루 약간,", 
        "꼬치 8개,", 
        "참기름 약간,", 
        "깨소금 약간,", 
        "설탕 1큰술,", 
        "꿀 1큰술,", 
        "다진파 2큰술,", 
        "다진마늘 3큰술,", 
        "배즙 3큰술,", 
        "생강즙 1큰술,"
    ],
    "id" : 29.0
},
{
    "_id" : ObjectId("5bf4dc69aa33c8cb75d5eda0"),
    "ROW_NUM" : 30.0,
    "SUMRY" : "쫄깃하고 부드러운 쇠고기와 양송이의 만남! 향도 맛도 일품이예요~",
    "NATION_NM" : "한식",
    "TY_NM" : "볶음",
    "COOKING_TIME" : "40분",
    "CALORIE" : "210Kcal",
    "chef" : "맹기용",
    "menu" : "쇠고기양송이볶음",
    "name" : "고급져요 쇠고기양송이볶음",
    "steps" : [ 
        "쇠고기는 잔칼집을 넣어 한 입 크기로 도톰하게 썰어둡니다.", 
        "피망은 한 입 크기로 네모 썰고 양송이는 모양대로 도톰하게 썹니다.", 
        "양파는 피망과 같은 크기로 네모 썰고 마늘은 얇게 편썰기를 합니다.", 
        "기름 두른 프라이팬에 쇠고기, 양파, 마늘을 볶다가 분량의 양념 재료를 넣고 끓으면 피망, 양송이를 넣고 숨이 죽으면 불에서 내립니다.", 
        "소금과 후춧가루를 제외한 분량의 양념재료를 넣어 약불에 졸여 농도가 걸죽해지면 소금과 후춧가루로 간을 해 마무리합니다."
    ],
    "ingredients" : [ 
        "쇠고기 400g,", 
        "양송이버섯 200g,", 
        "피망 4개,", 
        "양파 1개,", 
        "마늘 3톨,", 
        "간장 1큰술,", 
        "물엿 1큰술,", 
        "토마토케첩 4큰술,", 
        "설탕 1큰술,", 
        "소금 약간,", 
        "후춧가루 약간,", 
        "식용유 4큰술,"
    ],
    "id" : 30.0
})

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