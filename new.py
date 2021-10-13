import csv
import plotly.figure_factory as pff
import pandas as pd

df = pd.read_csv("data.csv")

figure = pff.create_distplot([df["Average"].tolist()],["average"],show_hist=False)
figure.show()