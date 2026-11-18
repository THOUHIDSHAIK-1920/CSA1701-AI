
diet(diabetes, vegetables).
diet(diabetes, whole_grains).
diet(diabetes, fruits).
diet(hypertension, low_salt_food).
diet(hypertension, vegetables).
diet(obesity, low_calorie_food).
diet(obesity, fruits).
diet(obesity, vegetables).

suggest_diet(Disease, Food) :-
    diet(Disease, Food).
