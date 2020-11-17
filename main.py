import numpy as np
import pandas as pd
import statsmodels
import pmdarima

df = pd.read_csv(r"C:\Users\Sandeep\PycharmProjects\series1\data\salesdaily.csv", parse_dates=True)
df["datum"] = pd.to_datetime(df["datum"])
df.set_index("datum")
from statsmodels.tsa.seasonal import seasonal_decompose
from pmdarima import auto_arima
fse=seasonal_decompose(df["M01AB"],period=7)
#todo check all seassonal decompose
#todo import autoarima and check pdf PDF
#todo create sarimax to all variables
#todo import sklearn and trantest split
#todo fit and transform to all variables and forecast
#todo create models
#todo download pickles
#todo create a flask website
#todo accommodate all pickles in flask
#todo export in heroku
datac = list(['M01AB', 'M01AE', 'N02BA', 'N02BE', 'N05B', 'N05C', 'R03', 'R06'])
#def fun(lable):
#    auto_arima(df[lable], m=7)

import pickle
pick = open(r"C:\Users\Sandeep\PycharmProjects\series1\data\pickle files\result1.pickle", "rb")
k=pickle.load(pick)
l = k.forecast(10)
print(type(l))
list_of_col = ["M01AB", "M01AE", "N02BA", "N02BE", "N05B", "N05C", "R03", "R06"]
products = dict()
lista = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(8):
    products[list_of_col[i]] = lista[i]
print(products)
print(products.items())




