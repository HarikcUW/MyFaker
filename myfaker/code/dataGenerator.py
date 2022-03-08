import pandas as pd

from .constants import *
from .regExProcessor import RegExProcessor
from .metricsProcessor import MetricsProcessor
from .dataframeProcessor import DataframeProcessor

class DataGenerator:


    def __init__(self, n, configList) -> None:
        self.__config = configList
        self.__n = MAX_SAMPLE_SIZE if n < 1 or n > MAX_SAMPLE_SIZE else n

    def generateData(self):
        df_data = pd.DataFrame()
        re_data = pd.DataFrame()
        metrics_data = pd.DataFrame()
        final_data = pd.DataFrame()
        try: 
            for cfg in self.__config:
                if(cfg['sourceType'] == 'dataframe'):
                    dfConfig = cfg['values']
                    dataframeObj = DataframeProcessor(self.__n,dfConfig)
                    df_data = dataframeObj.getDataFromDF()
                elif(cfg['sourceType'] == 'RegularExpression'):
                    reConfig = cfg['values']
                    reObj = RegExProcessor(self.__n,reConfig)
                    re_data = reObj.getDataFromRE()
                elif(cfg['sourceType'] == 'Metrics'):
                    metricsConfig = cfg['values']
                    metricsObj = MetricsProcessor(self.__n,metricsConfig)
                    metrics_data = metricsObj.processMetrics()
                else:
                    raise Exception("Invalid sourceType value in cinfiguration: " + cfg['sourceType'])

            df_data = df_data.reset_index(drop=True)
            re_data = re_data.reset_index(drop=True)
            metrics_data = metrics_data.reset_index(drop=True)

            final_data = pd.concat([df_data, re_data, metrics_data], axis=1)
            return final_data

            raise Exception("Error in generating data")

        except Exception as e:
            print("Error: " + repr(e)) 
