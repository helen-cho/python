#list 타입
names = ['홍길동', '심청이', '강감찬']
names.pop(0)
print(1, names, type(names))

names.append('박명수')
print(names, type(names))

names.pop()
print(3, names)

names.insert(1, '박명수')
names.append('박명수')
print(names)

print(names.count('박명수'))
print(names, names[1:3])
print(5,names.remove('심청이'), names)
names[0] = '김길동'
print(6, names)