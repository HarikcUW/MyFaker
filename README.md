## Data 515: Software Design for Data Science
[![Build Status](https://api.travis-ci.com/harikcUW/Data515_FakerExt.svg?branch=main)](https://travis-ci.com/github/harikcUW/Data515_FakerExt)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## MyFaker - Fake data generator

## Introduction

Data is king and for almost all the ML models need a large volume of quality data. With increase in privacy and security concerns, companies are restricting customer data usage so it is becoming hard to get good quality data for development and testing. So developers need to generate their own fake data to reflect real world scenarios.   

## Objective

The objective of this project is to build a package to generate random sample data set defined by user
- Flexibility/Configurability: Simple option to provide configuration:, so users need flexibility to generate data based on their conditions.
- Extensibility: Support custom data input: Each field needs different data, for example, medical data is different from sales data. So it is helpful if the package supports bringing their own data.
- Manage relation between data columns
- Generate pandas data frame: Simple to output or re structure in the required format

## Targeted users

This package is helpful for Students, programmers/developers, data scientists and analysts/researchers. They can use this library to generate data for their development and testing. Most data science work is of no use without data, similarly need data for testing as well as to understand any existing package. Researchers often need different data sets to analyze various scenarios.

## Use cases

- David, a student, would like to create a model using eCommerce sales data, but it is hard to find real credit card data for his experiment. He can use this package to generate his own data. He can specify the format of the card and other properties and generate thousands of records in no time.
- Mary, a data scientist, wants to analyze a model's performance and needs quality data. She can use this package to generate necessary data.

## How to Use:
Follow below steps to use the MyFaker package.
- Get latest code from Repo
    ```git clone https://github.com/HarikcUW/Data515_FakerExt.git```
- Check and update constants in constants.py file.
    - You can define Max number of rows and want to repeat any values or not
- Install MyFaker package using setup
    ``` cd MyFaker ```
    ``` python setup.py install ```
- In your script file, Import MyFaker package
- Define data schema and prepare configuration dictionary list
- Create an object and call processInput function with parameters (number of rows to generate, configuration dictionary list)
- Capture return data frame
 
### How to prepare configuration dictionary:
Right now MyFaker generates data using any existing data frame or regular expression.
Config parameter dictionary has following items
- sourceType: What is the source for data, acceptable values: Dataframe, RegularExpression, Metrics
- values: dictionary list to get input, columns and its definition
  - for data frame – include actual data frame, column name, column rename (if different name required in output)
  - for regular expression – include column name, regular expression, prefix, suffix
  - for Metrics – column name, data type (either float or int), start and end values
 
## Example#1: 
### Generate random data using regular expression. In this scenario no input data is required.
```
# import MyFaker package
from MyFaker.code.helper import DataGenerator

# Define config dictionary list. rstr package is used to generate data as defined in regular expression  
configList = [{'sourceType':'RegularExpression', 'values' : [ {'name' :'Featurs'
                ,'columns': [{'colName' : 'FirstName', 'prefix' : 'FirstName',  'sufix' : '', 'regExpression' : '[0-9]{2}'  } 
                             ,{'colName' : 'UserEmail', 'regExpression' : '[A-Za-z]{6,10}[0-9]{2}@[a-z]{5}\d\.com' } ]}]}
              ,{'sourceType':'Metrics', 'values' : [ {'name' :'Featurs'
                ,'columns': [{'colName' : 'SalesQuantity', 'dataType' : 'int', 'startValue' : '10', 'endValue' : '40'  } 
                             ,{'colName' : 'SalesAmount', 'dataType' : 'float', 'startValue' : '10', 'endValue' : '40'  } ]}]}
             ]

# Generate 10 random rows as defined in configList
dg = DataGenerator(10,configList)
dfr = dg.processInput()
print(dfr)

------------------------------------------------------------------
Output:

     FirstName                UserEmail  SalesQuantity  SalesAmount
0  FirstName77      EdazLv72@yhopz7.com             40    15.711852
1  FirstName61    AuueXfjS62@foxfx2.com             12    22.351783
2  FirstName22    EuzYtEDx98@golia4.com             31    37.666205
3  FirstName47   tiJapfiSG18@dzkix6.com             25    11.626575
4  FirstName44  nzHOYMmrnt64@wxzzm0.com             10    14.879003
5  FirstName43      BacxPA97@hgftb6.com             17    27.401190
6  FirstName38      iUcXaW58@duzvu8.com             33    28.602415
7  FirstName95    RMGamxKL56@cguxl0.com             31    33.526898
8  FirstName63   FdzygrzbF49@fpueb5.com             26    28.541427
9  FirstName94    YHDtLYXs56@ibgbb3.com             19    18.988063
```

## Example#2: 
### Generate random data using data frame. In this scenario user can get data from a file or create a list and convert it to data frame. 
```
import pandas as pd 
from MyFaker.code.helper import DataGenerator

df_Color = pd.DataFrame(['Green','Red','Yellow','Blue'], columns = ['Color'])

configList = [{'sourceType':'dataframe', 'values' : [ {'name':'df_Color', 'df': df_Color
                   ,'columns': [{'colName':'Color', 'colRename':'TagColor', 'prefix':'' } 
                                ]}]}
              ,{'sourceType':'Metrics', 'values':[{'name':'Featurs'
                ,'columns': [{'colName':'SalesQuantity', 'dataType':'int', 'startValue':'10', 'endValue':'40'} ]}]}
             ]

dg = DataGenerator(10,configList)
dfr = dg.processInput()
print(dfr)

------------------------------------------------------------------
Output:
  TagColor  SalesQuantity
0   Yellow             15
1     Blue             37
2      Red             32
3   Yellow             24
4    Green             18
5   Yellow             13
6   Yellow             33
7      Red             27
8      Red             26
9     Blue             10

```

## Limitations:

- rstr module doesn’t support all regular expressions, any unsupported complex expression required own implementation
- Not using distributes design, so result data set size & volume depends on user system capacity

## Future Extensions:

- Simplify how user can pass configuration, something like user pass (categorical, categorical, categorical, int, int, float)
- Extend to generate how many distinct values should generate for each categorical feature
- For Metrics – right now we generate random number, extend it to support any specific distribution

## Summary:

Data is required for almost all projects and often developers need to generate data themselves. The MyFaker package can help to generate fake data using either from another data frame and regular expression. 

## References:

- https://github.com/leapfrogonline/rstr
