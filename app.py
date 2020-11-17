import flask
from flask import Flask, render_template, redirect, request
from datetime import datetime, timedelta
import pandas as pd
import pickle
import os
from os import listdir

pat = r"C:\Users\Sandeep\PycharmProjects\series1\data\pickle files"
list_of_files = listdir(r"C:\Users\Sandeep\PycharmProjects\series1\data\pickle files")
list_of_col = ["N02BE", "N05B", "N05C", "R03", "R06"]
m = {}
for i in range(5):
    m[list_of_col[i]] = list_of_files[i]

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        d1 = request.form.get("d1")
        pt = datetime.strptime(d1, "%Y-%m-%d")
        dt = datetime.strptime("10/8/2019", "%d/%m/%Y")
        x = int((pt.timestamp() - dt.timestamp()) / 86400)
        m1 = request.form.get("Medicine")
        s = os.path.join(pat, m[m1])
        pick = open(s, "rb")
        k = pickle.load(pick)
        list1 = k.forecast(x)
        pd.options.display.float_format = '${:,.2f}'.format
        df = pd.DataFrame(list1)
        df = df.applymap('{:,.2f}'.format)
        #print(df)
        return render_template("success.html", data=df.iloc[-1],pt=pt, m1=m1)
    return render_template("index.html")
    '''date=d1
    product=m1
    date = datetime.strptime(d1, "%Y-%m-%d")
    last_date = datetime.strptime("10/8/2019", "%d/%m/%Y")
    x1 = int((pt.timestamp() - dt.timestamp()) / 86400)
    product = request.form.get("Medicine")
    modelfile = os.path.join(pat, m[product])
    pickfile = open(modelfile,"rb")
    model = pickle.load(pickfile)'''

@app.route("/multiple_products", methods=['POST', 'GET'])
def total():
    if request.method == "POST":
        #r1 = request.form.get("M01AB")
        #r2 = request.form.get("M01AE")
        #r3 = request.form.get("N02BA")
        r4 = request.form.get("N02BE")
        r5 = request.form.get("N05B")
        r6 = request.form.get("N05C")
        r7 = request.form.get("R03")
        r8 = request.form.get("R06")
        rd1 = request.form.get("rd1")
        products = {}
        lista = [r4, r5, r6, r7, r8]
        global count
        count = 0
        rd1 = datetime.strptime(rd1, "%Y-%m-%d")
        dt = datetime.strptime("10/8/2019", "%d/%m/%Y")
        x1 = int((rd1.timestamp() - dt.timestamp()) / 86400)
        for i in lista:
            if i==None:
                count = count+0
            else:
                s = os.path.join(pat, m[i])
                pick = open(s, "rb")
                k = pickle.load(pick)
                list1 = k.forecast(x1)
                s1 = list1.iloc[-1]
                count = count+s1

        return render_template("results.html", r1=round(count,2), date = rd1, totalp = lista)

    return render_template("index1.html")




if __name__ == "__main__":
    app.run(debug=True)
