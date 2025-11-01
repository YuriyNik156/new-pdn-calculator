import pandas as pd
df = pd.read_excel("data/rosstat_data_regions.xlsx")
print(df.columns.tolist())
