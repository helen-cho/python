students=[
    {"no":"1번", "이름":"홍길동", "국어":90, "영어":95, "수학": 98},
    {"no":"2번", "이름":"강감찬", "국어":80, "영어":99, "수학": 96},
    {"no":"3번", "이름":"이순신", "국어":92, "영어":85, "수학": 78},
    {"no":"4번", "이름":"성춘향", "국어":78, "영어":55, "수학": 67},
    {"no":"5번", "이름":"이몽룡", "국어":95, "영어":85, "수학": 87},
 ]

#학점구하기
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

for s in students:
    tot = s["국어"]+s["영어"]+s.get("수학")
    avg = tot/3
    level = grade(avg)
    print(s["no"], s["이름"], tot, f"{avg:.2f}", level)