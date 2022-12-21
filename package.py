import pandas as pd

dat={
    'name':['sampath','sai','aparna','Jahnavi'],
    'age':[28,21,25,21],
    'dept':['hr','dev','testing','operation']
}
#row_label=[1,2,3,4]
df =pd.DataFrame(data=dat)
print(df)
print(df.size)
print(df.shape)
print(df.head(3))
print(df.tail(2))
print(df.name)
#Names=df['name']
#print(Names)
print(df.tail(1))
print(df.age)
print(df.name)
Names=df['name']
print(Names)
print(df.loc[0])
#df_csv=df.read_csv('r c:\Users\User\Document\TESTINGITCRATSINTRANETPORTAL.csv')
#print(df_csv)
print(df.columns)
print(df.memory_usage())