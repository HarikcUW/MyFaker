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

How to use:

- Import MyFaker module:
- Prepare configuration:
```
configList = [{'sourceType':'dataframe'
                  ,'values' : [{'name' : 'df_Country', 'df' : df_Country
                                  ,'columns': [{'colName' : 'CountryCode', 'colRename' : 'CountryISOCode' } 
                                                ,{'colName' : 'Region', 'colRename' : 'CountryRegion'}]
                                }
                               ,{'name' : 'df_Color', 'df' : df_Color
                                  ,'columns': [{'colName' : 'Color', 'colRename' : 'DressColor' }] 
                                }
                               ,{'name' :'df_Product', 'df' : df_Product
                                  ,'columns': [{'colName' : 'ProductId', 'colRename' : 'ProductIdentifier' } 
                                              ,{'colName' : 'ProductName' }]}
                              ]
                }
              ,{'sourceType':'RegularExpression'
                  ,'values' : [{'name' :'Featurs'
                    ,'columns': [{'colName' : 'FirstName', 'prefix' : 'FirstName',  'sufix' : '', 'regExpression' : '[0-9]{2}'  } 
                                ,{'colName' : 'UserEmail', 'regExpression' : '[A-Za-z]{6,10}[0-9]{2}@[a-z]{5}\d\.com' } ]}]
                }
              ,{'sourceType':'Metrics', 'values' : [{'name' :'Featurs'
                ,'columns': [{'colName' : 'SalesQuantity', 'dataType' : 'int', 'startValue' : '10', 'endValue' : '40'  } 
                             ,{'colName' : 'SalesAmount', 'dataType' : 'float', 'startValue' : '10', 'endValue' : '40'  } ]}]
                }
             ]
```
- Generate data:

- Sample Output: MyFaker module returns generated fake data as pandas data frame.
![image](https://user-images.githubusercontent.com/92060455/156967364-718d55e7-2102-494d-bce2-c1f60c922242.png)

## Example:1

## Limitations:
-	rstr module doesn’t support all regular expressions, any unsupported complex expression required own implementation
-	Not using distributes design, so result data set size & volume depends on user system capacity

