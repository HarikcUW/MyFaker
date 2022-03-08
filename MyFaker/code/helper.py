import pandas as pd
import random
import rstr
from .constants import *

class DataGenerator:
    
    def __init__(self, n, configList) -> None:
        self.__config = configList
        self.__n = MAX_SAMPLE_SIZE if n < 1 or n > MAX_SAMPLE_SIZE else n

    def toUpper(self, txt):
        return txt.upper()

    def isUpper(self, txt):
        return txt.isupper()
    
    # Get n random samples from dataframe
    def getDfElements(self, df, columnList):
        return df.sample(self.__n, replace=REPEAT_SAMPLE)[df.columns[df.columns.isin(columnList)]]
    
    # Rename data frmae columns using dictionary
    def renameDfColumn(self, df, columnRenameDict):
        return df.rename(columns=columnRenameDict)

    ```
    Read column details from configuration and get random samples from the dataframe
    If rename columns specified create a dictionary and rename all columns once 
    ```
    def getRandomDataFromDF(self, df, columns):
        if not columns:
            print("Dict is empty")
        colList = []
        for item in columns:
            colList.append(item['colName'])

        df_t = self.getDfElements(df, colList)
        colListForRename = []
        colListRename = []

        for item in columns:
            if('colRename' in item.keys()):
                if(item['colRename']):
                    colListForRename.append(item['colName'])
                    colListRename.append(item['colRename'])
        renameColumnsDict = dict(zip(colListForRename, colListRename))

        df_t = self.renameDfColumn(df_t, renameColumnsDict)
        return df_t
    
    ```
    For each dataframe listed in configuration get random sample data
    combine data from all data frames and generate single output
    ```
    def getDataFromDF(self, configValue):
        rdf = pd.DataFrame()
        for params in configValue:
            df_Name = params['name']
            df = params['df']
            #df = getDFUsingName(df_List, df_Name)
            columns = params['columns']
            df_t = self.getRandomDataFromDF(df, columns)
            df_t = df_t.reset_index(drop=True)
            rdf = pd.concat([rdf, df_t], axis=1)
        return rdf

    # Generate random value as defined in regula expression using rstr package
    def getRegExData(self,columnInfo):
        data = []
        columnName = columnInfo['colName']
        regExp = columnInfo['regExpression']
        prefix = ""
        if('prefix' in columnInfo.keys()):
            prefix = columnInfo['prefix']
        for i in range(self.__n):
            data_regEx = prefix + rstr.xeger(regExp)
            data.append(data_regEx)
        return pd.DataFrame(data, columns=[columnName])

    ```
    For each column listed in RegulaExpression configuration get random sample data
    combine data from all data frames and generate single output
    ```
    def getDataFromRE(self, expressions):
        rdf = pd.DataFrame()
        for item in expressions:
            columns = item['columns']
            for columnInfo in columns:
                regExData = self.getRegExData(columnInfo)
                regExData = regExData.reset_index(drop=True)
                rdf = pd.concat([rdf, regExData], axis=1)
        return rdf
    
    # Generate random int or float value between start and end value
    def getMetricData(self, columnInfo):
        columnName = columnInfo['colName']
        columnDataType = columnInfo['dataType']
        startValue = 1
        endValue = 100
        if('startValue' in columnInfo.keys()):
            startValue = columnInfo['startValue']
        
        if('endValue' in columnInfo.keys()):
            endValue = columnInfo['endValue']
            
        if(columnDataType == 'float'):
            data = [random.uniform(float(startValue), float(endValue)) for x in range(self.__n)]
        else:
            data = [random.randint(int(startValue), int(endValue)) for x in range(self.__n)]

        return pd.DataFrame(data, columns=[columnName])

    def getMetricsData(self, metricInfo):
        rdf = pd.DataFrame()
        for item in metricInfo:
            columns = item['columns']
            for columnInfo in columns:
                metricData = self.getMetricData(columnInfo)
                metricData = metricData.reset_index(drop=True)
                rdf = pd.concat([rdf, metricData], axis = 1)
        return rdf 
    ```
    Process input configuration and return dataframe with define columns
    expected values for sourceType item :  dataframe, RegularExpression, Metrics
    ```
    def processInput(self):
        df_data = pd.DataFrame()
        re_data = pd.DataFrame()
        m_data = pd.DataFrame()
        final_data = pd.DataFrame()
        try: 
            for cfg in self.__config:
                #print("_____________________")
                #print("sourceType: %s" %(cfg['sourceType']))
                if(cfg['sourceType'] == 'dataframe'):
                    vals = cfg['values']
                    df_data = self.getDataFromDF(vals)
                elif(cfg['sourceType'] == 'RegularExpression'):
                    vals = cfg['values']
                    re_data = self.getDataFromRE(vals)
                elif(cfg['sourceType'] == 'Metrics'):
                    vals = cfg['values']
                    m_data = self.getMetricsData(vals)
                else:
                    raise Exception("Invalid sourcetype value in Config:" + cfg['sourceType'])
                
            df_data = df_data.reset_index(drop=True)
            re_data = re_data.reset_index(drop=True)
            m_data = m_data.reset_index(drop=True)
        
            final_data = pd.concat([df_data, re_data, m_data], axis=1)           
            return final_data
            raise Exception("Error in generating data")
        except Exception as e:
            print("Error: " + repr(e))
