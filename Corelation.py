import csv
import plotly_express as px
import numpy as np

with open("CoffeevsSleep.csv") as f:
    df = csv.DictReader(f)

    coffee = []
    sleep = []

    for data in df:
        coffee.append(float(data["Coffee in ml"]))
        sleep.append(float(data["sleep in hours"]))

    corelation = np.corrcoef(coffee, sleep)

    print(corelation[0,1])

    fig = px.scatter(df, x = coffee, y = sleep)

    fig.show()
