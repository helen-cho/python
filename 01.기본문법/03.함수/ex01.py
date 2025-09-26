#함수정의
def grade(score):
    grade=""
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=60:
        grade="D"
    else:
        grade="F"
    return grade

while True:
    score = input("점수:종료0>")
    if not score.isnumeric():
        print("숫자로 입력하세요!")
        continue
    if score=="0":
        print("프로그램을 종료합니다.")
        break
    else:
        grade = grade(int(score))
        print(grade)