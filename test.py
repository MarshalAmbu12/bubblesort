#!/usr/bin/python3

"""
***********************************************




Do not edit this file





***********************************************
"""
import unittest
from bubble_sort import *

class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(bubble_sort([0.2,1,22,100,3]),[0.2, 1, 3, 22, 100])
        

if __name__=='__main__':
    unittest.main()
