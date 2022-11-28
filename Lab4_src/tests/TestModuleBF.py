import unittest
from modules.ModuleB import ModuleB
from modules.ModuleF import ModuleF
from unittest.mock import Mock
from contextlib import redirect_stdout

# no need to test FileNotFOundError in Module B as this would require student to intentionally change
# a files permission to be not readable by current user

# setter method not tested as it is not required, Use "Whats the pythonic way to use getters and setters" stack overflow guide
# to assist in calling setter method w/ mocks IF you want to test


class TestB(unittest.TestCase):

    def test_loadFile_read_data(self):
        # create instance of Module B w/ mock Mod. F obj
        test_ModuleB = ModuleB(ModuleF())
        
        # create test .txt file with data
        test_file = "test_data.txt"
        
        test_name1 = "test_name"
        test_name2 = "another_test_name"
        test_number1 = "1234"
        test_number2 = "54321"
        
        test_data1 = "test_name,1234\n"
        test_data2 = "another_test_name,54321"
        
        with open(test_file, 'w') as f:
            f.write(test_data1)
            f.write(test_data2)  
        f.close()
        
        with open('./tests/TestBF_redirect_output_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                self.assertEqual(test_ModuleB.loadFile(test_file)[0].name, test_name1)
                self.assertEqual(test_ModuleB.loadFile(test_file)[0].number, test_number1)
                self.assertEqual(test_ModuleB.loadFile(test_file)[1].name, test_name2)
                self.assertEqual(test_ModuleB.loadFile(test_file)[1].number, test_number2)    
                test_ModuleB.loadFile("non_existent_file.txt")                           
        f1.close()	
    
        
        # assert ModuleF works as expected printing to terminal
        f1 = open("./tests/TestBF_redirect_output_actual.txt", "r")
        f2 = open("./tests/TestBF_redirect_output_expected.txt", "r")
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
    
