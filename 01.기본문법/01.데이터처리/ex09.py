#기본함수
print(1, abs(-5)) #절대값
print(2, pow(4, 3)) #4의 3승
print(3, max(5, 2, 10, 1, 7)) #최댓값
print(4, min(5, 2, 10, 1, 7)) #최솟값
print(5, round(3.14)) #반올림
print(6, round(3.14159, 3)) #반올림해서 3째자리까지 출력

from math import *
print(7, floor(4.99)) #내림
print(8, ceil(3.01)) #올림
print(9, sqrt(16)) #제곱근

from random import *
print(10, random()) #0이상 ~ 1미만
print(10, random() * 10) #0이상 ~ 10미만 (0~9.99999)
print(10, int(random() * 10)) #0 ~ 9까지

print(11, randint(1, 45)) #1 ~ 45번까지