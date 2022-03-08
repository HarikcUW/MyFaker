import pandas as pd
import random

class MetricsProcessor:

    def __init__(self, n, metricInfo) -> None:
        self._n = n
        self._metricInfo = metricInfo

    def getMetricData(self,columnInfo):
        columnName = columnInfo['colName']
        columnDataType = columnInfo['dataType']
        startValue = 1
        endValue = 100
        if('startValue' in columnInfo.keys()):
            startValue = columnInfo['startValue']
        
        if('endValue' in columnInfo.keys()):
            endValue = columnInfo['endValue']
            
        if(columnDataType == 'float'):
            data = [random.uniform(float(startValue),float(endValue)) for x in range(self._n)]
        else:
            data = [random.randint(int(startValue),int(endValue)) for x in range(self._n)]

        return pd.DataFrame(data, columns = [columnName])

    def processMetrics(self):
        rdf = pd.DataFrame()
        for item in self._metricInfo:
            columns = item['columns']
            for columnInfo in columns:
                metricData = self.getMetricData(columnInfo)
                metricData = metricData.reset_index(drop = True)
                rdf = pd.concat([rdf, metricData], axis = 1)
            
        return rdf 
