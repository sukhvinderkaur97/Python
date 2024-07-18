import pandas as pd
import numpy as np

column_names = ['Id', 'Name', 'Age']
df = pd.read_csv('data.csv', names= column_names, header=0)
df.head()
# df = pd.read_csv('data.csv')
# print(df)

df = df.drop([2, 6])

age = [20, 19, 20, 19, 26, 22, 20, 21]

mean_age = np.mean(age)
print(mean_age)

age = [mean_age if pd.isna(x) else x for x in age]

df.to_csv('updated_data.csv', index=False)

print("Mean Age:", mean_age)
print("\nUpdated Data:")
print(df)




