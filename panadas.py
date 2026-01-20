import pandas as pd
data ={
    'Name':['pavan','Kapil','Lalit','Ishan','Om'],
    'Age':[25,None,44,23,None],
    'Salary':[50000,60000,70000,None,None]
}
df=pd.DataFrame(data)
print("Original dataframe")
print(df)
print('Null values')
print(df.isnull())
print(df.isnull().sum())

print('dropping Misiing values')
df_drop = df.dropna()
print(df_drop)
print("Filling values by mean values")
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Salary'].fillna(df['Salary'].mean(),inplace=True)
print(df)