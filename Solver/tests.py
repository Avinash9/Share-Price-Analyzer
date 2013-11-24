import unittest
from Solver import *


class TestSolver(unittest.TestCase):
       def test_proper_data(self):
              data=get_result("Data/data.csv")
              '''   Company 1 max price month december  '''
              self.assertEquals('dec', data['Comp 1'].month)
              '''   Company 7 max price year is 1990  '''
              self.assertEquals('1990', data[' Comp 7'].year)
        
       def test_improper_data(self):
              data=get_result("Data/data.csv")
              '''   Company 2 do not have max price month december  '''
              self.assertNotEquals('dec', data[' Comp 2'].month)
              '''   Company 9 do not have max price in year 1991  '''
              self.assertNotEquals('1991', data[' Comp 9'].year)         
       
       
if __name__ == '__main__':
    unittest.main()
