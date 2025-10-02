import os
import pandas as pd
score_name = 'c:/python/03.데이터분석/data/학생성적.csv'
score = pd.read_csv(score_name)
cols = score.columns

def inputNum(title):
    while True:
        num = input(title)
        if num=='':
            return ''
        elif not num.isnumeric():
            print('점수는 숫자로입력하세요.')
        else:
            return int(num)
while True:
    os.system('cls')
    print('-' * 50)
    print('************* 성 적 관 리 **************')
    print('-' * 50)
    print('1.등록|2.목록|3.검색|4.삭제|5.수정|0.종료')
    print('-' * 50)
    menu = input('메뉴선택>')
    if menu=='0':
        break
    elif menu=='1': #등록
        idx = len(score)
        no = score['지원번호'].max()+1
        print(f'지원번호>{no}')
        grade=[]
        for index, col in enumerate(cols):
            if index==0: continue
            num = inputNum(col + '>')
            if num=='': num=0
            grade.append(num)
        score.loc[idx]=[no, grade[0], grade[1], grade[2], grade[3], grade[4]]
        score.to_csv(score_name, index=False)
        print('등록완료!')
        input('아무키나 누르세요!') 
    elif menu=='2':
        score = pd.read_csv(score_name)
        cols = score.columns
        for idx in range(len(score)):
            row = score.loc[idx]
            for col in cols:
                print(f'{col}:{row[col]} ' , end='')
            print()    
        input('아무키나 누르세요!') 
    elif menu=='3':
        for index, col in enumerate(cols):
            print(f'{index}.{col}', end='|')
        input('>')
        input('아무키나 누르세요!')   
    elif menu=='4': #삭제
        idx = input('지원번호>')
        idx = int(idx)
        filt = score['지원번호']==idx
        search = score[filt].index
        if len(search)==0:
            print('삭제할 지원자가 없습니다.')
        else:
            row=score[filt].loc[search[0]]
            for col in cols:
                print(f'{col}:{row[col]}')
            sel = input('삭제하실래요(Y)>')
            if sel=='Y' or sel=='y':
                score.drop(index=search[0], inplace=True)
                score.to_csv(score_name, index=False)
                print('삭제완료!')
        input('아무키나 누르세요!')
    elif menu=='5':
        idx = input('지원번호>')
        idx = int(idx)
        filt = score['지원번호']==idx
        search = score[filt].index
        if len(search)==0:
            print('수정할 지원자가 없습니다.')
        else:
            row=score[filt].loc[search[0]]
            grade = []
            for index, col in enumerate(cols):
                if index==0: continue
                num=inputNum(f'{col}:{row[col]}>')
                if num=='':
                    num=row[col]
                grade.append(num)
            score.loc[search[0]]=[idx, grade[0], grade[1], grade[2], grade[3], grade[4]]
            score.to_csv(score_name, index=False)
            print('수정완료!')
        input('아무키나 누르세요!')
    else:
        input('0~5번을 누르세요!')            