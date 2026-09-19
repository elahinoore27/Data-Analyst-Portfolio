import pandas as pd 
#1. Create DataFrame
# df=pd.DataFrame([1,2,3,],columns=['number'],index=['a','b','c'])
# print(df)

# print(type(df)) 

data={
    'Name':['Noore','Elahi','Shane','fazle','Saba'],
    'Age':[20,22,32,5,2],
    'Salary':[2466,75,7,4,7]
}
df=pd.DataFrame(data,index=['a','b','c','d','e'])
# print(df)


# ## Basic Dataframe understandin

# print(df.head(2)) #top 2 row
# print(df.tail(2)) # last 2 row

# print(df.shape)  # it is give no of row and columns

# df1=df.rename(columns={'Salary':'Monthly_salary'},inplace=True) #how rename column
# print(df1)

# print(df.info())  #it tells infromation of data

# print(df.describe())  # it is tell stastical value

##How to import and export csv file in pandas load and save

# df.to_csv('test.csv',index=False)   # how create csv file in pandas export
# print(df)

# load_df=pd.read_csv('test.csv')  #how load csv in pandas import
# print(load_df)

## Row andcolumn selection


# print(df[['Name']])
# print(df[['Name','Salary']])

# print(df.loc[df.Name=='Noore'])   # this is  label index based name
# print(df.loc[(df.Name=='Noore') & (df.Age>=12)])

###iloc this is index value based

# print(df.iloc[0])  ##[start:end:step]
# print(df.iloc[0:3]) ## butin goes 0 to 2 not 3
# print(df.loc[0:2])  in loc it goes 0 to 2


##Filter Dataframe

# print(df['Age']>12)   ##it give boolean value

# print(df[df['Age']>12])  ##it's give value 

# print(df[(df['Age']>12) & (df['Salary']>7)])

# print(df.where(df['Age']>12,other="Not"))  #if you don't want change then use where


### Add column

# df['Team']=['Cricket','tennia','football','hockey','table-tennis']
# print(df)

# df['Bonus']=df['Salary']*0.2
# print(df)

 ##Add Row

# df.loc[len(df)]=['Sayyad',20,45634]
# print(df)
# print(len(df))

###update  value

# df.loc[0,'Salary']=50000
# print(df)

# df.iloc[0, df.columns.get_loc('Salary')] = 50000
# print(df)

# df.loc[df.Name=='Noore','Salary']=90000
# print(df)


### delete row and column values


# df.drop(df[df['Name'] == 'Saba'].index, inplace=True)  # delete specifice index that's why use index
# print(df)
# df.drop('Salary',inplace=True,axis=1)   #inplace=True means modify the original df directly
# print(df)

# df.drop(['Name','Age'],inplace=True,axis=1) 
# print(df)

# df.drop(1, inplace=True)
# print(df)


###Sorting 

# f=df.sort_values('Salary') #assending
# print(f)

# f1=df.sort_values('Salary',ascending=False)
# print(f1)