import unittest
import pandas as pd
from sales_etl_project.etl_sales import transform_data

class TestETL(unittest.TestCase):
    def setUp(self):
        #sample data for testing
        self.df = pd.DataFrame({
            "Region": ["East", "West", "East", None],
            "Date": ["2023-01-01", "2023-01-10", "2023-01-20", "2023-01-25"],
            "Sales": [1000, 2000, None, 1300]
        })
    
    def test_shape_after_transformation(self):
        #should remove nulls -> keep 2 rows, east, west
        result = transform_data(self.df)
        self.assertEqual(len(result),2)
    
    def test_required_colmns_present(self):
        #should have colummns region, month, sales
        result = transform_data(self.df)
        self.assertListEqual(sorted(result.columns.tolist()), sorted(["Region", "Month", "Sales"]))
    
    def test_month_column_format(self):
        result= transform_data(self.df)
        self.assertTrue(all(result['Month'].str.match(r'^\d{4}-\d{2}$')))
    
    def test_no_nulls_in_critical_columns(self):
        result = transform_data(self.df)
        self.assertFalse(result['Region'].isnull().any())
        self.assertFalse(result['Month'].isnull().any())
        self.assertFalse(result['Sales'].isnull().any())
    
    def test_sum_grouped(self):
        result = transform_data(self.df)
        east_row = result[result['Region'] == 'East']
        west_row = result[result['Region'] == 'West']
        #east , only first row(1000) and seconde should be null 
        self.assertEqual(east_row['Sales'].values[0], 1000)
        #west, only second row(2000)
        self.assertEqual(west_row['Sales'].values[0], 2000)

if __name__ == '__main__':
    unittest.main()