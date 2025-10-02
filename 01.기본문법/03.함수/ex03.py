#숫자인 체크 함수
def isNumber(str):
    if str.isnumeric():
        return True
    else:
        print("숫자로 입력하세요!")
        return False
    
#학점구하기 함수
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
    score = input("점수>")
    if score=="":
        break
    if isNumber(score):
        level = grade(int(score))
        print(f"평점:{level}")
