#if
# gender = input('성별을 입력하세요(1/2)>')
# if gender=='1':
#     print('남자입니다.')
# else:
#     print('여자입니다.')

num1 = input('숫자1>')
num2 = input('숫자2>')
num1 = int(num1)
num2 = int(num2)

if num1 > num2:
    print(f'{num1}이(가) {num2} 보다 큽니다.')
elif num1 == num2:
    print(f'{num1}과 {num2}는 같습니다.')
else:
    print(f'{num1}이(가) {num2}보다 작습니다.')