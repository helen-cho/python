def createModel():
    #학습 데이터 생성
    import pandas as pd
    df_train = pd.read_csv('data/감성분석/train.csv')
    df_train = df_train[:1000]

    #한글 형태소 분리함수
    from konlpy.tag import Okt
    okt = Okt()
    def okt_tokenizer(text):
        tokens = okt.morphs(text)
        return tokens

    #document 벡타화
    from sklearn.feature_extraction.text import TfidfVectorizer
    vector = TfidfVectorizer(tokenizer=okt_tokenizer, ngram_range=(1, 2), 
                            min_df=3, max_df=0.9, token_pattern=None)
    vector.fit(df_train['document'])
    vector_trans = vector.transform(df_train['document'])

    #모델생성후 모델학습
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(C=10, max_iter=100)
    model.fit(vector_trans, df_train['label'])

    return vector, model