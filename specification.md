======================NRM DB data specification====================== 

recipe_doc = {"Id":recipe.id, "Name":recipe.name, "Chef":recipe.chef,"Menu":recipe.menu, "steps":recipe.steps}

recipe.id: int 
recipe.name : string 
recipe.chef : string
recipe.menu : string
recipe.steps : [string, string, ... ]

======================API data specification======================


데이터명 : 레시피 기본정보
번호	컬럼명	컬럼ID	컬럼설명
1	레시피 코드	RECIPE_ID	레시피 코드
2	레시피 이름	RECIPE_NM_KO	레시피 이름
3	간략(요약) 소개	SUMRY	간략(요약) 소개
4	유형코드	NATION_CODE	유형코드
5	유형분류	NATION_NM	유형분류
6	음식분류코드	TY_CODE	음식분류코드


데이터명 : 레시피 재료정보
번호	컬럼명	컬럼ID	컬럼설명
1	레시피 코드	RECIPE_ID	레시피 코드
2	재료순번	IRDNT_SN	재료순번
3	재료명	IRDNT_NM	재료명
4	재료용량	IRDNT_CPCTY	재료용량
5	재료타입 코드	IRDNT_TY_CODE	재료타입 코드
6	재료타입명	IRDNT_TY_NM	재료타입명

데이터명 : 레시피 과정정보
번호	컬럼명	컬럼ID	컬럼설명
1	레시피 코드	RECIPE_ID	레시피 코드
2	요리설명순서	COOKING_NO	요리설명순서
3	요리설명	COOKING_DC	요리설명
4	과정 이미지 URL	STRE_STEP_IMAGE_URL	과정 이미지 URL
5	과정팁	STEP_TIP	과정팁    