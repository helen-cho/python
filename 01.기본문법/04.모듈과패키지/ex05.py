import os

path = os.getcwd()
print('현재폴더', path)

check = path + "/04.모듈과패키지/travel2"
if os.path.exists(check):
    os.rmdir(check)
    print("폴더삭제")
else:
    os.makedirs(check)
    print('폴더생성')    
    