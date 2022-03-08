import unittest
from myfaker.code.helper import DataGenerator
import pandas as pd

class TestHelperMethods(unittest.TestCase):

    def test_getDfElements(self):
        df_Product = pd.DataFrame([['Laptop', 'Physical', 798.0], ['Keyboard', 'Physical', 56.50], ['Subscription', 'Digital', 15.0]]
            , columns=['Product','Type','Cost'])
        columnList = ['Product', 'Cost']
        dg = DataGenerator(5,[])
        df_selectColumns = dg.getDfElements(df_Product,columnList)
        # Check if correct number of rows returned
        self.assertTrue(df_selectColumns.shape[0] == 5)

        # Check if only selected columns returned
        self.assertTrue(df_selectColumns.columns.values.tolist() == columnList)
    
    def test_getRegExDataFixedSize(self):
        dg = DataGenerator(5,[])
        columnInfo = {'colName':'PhoneNumber','regExpression':'425[0-9]{7}'}
        df_regEx = dg.getRegExData(columnInfo)

        # Check if all rows has 10 digits
        self.assertTrue(len(min(df_regEx['PhoneNumber'])) == 10)
        self.assertTrue(len(max(df_regEx['PhoneNumber'])) == 10)

    def test_getRegExDataRangeSize(self):
        dg = DataGenerator(5,[])
        columnInfo = {'colName':'PhoneNumber','regExpression':'425[0-9]{4:7}'}
        df_regEx = dg.getRegExData(columnInfo)

        # Check if all rows has 10 digits
        self.assertTrue(len(min(df_regEx['PhoneNumber'])) >= 7)
        self.assertTrue(len(max(df_regEx['PhoneNumber'])) <= 10)        

    def test_getMetricDataInt(self):
        dg = DataGenerator(5,[])
        columnInfo = {'colName':'SalesQuantity','dataType':'int', 'startValue':'10', 'endValue':'40'}
        df_Metric = dg.getMetricData(columnInfo)

        # Check if all rows has 10 digits
        self.assertTrue(min(df_Metric['SalesQuantity']) >= 10)
        self.assertTrue(max(df_Metric['SalesQuantity']) <= 40)  

        # Check if all values are integers
        self.assertTrue((df_Metric['SalesQuantity'] == df_Metric['SalesQuantity'].astype(int)).all())  

    def test_getMetricDataFloat(self):
        dg = DataGenerator(5,[])
        columnInfo = {'colName':'SalesQuantity','dataType':'float', 'startValue':'10', 'endValue':'40'}
        df_Metric = dg.getMetricData(columnInfo)

        # Check if all rows has 10 digits
        self.assertTrue(min(df_Metric['SalesQuantity']) >= 10)
        self.assertTrue(max(df_Metric['SalesQuantity']) <= 40)  

        # Check if all values are integers
        self.assertTrue((df_Metric['SalesQuantity'] != df_Metric['SalesQuantity'].astype(int)).all())  

    def test_renameDfColumn(self):
        df_Color = pd.DataFrame(['Green','Red','Yellow','Blue'], columns = ['Color'])
        columnRenameDict = {'Color': 'NewColor'}
        dg = DataGenerator(10,[])
        self.assertTrue('NewColor' in dg.renameDfColumn(df_Color,columnRenameDict).columns)

if __name__ == '__main__':
    unittest.main()
    
