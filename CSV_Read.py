import pandas as pd


file=str(input())

df = pd.read_csv(file)

print(df.to_string())