import unittest
import pandas as pd
from Project import load_data  

class TestDataLoading(unittest.TestCase):
    def test_load_data_success(self):
        df = load_data('students.csv')  
        self.assertIsInstance(df, pd.DataFrame)
    


if __name__ == '__main__':
    unittest.main()
