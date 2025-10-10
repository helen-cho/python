#논리연산자 (and, or, not)
age = 19
gender = '남'

#남자면서 나이가 20세이상
result1 = (age >= 20)
print(1, result1)

result2 = (gender == '남')
print(2, result2)

result3 = (result1 and result2)
print(3, result3)