import pandas as pd 
from MyFaker.code.helper import DataGenerator

df_Color = pd.DataFrame(['Green','Red','Yellow','Blue'], columns = ['Color'])

#df_List = [df_Country,df_Product,df_Color]

configList = [{'sourceType':'dataframe', 'values' : [ {'name' : 'df_Color', 'df' : df_Color
                   ,'columns': [{'colName' : 'Color', 'colRename' : 'DressColor', 'prefix' : '' } 
                                ]}]}
              ,{'sourceType':'RegularExpression', 'values' : [ {'name' :'Featurs'
                ,'columns': [{'colName' : 'FirstName', 'prefix' : 'FirstName',  'sufix' : '', 'regExpression' : '[0-9]{2}'  } 
                             ,{'colName' : 'UserEmail', 'regExpression' : '[A-Za-z]{6,10}[0-9]{2}@[a-z]{5}\d\.com' } ]}]}
              ,{'sourceType':'Metrics', 'values' : [ {'name' :'Featurs'
                ,'columns': [{'colName' : 'SalesQuantity', 'dataType' : 'int', 'startValue' : '10', 'endValue' : '40'  } 
                             ,{'colName' : 'SalesAmount', 'dataType' : 'float', 'startValue' : '10', 'endValue' : '40'  } ]}]}
             ]

dg = DataGenerator(10,configList)
dfr = dg.processInput()
print(dfr)