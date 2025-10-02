sum=0
while True:
    num = input('숫자입력>')
    if num == '':
        print('프로그램종료')
        break
    sum += int(num)

print('합계:', sum)