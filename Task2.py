# 2. Напишите программу для 
# проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def InputNum(x):
    xyz = ['X','Y','Z']
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a

def ChekPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

stat = InputNum(3)

if ChekPredicate(stat) == True:
    print(f'При значениях X = {stat[0]}, Y = {stat[1]}, Z = {stat[2]}, утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истино')
else:
    print(f'При значениях X = {stat[0]}, Y = {stat[1]}, Z = {stat[2]}, утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ложно') 