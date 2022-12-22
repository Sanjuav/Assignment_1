import unittest
import os
from csv_file import csv_file  

class TestFile(unittest.TestCase):
    
    def test_csv_file(self):
        """Test method that checks whether a csv file is created as expected"""
        MAC_VALUES = "assignment_network.csv"
        row_header =[('Country', 'State', 'City', 'Town')]
        csv_file(MAC_VALUES, row_header)
        assert os.path.exists(MAC_VALUES) == True
        
if __name__ == '__main__':
    unittest.main()