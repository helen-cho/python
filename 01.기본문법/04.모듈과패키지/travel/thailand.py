def trip1():
     print('[태국 패지지 3박5일] 방콕, 파타야 여행(야시장 투어) 50만원')

def trip2():
     print('[태국 패지지 3박5일] 치양마이 1달 살기 500만원')

if __name__ == '__main__':
    print('thailand 모듈을 직접 실행')
    print('이 문장은 모듈을 직접 실행할 때만 실행됩니다.')
    trip1()
else:
    print('thailand 외부에서 모듈 호출')