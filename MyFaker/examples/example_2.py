```
Generate fake data with MyFaker library using list and regular expressions
This exampe will return random text for FirstName and Email as defined in regular expression 
For Metrics, it will return randon value between start and end values. 
```
import pandas as pd 
from MyFaker.code.helper import DataGenerator

df_Color = pd.DataFrame(['Green','Red','Yellow','Blue'], columns = ['Color'])

configList = [{'sourceType' : 'dataframe', 'values' : [{'name' : 'df_Color','df' : df_Color
                   ,'columns' : [{'colName' : 'Color','colRename' : 'TagColor', 'prefix' :  ''}]}]}
              ,{'sourceType' : 'RegularExpression', 'values' : [{'name' : 'Featurs'
                ,'columns' : [{'colName' : 'FirstName', 'prefix' : 'FirstName', 'sufix' : '', 'regExpression' : '[0-9]{2}'} 
                             ,{'colName' : 'UserEmail', 'regExpression' : '[A-Za-z]{6,10}[0-9]{2}@[a-z]{5}\d\.com'}]}]}
              ,{'sourceType' : 'Metrics', 'values' : [{'name' : 'Featurs'
                ,'columns' : [{'colName' : 'SalesQuantity', 'dataType' : 'int', 'startValue' : '10', 'endValue' : '40'} 
                             ,{'colName' : 'SalesAmount', 'dataType' : 'float', 'startValue' : '10', 'endValue' : '40'}]}]}]

fakeData = DataGenerator(10, configList)
df_fakeData = fakeData.processInput()
print(df_fakeData)
