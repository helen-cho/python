#문자열 슬라이싱
jumin = '990120-2155011'

#남자?
gender = jumin[7]
result = gender=='1' or gender=='3'
print(f'{gender} 결과는 {result}')

yy=jumin[:2] #인덱스 0부터 인덱스 2전까지(0~1)
print(yy)
mm=jumin[2:4] #인덱스 2부터 인덱스 4전까지(2~3)
print(mm)
dd=jumin[4:6] #인덱스 4부터 인덱스 6전까지(4~5)
print(dd)
print(f'{yy}년{mm}월{dd}일')

print(jumin[-7:])
print(jumin[-1])