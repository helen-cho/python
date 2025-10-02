names = ['홍길동', '심청이', '강감찬', '이순신', '성춘향']

no=1
for name in names:
    print(f'{no}:{name}')
    no +=1
print('-' * 50)

for index, name in enumerate(names):
    print(f'{index+1}:{name}')
print('-' * 50)

for index in range(len(names)):
    print(f'{index+1}:{names[index]}')