#딕션너리 (dict)
students= {1:'홍길동', 2:'강감찬', 3:'이순신'}
print(1, type(students))

#검색
print(2, students.get(4), students[2])
#입력
students[5]='유재석'
print(3, students)
#수정
students[1]='김길동'
print(4, students)
#삭제
students.pop(2)
print(5, students)
#전부삭제
students.clear()
print(6, students)