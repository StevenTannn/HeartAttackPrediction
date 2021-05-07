from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import StandardScaler
from matplotlib.figure import Figure
import seaborn as sns
import numpy as np
from io import BytesIO
import base64
from joblib import load

sns.set_style('darkgrid')
app = Flask(__name__, template_folder='template')
attributes = ['anaemia','diabetes','high_blood_pressure','sex','smoking']
df = pd.read_csv("../heart_failure_clinical_records_dataset.csv")

def visualizeDataPreview():
    fig = Figure(figsize=(15, 15))
    ax = fig.subplots(3, 2)
    ax = np.array(ax).flatten()
    i = 0
    for attrib in [*attributes,'DEATH_EVENT']:
        plot = sns.countplot(x=df[attrib], ax=ax[i])
        grouped = df[attrib].value_counts()
        j = 0
        for key in grouped.keys():
            plot.text(j, 100, grouped[key],
                      color="black", ha="center", fontsize=12)
            j += 1
        i += 1
    buf = BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png")
    fig.clear()
    return base64.b64encode(buf.getbuffer()).decode("ascii")


def getComparisonData(key):
    df_hp = df.groupby([key, 'DEATH_EVENT']).size()
    comparisons = {}
    for i in df[key].unique():
        total = sum(df_hp[i])
        temp = []
        for y in df_hp[i]:
            temp.append([y, round(y / total * 100, 2)])
        comparisons[i] = temp
    return comparisons


def getComparisonBar(key):
    fig = Figure()
    ax = fig.subplots(1, 1)
    sns.countplot(data=df, x=key, hue='DEATH_EVENT', ax=ax)
    buf = BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png")
    fig.clear()
    return base64.b64encode(buf.getbuffer()).decode("ascii")


def getComparisonSummary(comparison, labels):
    result = ""
    for label in labels:
        result += f"<strong>{label}</strong><br/>"
        temp = comparison[label]

        try:
            result += f"no death: {temp[0][0]:5} , {temp[0][1]:5}%<br/>"
            result += f"death: {temp[1][0]:5}  , {temp[1][1]:5}%<br/>"
        except:
            result += str(temp)
    return result


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        return predictController()
    elif request.method == 'GET':
        return dashboardController()


def dashboardController():
    fig1 = visualizeDataPreview()
    comparisons = {}
    for attrib in attributes:
        cData = getComparisonData(attrib)
        comparisons[attrib] = {
            "summary" : getComparisonSummary(cData, df[attrib].unique()),
            "image": getComparisonBar(attrib)
        }
    return render_template("index.html",df=df,attributes=attributes,fig1=fig1,comparisons=comparisons)


def predictController():
    labels = ['age','ejection_fraction','serum_creatinine','serum_sodium','time']
    value = []
    for label in labels:
        value.append(float(request.form[label]))
    sc=load('std_scaler.bin')
    value1 = sc.transform([value])
    model = load('heart_attack.pkl')
    print(value)
    print(value1)
    prediction = model.predict(value1)
    print(prediction)
    if prediction[0] == 0:
        return "No Heart Attack"
    else:
        return "Heart Attack"
