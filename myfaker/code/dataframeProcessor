import pandas as pd
import rstr
from .constants import *

class DataframeProcessor:

    def __init__(self, n, configValue) -> None:
        self._n = n
        self._configValue = configValue

    def getDfElements(self, df, columnList):
        return df.sample(self._n, replace=REPEAT_SAMPLE)[df.columns[df.columns.isin(columnList)]]

    def renameDfColumn(self, df, columnRenameDict):
        return df.rename(columns=columnRenameDict)

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

    def getDataFromDF(self):
        rdf = pd.DataFrame()
        for params in self._configValue:
            df_Name = params['name']
            df = params['df']
            #df = getDFUsingName(df_List, df_Name)
            columns = params['columns']
            df_t = self.getRandomDataFromDF(df, columns)
            df_t = df_t.reset_index(drop=True)

            rdf = pd.concat([rdf, df_t], axis=1)
        return rdf
