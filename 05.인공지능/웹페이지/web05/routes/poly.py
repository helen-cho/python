from flask import Blueprint, render_template, request
bp = Blueprint('poly', __name__, url_prefix='/poly')


def model_poly():
    import pandas as pd
    dataset = pd.read_csv('data/PolynomialRegressionData.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    from sklearn.preprocessing import PolynomialFeatures
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)

    from sklearn.linear_model import LinearRegression
    poly_reg = LinearRegression()
    poly_reg.fit(X_poly, y)
    return poly_reg

@bp.route('/data')
def data():
    model = model_poly()

    import pandas as pd
    df = pd.read_csv('data/다항회귀.csv')
    X = df.iloc[:, 1:].values

    from sklearn.preprocessing import PolynomialFeatures
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)
    y_pred=model.predict(X_poly)
    df['예측점수'] = y_pred
    df['예측점수']=df['예측점수'].apply(lambda x: round(x, 2))
    df.rename(columns={'name':'이름', 'hour':'공부시간'}, inplace=True)
    return df.to_html(classes='table table-striped table-hover', index=False)

@bp.route('/predict')
def predict():
    model = model_poly()
    hour = float(request.args['hour'])
    
    from sklearn.preprocessing import PolynomialFeatures
    poly = PolynomialFeatures(degree=2)
    hour_poly = poly.fit_transform([[hour]])
    pred = model.predict(hour_poly)
    return f'{pred[0]:.2f}'

@bp.route('/')
def poly():
    return render_template('index.html', pageName='poly.html', title='다항회귀')