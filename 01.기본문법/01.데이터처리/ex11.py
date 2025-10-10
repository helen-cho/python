#문자열 함수
str = 'python is amazing'
print(1, str.lower())
print(2, str.upper())
print(3, str.capitalize())
print(4, str[0].islower())
print(5, len(str))
print(str.replace('python', '파이썬'))

index = str.index('a')
print(index)
print(str[index:].upper())

print(6, str.find('ab'))
print(7, str.count('i'))