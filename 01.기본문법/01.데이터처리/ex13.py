#딕션너리 타입
students={1:'홍길동', 2:'심청이', 3:'강감찬'}
print(students, type(students))
print(students.get(2))
print(students[2])

students[4] = '박명수'  #추가
print(students, type(students))

print(4 in students)

keys = students.keys()
print(keys, type(keys))

values = students.values()
print(values, type(values))

print('박명수' in values)