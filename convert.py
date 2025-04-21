import pandas as pd


df = pd.read_excel("data.xlsx")


df.to_csv("adult.data.csv", index=False)
