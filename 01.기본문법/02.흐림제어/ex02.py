score = int(input('점수>'))
grade=''
#print(type(grade), type(score))
if score >= 90:
    if score >= 95:
        grade = 'A+'
    else:
        grade = 'A0'
elif score >= 80:
    if score >= 85:
        grade = 'B+'
    else:
        grade = 'B0'
elif score >= 70:
    if score >= 75:
        grade = 'C+'
    else:
        grade = 'C0'
elif score >= 60:
    if score >= 65:
        grade = 'D+'
    else:
        grade = 'D0'
else:
    grade = 'F'
print(f'{score}의 학점은 {grade}입니다.')