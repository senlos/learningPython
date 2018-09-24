# before import, install pandas
# pandas manipulate datas as DataFrame, can create from dicionary or import from CSV
import pandas as pd
df = pd.read_csv('data\parks.csv')
print(df)
# indexing DataFrames
# Square brackets can use to get columns
# Single brackets bring out Pandas Series
print(df['Longitude'])
# Double brackets return Pandas DataFrame
print(df[['Park Code','Longitude']])
# Also, Square Brackets can use to get obversations, rows
print(df[0:4])
# loc and iloc
# iloc, integer index based
print(df.iloc[2])
# loc, label based
#print(df.loc['State'])
