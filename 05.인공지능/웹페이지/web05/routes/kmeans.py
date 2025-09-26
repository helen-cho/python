from flask import Blueprint, render_template, send_file, request
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

bp = Blueprint('kmeans', __name__, url_prefix='/kmeans')

def model_kmeans(K):
    import pandas as pd
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=K, random_state=0)

    dataset = pd.read_csv('data/KMeansData.csv')
    X = dataset.iloc[:, [0,1]].values

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_trans = scaler.fit_transform(X)
    kmeans.fit(X_trans)
    
    centers_org = scaler.inverse_transform(kmeans.cluster_centers_)
    return kmeans, X, X_trans, centers_org

@bp.route('/cluster')
def cluster():
    inertia_list=[] #각 점들에서 중심점까지의 거리 제곱의 합
    for i in range(1, 11, 1):
        kmeans, X, X_trans, centers_org = model_kmeans(i)
        kmeans.fit(X_trans)
        inertia_list.append(kmeans.inertia_)
        
    x = list(range(1, 11, 1))
    y = inertia_list

    plt.figure(figsize=(5, 3))
    plt.plot(x, y, marker='o')
    plt.xticks([x for x in range(1, 11, 1)])
    plt.grid(True, ls='--', lw=0.5)
    plt.xlabel('n_cluster')
    plt.ylabel('inertia')
    #plt.show()
    img = BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@bp.route('/graph')
def graph():
    no = int(request.args['no'])
    print('............', no)
    kmeans, X_org, X_trans, centers_org = model_kmeans(no)
    y_pred = kmeans.fit_predict(X_trans)

    plt.figure(figsize=(5, 3))
    for i in range(no):
        index = np.where(y_pred==i)
        x=X_org[index, 0]
        y=X_org[index, 1]
        plt.scatter(x, y, s=100, ec='black')
        cx = centers_org[i, 0]
        cy = centers_org[i, 1]
        plt.scatter(cx, cy, c='yellow', s=300, ec='black', marker='s')
        plt.text(cx, cy, i, ha='center', va='center')
        plt.xlabel('hour')
        plt.ylabel('score')
    for idx, x in enumerate(X_org):
        plt.text(x[0], x[1], idx, ha='center', va='center', color='white', size=7)
    #plt.show()
    img = BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@bp.route('/data')
def data():
    no = int(request.args['no'])
    kmeans, X_org, X_trans, centers_org = model_kmeans(no)
    y_pred = kmeans.fit_predict(X_trans)

    import pandas as pd
    df = pd.read_csv('data/K-평균.csv')
    df['그룹'] = y_pred
    df = df[:10]
    table = df.to_html(classes='table table-striped table-hover', index=False)
    data = {'table':table}
    return data

@bp.route('/')
def kmeans():
    import pandas as pd
    df = pd.read_csv('data/K-평균.csv')
    df = df[:10]
    table = df.to_html(classes='table table-striped table-hover', index=False)
    return render_template('index.html', pageName='kmeans.html', 
                           title='K-평균', table=table)