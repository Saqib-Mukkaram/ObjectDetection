import pandas as pd
import matplotlib
#importing CSV
Games_data = pd.read_csv("games.csv",index_col=False)

# print( Games_data.dtypes) 
# print(Games_data.columns) 
# print(Games_data.index) 
# print(Games_data.describe())
# print(Games_data.info())
# print(Games_data.head(3))
# print(Games_data.tail(3))
# print(Games_data.loc[5])
#print(Games_data.Title)
# print(Games_data[Games_data["Rating"] > 4.5 ].head(10))

#crosstab = pd.crosstab(Games_data["Title"], Games_data["Rating"])
#print(f"{crosstab.all()}")
Games_data["Rating"].plot()

