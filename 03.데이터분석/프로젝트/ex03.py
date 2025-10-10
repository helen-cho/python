import os
import pandas as pd

file_name = 'c:/python/03.데이터분석/data/학생성적.csv'
score = pd.read_csv(file_name)
cols = score.columns

def sort_list():
    while True:
        score = pd.read_csv(file_name)
        for idx, col in enumerate(cols):
            print(f'{idx}:{col}', end='|')
        print()
        sel = inputNum('선택>')
        if sel=='': break
        score=score.sort_values(cols[sel], ascending=False)
        for idx in score.index:
            row = score.loc[idx]
            for col in cols:
                print(f'{col}:{row[col]}', end=' ')
            print()

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
    score = pd.read_csv(file_name)
    os.system('cls')
    print('-' * 50)
    print('**************** 성 적 관 리 *****************')
    print('-' * 50)
    print('1.등록|2.목록|3.검색|4.삭제|5.수정|0.종료')
    print('-' * 50)
    menu = input('메뉴선택>')
    if menu=='0':
        break
    elif menu=='1':#등록
        index = max(score.index)+1 #저장할 index번호
        no = score['지원번호'].max()+1
        grade=[]
        for idx, col in enumerate(cols):
            if idx==0:
                print(f'지원번호>{no}')
            else:    
                num = inputNum(f'{col}>')
                if num=='': num=0
                grade.append(num)
        score.loc[index]=[no, grade[0], grade[1], grade[2], grade[3], grade[4]]
        score.to_csv(file_name, index=False)
        print('등록성공!')
        input('아무키나 누르세요!')
    elif menu=='2': #목록
        sort_list()
        input('아무키나 누르세요!')
    elif menu=='3': #검색
        while True:
            no = inputNum('지원번호>')
            if no == '':break
            filt = score['지원번호']==no
            idxs = score[filt].index
            if len(idxs)==0:
                print('해당 지원번호가 없습니다!')
            else:
                row = score.loc[idxs[0]]
                for col in cols:
                    print(f'{col}:{row[col]}', end=' ')
                print()
    elif menu=='4':#삭제
        no = inputNum('지원번호>')
        filt = score['지원번호'] == no
        idx = score[filt].index
        if len(idx)==0:
            print('해당 지원번호가 없습니다!')
        else:
            row = score.loc[idx[0]]
            for col in cols:
                print(f'{col}:{row[col]}', end=' ')
            print()
            sel = input('삭제하실래요(Y)>')
            if sel=='Y' or sel=='y':
                score.drop(index=idx[0], inplace=True)
                score.to_csv(file_name, index=False)
                print('삭제완료!')
        input('아무키나 누르세요!')
    elif menu=='5':#수정
        no = inputNum('지원번호>')
        idx = score[score['지원번호']==no].index
        if len(idx)==0:
            print('해당 지원번호가 없습니다!')
        else:
            row = score.loc[idx[0]]
            grade=[]
            for index, col in enumerate(cols):
                if index==0:continue
                num = inputNum(f'{col}:{row[col]}>')
                if num=='':
                    num = row[col]
                grade.append(num)
            sel = input('수정하실래요(Y)>')
            if sel=='Y' or sel=='y':
                score.loc[idx[0]]=[no, grade[0],grade[1],grade[2],grade[3],grade[4]]
                score.to_csv(file_name, index=False)
                print('수정완료!')
        input('아무키나 누르세요!')
    else:
        input('0~5번 메뉴를 선택하세요!')