import unittest
from modules.ModuleA import ModuleA
from modules.ModuleB import ModuleB
from modules.ModuleC import ModuleC
from modules.ModuleD import ModuleD
from modules.ModuleE import ModuleE
from modules.ModuleF import ModuleF
from modules.ModuleG import ModuleG
from contextlib import redirect_stdout
from unittest.mock import Mock
from data.Entry import Entry


class TestA(unittest.TestCase):

    def setUp(self):
        # create instance of Module A w/ mock obj's for parameters
        self.test_ModuleF = ModuleF()
        self.test_ModuleG = ModuleG()
        self.test_ModuleB = ModuleB(self.test_ModuleF)
        self.test_ModuleC = ModuleC(self.test_ModuleF)
        self.test_ModuleD = ModuleD(self.test_ModuleF, self.test_ModuleG)
        self.test_ModuleE = ModuleE()
        self.test_ModuleA = ModuleA(self.test_ModuleB, self.test_ModuleC, self.test_ModuleD, self.test_ModuleE)
        self.test_filename = "test_file_ModuleABCDEFG.txt"
        self.test_data = []


# create system
        self.F = ModuleF()
        self.G = ModuleG()
        self.A = ModuleA(ModuleB(self.F), ModuleC(self.F), ModuleD(self.F, self.G), ModuleE())
        self.filename = "data.txt"

    def test_parseLoad_method(self):
        self.test_data = []
        self.test_ModuleA.data = self.test_data
        
        # when B.parseLoad called with empty/ nonexistent file it returns empty list
        self.assertTrue(self.test_ModuleA.parseLoad(self.test_filename))        
        
    
    def test_runSort_method(self):
        # assert that runSort does not return None 
        self.test_ModuleA._data = self.test_data
        self.assertTrue(self.test_ModuleA.runSort()) 
   
   
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
        
        
    def test_runExit_method(self):
        with open('./bottomuptests/TestAE_redirect_output_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                try:
                    self.test_ModuleA.runExit()
                except SystemExit:
                    pass   
        f1.close()
        
        # assert contents of expected file is the same as actual
        f1 = open("./bottomuptests/TestAE_redirect_output_actual.txt", "r")
        f2 = open("./bottomuptests/TestAE_redirect_output_expected.txt", "r")
        i = 0
        for line1 in f1:
            i+=1
            for line2 in f2:
                self.assertEqual(line1, line2)
                break
        f1.close()
        f2.close()
   

    def test_run_exit_command_method(self):
        with open('./bottomuptests/TestAE_redirect_output_exit_command_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                try:
                    self.test_ModuleA.run("exit")
                except SystemExit:
                    pass   
        f1.close()
        
        # assert contents of expected file is the same as actual
        f1 = open("./bottomuptests/TestAE_redirect_output_exit_command_actual.txt", "r")
        f2 = open("./bottomuptests/TestAE_redirect_output_exit_command_expected.txt", "r")
        i = 0
        for line1 in f1:
            i+=1
            for line2 in f2:
                self.assertEqual(line1, line2)
                break
        f1.close()
        f2.close()    
   

    def test_run_load_command_method(self):
        # test load command
        with open('./bottomuptests/TestABCDEFG_redirect_output_load_command_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                self.test_ModuleA.run("load")
                self.test_ModuleA.run("load", self.test_filename)
        f1.close()

        # assert contents of expected file is the same as actual
        f1 = open("./bottomuptests/TestABCDEFG_redirect_output_load_command_actual.txt", "r")
        f2 = open("./bottomuptests/TestABCDEFG_redirect_output_load_command_expected.txt", "r")
        i = 0
        for line1 in f1:
            i+=1
            for line2 in f2:
                self.assertEqual(line1, line2)
                break
        f1.close()
        f2.close()

        
    def test_run_sort_command_method(self):
        with open('./bottomuptests/TestAC_redirect_output_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                self.test_ModuleA._data = None
                self.test_ModuleA.run("sort")
                self.test_ModuleA._data = [Entry("hello","54")]
                self.test_ModuleA.run("sort")                           
        f1.close()
    
        # assert contents of expected file is the same as actual
        f1 = open("./bottomuptests/TestAC_redirect_output_actual.txt", "r")
        f2 = open("./bottomuptests/TestAC_redirect_output_expected.txt", "r")
        i = 0
        for line1 in f1:
            i+=1
            for line2 in f2:
                self.assertEqual(line1, line2)
                break
        f1.close()
        f2.close()
        
                
    def test_run_add_command_method(self):
        with open('./bottomuptests/TestAD_redirect_output_add_command_actual.txt', 'w') as f1:
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
        f1 = open("./bottomuptests/TestAD_redirect_output_add_command_actual.txt", "r")
        f2 = open("./bottomuptests/TestAD_redirect_output_add_command_expected.txt", "r")
        i = 0
        for line1 in f1:
            i+=1
            for line2 in f2:
                self.assertEqual(line1, line2)
                break
        f1.close()
        f2.close()

        
    def test_run_update_command_method(self):
        with open('./bottomuptests/TestAD_redirect_output_update_command_actual.txt', 'w') as f1:
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
        f1 = open("./bottomuptests/TestAD_redirect_output_update_command_actual.txt", "r")
        f2 = open("./bottomuptests/TestAD_redirect_output_update_command_expected.txt", "r")
        i = 0
        for line1 in f1:
            i+=1
            for line2 in f2:
                self.assertEqual(line1, line2)
                break
        f1.close()
        f2.close()
    
    
    def test_run_delete_command_method(self):
        with open('./bottomuptests/TestAD_redirect_output_delete_command_actual.txt', 'w') as f1:
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
        f1 = open("./bottomuptests/TestAD_redirect_output_delete_command_actual.txt", "r")
        f2 = open("./bottomuptests/TestAD_redirect_output_delete_command_expected.txt", "r")
        i = 0
        for line1 in f1:
            i+=1
            for line2 in f2:
                self.assertEqual(line1, line2)
                break
        f1.close()
        f2.close()
        
        
    def test_entire_system(self):
        # no command given, assert it prints expected val to terminal
        with open('./bottomuptests/TestABCDEFG_entire_system_no_command_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                self.test_ModuleA.run()
        f1.close()
        f1 = open("./bottomuptests/TestABCDEFG_entire_system_no_command_actual.txt", "r")
        f2 = open("./bottomuptests/TestABCDEFG_entire_system_no_command_expected.txt", "r")
        i = 0
        for line1 in f1:
            i+=1
            for line2 in f2:
                self.assertEqual(line1, line2)
                break
        f1.close()
        f2.close()
        
        # help command, assert it prints expected val to terminal
        with open('./bottomuptests/TestABCDEFG_entire_system_help_command_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                self.test_ModuleA.run("help")
        f1.close()
        f1 = open("./bottomuptests/TestABCDEFG_entire_system_help_command_actual.txt", "r")
        f2 = open("./bottomuptests/TestABCDEFG_entire_system_help_command_expected.txt", "r")
        i = 0
        for line1 in f1:
            i+=1
            for line2 in f2:
                self.assertEqual(line1, line2)
                break
        f1.close()
        f2.close()
        
        # load data command, assert data is loaded into local data list
        self.test_ModuleA.run("load","data.txt")
        self.assertTrue(len(self.test_ModuleA._data) == 6)
        self.assertEqual(self.test_ModuleA._data[0].name, "Jeremy")
        self.assertEqual(self.test_ModuleA._data[0].number, "1234")
        self.assertEqual(self.test_ModuleA._data[5].name, "Frank")
        self.assertEqual(self.test_ModuleA._data[5].number, "123456789789")
        
        # update command is given, assert data is updated
        self.test_ModuleA.run("update",3,"James","56789")
        self.assertEqual(self.test_ModuleA._data[2].name, "James")
        self.assertEqual(self.test_ModuleA._data[2].number, "56789")
        
        # add command is given, assert data list is updated with entry added to end of list
        self.test_ModuleA.run( "add","Ahmed","477848")
        self.assertEqual(self.test_ModuleA._data[6].name, "Ahmed")
        self.assertEqual(self.test_ModuleA._data[6].number, "477848")
        
        # delete command is given, assert data list is updated at & +/- 1 index around the deleted entry
        self.test_ModuleA.run( "delete",2)
        self.assertTrue(len(self.test_ModuleA._data) == 6)
        self.assertEqual(self.test_ModuleA._data[0].name, "Jeremy")
        self.assertEqual(self.test_ModuleA._data[0].number, "1234")
        self.assertEqual(self.test_ModuleA._data[1].name, "James")
        self.assertEqual(self.test_ModuleA._data[1].number, "56789")
        self.assertEqual(self.test_ModuleA._data[2].name, "JJJ")
        self.assertEqual(self.test_ModuleA._data[2].number, "1234")
        
        # sort command is given, assert list is in correct order
        self.test_ModuleA.run("sort")
        self.assertEqual(self.test_ModuleA._data[0].name, "Ahmed")
        self.assertEqual(self.test_ModuleA._data[1].name, "Frank")
        self.assertEqual(self.test_ModuleA._data[2].name, "JJJ")
        self.assertEqual(self.test_ModuleA._data[3].name, "James")
        self.assertEqual(self.test_ModuleA._data[4].name, "Jeremy")
        self.assertEqual(self.test_ModuleA._data[5].name, "Thomas")
        
        # exit command is given
        self.test_ModuleA.run(" exit")

    
    
if __name__ == '__main__':
    unittest.main()
    
