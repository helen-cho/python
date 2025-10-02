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

def inputNum(title):
    while True:
        str = input(f"{title}>")
        if str.isnumeric():
            return int(str)
        elif str == "":
            return 0
        else:
            print(f"{title}을(를) 숫자로 입력하세요!")

#메뉴출력함수
def menuPrint(title):
    print(f"\n***************{title}******************")
    print("------------------------------------------")
    print("|1.입력|2.검색|3.목록|4.삭제|5.수정|0.종료")
    print("------------------------------------------")