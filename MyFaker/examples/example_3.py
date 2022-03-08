import pandas as pd 
import os
from MyFaker.code.helper import DataGenerator

df_Color = pd.DataFrame(['Green','Red','Yellow','Blue'], columns = ['Color'])

my_path = os.path.abspath(os.path.dirname(__file__))
df_Product_Path = os.path.join(my_path, "data/ProductInfo.csv")
df_Country_Path = os.path.join(my_path, "data/CountryInfo.csv")

print("df_Product_Path : %s" %(df_Product_Path))
df_Product= pd.read_csv(df_Product_Path)
df_Country= pd.read_csv(df_Country_Path)

configList = [{'sourceType':'dataframe', 'values':[{'name':'df_Country', 'df':df_Country
                   ,'columns':[{'colName':'CountryCode', 'colRename':'CountryISOCode', 'prefix':''} 
                                ,{'colName':'Region','colRename':'CountryRegion'}]}
              ,{'name':'df_Color', 'df':df_Color
                   ,'columns':[{'colName':'Color', 'colRename':'DressColor', 'prefix':''}]}
              ,{'name':'df_Product', 'df':df_Product
                ,'columns':[{'colName':'ProductId', 'colRename':'ProductIdentifier', 'prefix':''} 
                             ,{'colName':'ProductName' }]}]}
              ,{'sourceType':'RegularExpression', 'values':[{'name':'Featurs'
                ,'columns':[{'colName':'FirstName', 'prefix':'FirstName', 'sufix':'', 'regExpression':'[0-9]{2}'} 
                             ,{'colName':'UserEmail', 'regExpression':'[A-Za-z]{6,10}[0-9]{2}@[a-z]{5}\d\.com'}]}]}
              ,{'sourceType':'Metrics', 'values':[{'name':'Featurs'
                ,'columns':[{'colName':'SalesQuantity', 'dataType':'int', 'startValue':'10', 'endValue':'40'} 
                             ,{'colName':'SalesAmount', 'dataType':'float', 'startValue':'10', 'endValue':'40'}]}]}
             ]

fakeData = DataGenerator(10, configList)
df_fakeData = fakeData.processInput()
print(df_fakeData)
