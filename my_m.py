import pandas as pd
data1 = pd.read_csv("my_m1.csv")
data1.drop("UserName",axis=1, inplace=True)
data2 = pd.read_csv("my_m2.csv", sep=";",header=None, names=["Age","City", "Gender", "firstlastname","Email","Country"])
data2[["FirstName","LastName"]] = data2["firstlastname"].str.split(expand=True)
data2.drop(["firstlastname"],axis=1,inplace=True)
data3 = pd.read_csv("my_m3.csv", sep="\t",header=0, names=["Gender", "firstlastname","Email","Age","City","Country"])
data3[["FirstName","LastName"]] = data3["firstlastname"].str.split(expand=True)
data3.drop(["firstlastname"],axis=1,inplace=True)
for each in data3.columns:
  data3[each] = data3[each].str.replace('string_|integer_|boolean_|character_','',regex = True)
data3["Age"] = data3["Age"].str.replace('[a-zA-Z]','',regex = True)
all=[data1,data2,data3]
data=pd.concat(all, ignore_index=True)
gender={'0':'Male','M':'Male','1':'Female','F':'Female'}
data['Gender']=data['Gender'].replace(gender)
data['FirstName']=data['FirstName'].str.title()
data['FirstName']=data['FirstName'].str.replace('\\','',regex = True)
data['FirstName']=data['FirstName'].str.replace('""','',regex = True)
data['LastName']=data['LastName'].str.title()
data['LastName']=data['LastName'].str.replace('\\','',regex = True)
data['LastName']=data['LastName'].str.replace('""','',regex = True)
data['Email']=data['Email'].str.lower()
data['Email']=data['Email'].str.replace('_','.',regex = True)
data['City']=data['City'].str.title()
data['Country']='USA'
print(data.head())