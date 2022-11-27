import unittest
from modules.ModuleA import ModuleA
from modules.ModuleC import ModuleC
from contextlib import redirect_stdout
from unittest.mock import Mock
from data.Entry import Entry


class TestA(unittest.TestCase):

    def setUp(self):
        # create instance of Module A w/ mock obj's for parameters
        self.mock_ModuleB = Mock()
        self.test_ModuleC = ModuleC(Mock())
        self.mock_ModuleD = Mock()
        self.mock_ModuleE = Mock()
        self.test_ModuleA = ModuleA(self.mock_ModuleB, self.test_ModuleC, self.mock_ModuleD, self.mock_ModuleE)
        self.test_filename = "test_file_ModuleA.txt"
        self.test_data = []
        
        
    def test_runSort_method(self):
        # assert that runSort does not return None 
        self.test_ModuleA._data = self.test_data
        self.assertTrue(self.test_ModuleA.runSort())

        
    def test_run_sort_command_method(self):
        with open('./tests/TestAC_redirect_output_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                self.test_ModuleA._data = None
                self.test_ModuleA.run("sort")
                self.test_ModuleA._data = [Entry("hello","54")]
                self.test_ModuleA.run("sort")                           
        f1.close()
    
        # assert contents of expected file is the same as actual
        f1 = open("./tests/TestAC_redirect_output_actual.txt", "r")
        f2 = open("./tests/TestAC_redirect_output_expected.txt", "r")
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
    
