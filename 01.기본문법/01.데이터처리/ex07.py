#나이, 성별 입력 받아서 여탕에 들어갈수 있을까요?
#조건: 여자이거나, 남자이면서 4세미만
print('여탕에 입장가능?')
age = int(input('나이>'))
gender = input('성별>')
result = (gender=='여') or (gender=='남' and age < 4)
print(f'결과는 {result}입니다.')

print('-' * 50)
print('남탕에 입장가능?')
#조건: 남자이거나, 여자이면서 3세미만
result = (gender =='남') or (gender=='여' and age <3)
print(f'결과는 {result}입니다.')