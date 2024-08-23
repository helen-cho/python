import pandas as pd

data = {
 '영화' : ['명량', '극한 직업', '신과 함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번 방의 선물', '암살'],
 '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
 '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], #(단위 : 만 명)
 '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}

def graph1():
  df = pd.DataFrame(data)
  return df

def graph2():
  df = pd.DataFrame(data)
  df_group = df.groupby('개봉 연도')[['관객 수', '평점']].mean()
  return df_group

def graph3():
  df = pd.read_excel('../data/출생아수.xlsx', skiprows=2, nrows=2, index_col=0)
  df.rename(index={'출생아\xa0수':'출생아 수', '합계\xa0출산율':'합계 출산율'}, inplace=True)
  df = df.T
  return df