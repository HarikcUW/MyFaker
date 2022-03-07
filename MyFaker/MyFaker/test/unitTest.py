import unittest
from MyFaker.code.helper import DataGenerator
import pandas as pd

class TestHelperMethods(unittest.TestCase):

    def test_upper(self):
        dg = DataGenerator(10,[])
        self.assertEqual(dg.toUpper("hari"), 'HARI')

    def test_isupper(self):
        dg = DataGenerator(10,[])
        self.assertTrue(dg.isUpper("HARI"))
        self.assertTrue(dg.isUpper("HAI"))

    def test_renameDfColumn(self):

        df_Color = pd.DataFrame(['Green','Red','Yellow','Blue'], columns = ['Color'])
        columnRenameDict = {'Color': 'NewColor'}
        dg = DataGenerator(10,[])
        self.assertTrue('NewColor' in dg.renameDfColumn(df_Color,columnRenameDict).columns)

if __name__ == '__main__':
    unittest.main()