import unittest
from modules.ModuleA import ModuleA
from modules.ModuleE import ModuleE
from unittest.mock import Mock
from contextlib import redirect_stdout
from data.Entry import Entry


class TestA(unittest.TestCase):

    def setUp(self):
        # create instance of Module A w/ mock obj's for parameters
        self.mock_ModuleB = Mock()
        self.mock_ModuleC = Mock()
        self.mock_ModuleD = Mock()
        self.test_ModuleE = ModuleE()
        self.test_ModuleA = ModuleA(self.mock_ModuleB, self.mock_ModuleC, self.mock_ModuleD, self.test_ModuleE)
        self.test_filename = "test_file_ModuleA.txt"
        self.test_data = []


    def test_runExit_method(self):
        with open('./tests/TestAE_redirect_output_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                try:
                    self.test_ModuleA.runExit()
                except SystemExit:
                    pass   
        f1.close()
        
        # assert contents of expected file is the same as actual
        f1 = open("./tests/TestAE_redirect_output_actual.txt", "r")
        f2 = open("./tests/TestAE_redirect_output_expected.txt", "r")
        i = 0
        for line1 in f1:
            i+=1
            for line2 in f2:
                self.assertEqual(line1, line2)
                break
        f1.close()
        f2.close()
   

    def test_run_exit_command_method(self):
        with open('./tests/TestAE_redirect_output_exit_command_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                try:
                    self.test_ModuleA.run("exit")
                except SystemExit:
                    pass   
        f1.close()
        
        # assert contents of expected file is the same as actual
        f1 = open("./tests/TestAE_redirect_output_exit_command_actual.txt", "r")
        f2 = open("./tests/TestAE_redirect_output_exit_command_expected.txt", "r")
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
    
