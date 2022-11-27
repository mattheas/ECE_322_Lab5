import unittest
from contextlib import redirect_stdout
from modules.ModuleA import ModuleA
from modules.ModuleB import ModuleB
from unittest.mock import Mock


class TestA(unittest.TestCase):

    def setUp(self):
        # create instance of Module A w/ mock obj's for parameters
        self.test_ModuleB = ModuleB(Mock())
        self.mock_ModuleC = Mock()
        self.mock_ModuleD = Mock()
        self.mock_ModuleE = Mock()
        self.test_ModuleA = ModuleA(self.test_ModuleB, self.mock_ModuleC, self.mock_ModuleD, self.mock_ModuleE)
        self.test_filename = "test_file_ModuleA.txt"
        self.test_data = []
        
        
    def test_parseLoad_method(self):
        self.test_data = []
        self.test_ModuleA.data = self.test_data
        
        # when B.parseLoad called with empty/ nonexistent file it returns empty list
        self.assertTrue(self.test_ModuleA.parseLoad(self.test_filename))         
   

    def test_run_load_command_method(self):
        # test load command
        with open('./tests/TestAB_redirect_output_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                self.test_ModuleA.run("load")
                self.test_ModuleA.run("load", self.test_filename)
        f1.close()

        # assert contents of expected file is the same as actual
        f1 = open("./tests/TestAB_redirect_output_actual.txt", "r")
        f2 = open("./tests/TestAB_redirect_output_expected.txt", "r")
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
    
