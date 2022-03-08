import pandas as pd
import rstr

class RegExProcessor:

    def __init__(self, n, expressions) -> None:
        self._n = n
        self._expressions = expressions

    def getRegExData(self,columnInfo):
        data = []
        columnName = columnInfo['colName']
        regExp = columnInfo['regExpression']
        prefix = ""
        if('prefix' in columnInfo.keys()):
            prefix = columnInfo['prefix']
        for i in range(self._n):
            data_regEx = prefix + rstr.xeger(regExp)
            data.append(data_regEx)
            
        return pd.DataFrame(data, columns = [columnName])

    def getDataFromRE(self):
        rdf = pd.DataFrame()
        for item in self._expressions:
            columns = item['columns']
            for columnInfo in columns:
                regExData = self.getRegExData(columnInfo)
                regExData = regExData.reset_index(drop=True)
                rdf = pd.concat([rdf, regExData], axis=1)
            
        return rdf
