temp = [i for i in range(1, 11)]
print(temp, type(temp))

even = [i for i in temp if i%2==0]
print(even)

odd = [i for i in temp if i%2==1]
print(odd)

result = ['짝수' if i%2==0 else '홀수' for i in temp]
print(result)

names = ['Iron man', 'Chris', 'Justin Hwang']
names = [len(name) for name in names]
print(names)