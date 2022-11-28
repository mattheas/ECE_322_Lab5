import unittest
from modules.ModuleA import ModuleA
from modules.ModuleD import ModuleD
from unittest.mock import Mock
from data.Entry import Entry
from contextlib import redirect_stdout


class TestA(unittest.TestCase):

    def setUp(self):
        # create instance of Module A w/ mock obj's for parameters
        self.mock_ModuleB = Mock()
        self.mock_ModuleC = Mock()
        self.test_ModuleD = ModuleD(Mock(), Mock())
        self.mock_ModuleE = Mock()
        self.test_ModuleA = ModuleA(self.mock_ModuleB, self.mock_ModuleC, self.test_ModuleD, self.mock_ModuleE)
        self.test_filename = "test_file_ModuleAD.txt"
        self.test_data = []

    def test_parseDelete_method(self):
        self.test_ModuleA._filename = self.test_filename
        self.test_ModuleA._data = [Entry("hello","54")]
        index_to_del = 0
        self.assertTrue(self.test_ModuleA.parseDelete(index_to_del))
  
        
    def test_parseAdd_method(self):
        self.test_ModuleA._filename = self.test_filename
        self.test_ModuleA._data = self.test_data
        test_name = "Bobby"
        test_number = "42349"
        self.assertTrue(self.test_ModuleA.parseAdd(test_name, test_number))
       
        
    def test_parseUpdate_method(self):
        # populate test data array
        test_name = "Manny"
        test_name1 = "Hanny"
        test_num = "87635"
        test_num1 = "96453"
        self.test_data = [Entry(test_name,test_num), Entry(test_name1,test_num1)]
        self.test_ModuleA._filename = self.test_filename
        self.test_ModuleA._data = self.test_data
        
        test_new_name = "Not Hanny"
        test_new_number = "123693"
        index_to_update = 1
        self.assertTrue(self.test_ModuleA.parseUpdate(index_to_update, test_new_name, test_new_number))
        
                
    def test_run_add_command_method(self):
        with open('./tests/TestAD_redirect_output_add_command_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                self.test_ModuleA._data = [Entry("hello","54")]
                self.test_ModuleA.run("add")
                
                self.test_ModuleA._data = None
                self.test_ModuleA.run("add")
                
                self.test_ModuleA._data = []
                self.test_ModuleA._filename = self.test_filename
                self.test_ModuleA.run("add", "test_name_to_add", "76585")
        f1.close()
        
        # assert contents of expected file is the same as actual
        f1 = open("./tests/TestAD_redirect_output_add_command_actual.txt", "r")
        f2 = open("./tests/TestAD_redirect_output_add_command_expected.txt", "r")
        i = 0
        for line1 in f1:
            i+=1
            for line2 in f2:
                self.assertEqual(line1, line2)
                break
        f1.close()
        f2.close()

        
    def test_run_update_command_method(self):
        with open('./tests/TestAD_redirect_output_update_command_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                self.test_ModuleA._data = [Entry("hello","58945")]
                self.test_ModuleA.run("update")
                
                self.test_ModuleA._data = None
                self.test_ModuleA.run("update")
                
                self.test_ModuleA._data = []
                self.test_ModuleA._filename = self.test_filename
                index_to_update = 0
                self.test_ModuleA.run("update",index_to_update ,"test_name_to_update", "76585")
        f1.close()
    
        # assert contents of expected file is the same as actual
        f1 = open("./tests/TestAD_redirect_output_update_command_actual.txt", "r")
        f2 = open("./tests/TestAD_redirect_output_update_command_expected.txt", "r")
        i = 0
        for line1 in f1:
            i+=1
            for line2 in f2:
                self.assertEqual(line1, line2)
                break
        f1.close()
        f2.close()
    
    
    def test_run_delete_command_method(self):
        with open('./tests/TestAD_redirect_output_delete_command_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                self.test_ModuleA._data = [Entry("hello","58945")]
                self.test_ModuleA.run("delete")
                
                self.test_ModuleA._data = None
                self.test_ModuleA.run("delete")
                
                self.test_ModuleA._data = [Entry("hello","58945")]
                self.test_ModuleA._filename = self.test_filename
                index_to_delete = 0
                self.test_ModuleA.run("delete", index_to_delete)
        f1.close()
        
        # assert contents of expected file is the same as actual
        f1 = open("./tests/TestAD_redirect_output_delete_command_actual.txt", "r")
        f2 = open("./tests/TestAD_redirect_output_delete_command_expected.txt", "r")
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
    
