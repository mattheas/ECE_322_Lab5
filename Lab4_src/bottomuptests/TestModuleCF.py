import unittest
from modules.ModuleC import ModuleC
from modules.ModuleF import ModuleF
from data.Entry import Entry
from unittest.mock import Mock
from contextlib import redirect_stdout

# As told in the lab manual no need to test getters/ setters, focus on the main methods, although these would normally be tested


class TestC(unittest.TestCase):

    def test_sortData_method(self):
        # create lists of unsorted and sorted Entry obj's
        test_name = "zan"
        test_name1 = "abc"
        test_name2 = "bgf"
        test_num = "123456"
        test_num1 = "234098"
        test_num2 = "42439"
        unsorted_data_list = [Entry(test_name,test_num), Entry(test_name1,test_num1), Entry(test_name2,test_num2)]
        sorted_data_list = [Entry(test_name1,test_num1), Entry(test_name2,test_num2), Entry(test_name,test_num)]
    	
        test_ModuleC = ModuleC(ModuleF())
        
        with open('./bottomuptests/TestCF_redirect_output_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                self.assertEqual(test_ModuleC.sortData(unsorted_data_list)[0].name, sorted_data_list[0].name)
                self.assertEqual(test_ModuleC.sortData(unsorted_data_list)[1].name, sorted_data_list[1].name)
                self.assertEqual(test_ModuleC.sortData(unsorted_data_list)[2].name, sorted_data_list[2].name)                      
        f1.close()	
    
        
        # assert ModuleF works as expected printing to terminal
        f1 = open("./bottomuptests/TestCF_redirect_output_actual.txt", "r")
        f2 = open("./bottomuptests/TestCF_redirect_output_expected.txt", "r")
        i = 0
        for line1 in f1:
            i+=1
            for line2 in f2:
                self.assertEqual(line1, line2)
                break
        f1.close()
        f2.close()

        
        
        
if __name__ == '__main__':
    unittest.main()
    
