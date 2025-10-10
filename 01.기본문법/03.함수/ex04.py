from function import grade, isNumber


while True:
    kor = input("국어>")
    if isNumber(kor):
        break

while True:
    eng = input("영어>")
    if isNumber(eng):
        break

while True:
    mat = input("수학>")
    if isNumber(mat):
        break

avg = (int(kor)+int(mat) + int(eng))/3
level = grade(avg)
print(f"평균:{avg:.2f} 평점:{level}")