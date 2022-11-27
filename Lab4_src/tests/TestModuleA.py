import unittest
from modules.ModuleA import ModuleA
from unittest.mock import Mock
from unittest.mock import patch
from data.Entry import Entry


class TestA(unittest.TestCase):

    def setUp(self):
        # create instance of Module A w/ mock obj's for parameters
        self.mock_ModuleB = Mock()
        self.mock_ModuleC = Mock()
        self.mock_ModuleD = Mock()
        self.mock_ModuleE = Mock()
        self.test_ModuleA = ModuleA(self.mock_ModuleB, self.mock_ModuleC, self.mock_ModuleD, self.mock_ModuleE)
        self.test_filename = "test_file_ModuleA.txt"
        self.test_data = []

    def test_parseDelete_method(self):
        self.test_data = []
        self.test_ModuleA._filename = self.test_filename
        self.test_ModuleA._data = self.test_data
        index_to_del = 2
        
        # mock return value of deleteData method to return empty list
        self.mock_ModuleD.deleteData.return_value = []
        self.assertTrue(self.test_ModuleA.parseDelete(index_to_del))
        self.mock_ModuleD.deleteData.assert_called_with(self.test_data, index_to_del, self.test_filename)
        
        # mock return value of deleteData method to return None
        self.mock_ModuleD.deleteData.return_value = None
        self.assertFalse(self.test_ModuleA.parseDelete(index_to_del))
        self.mock_ModuleD.deleteData.assert_called_with(self.test_data, index_to_del, self.test_filename)
        
        
    @patch.object(ModuleA, "displayHelp")
    def test_displayHelp_method(self, mock_displayHelp):
        # call to mock method
        mock_displayHelp()
        
        # assertion statements
        mock_displayHelp.assert_called()
        self.assertTrue(self.test_ModuleA.displayHelp())
        
        
    def test_parseLoad_method(self):
        self.test_data = []
        self.test_ModuleA.data = self.test_data
        
        # mock return value of loadFile method to return empty list
        self.mock_ModuleB.loadFile.return_value = []
        self.assertTrue(self.test_ModuleA.parseLoad(self.test_filename))
        
        # mock return value of loadFile method to return None
        self.mock_ModuleB.loadFile.return_value = None
        self.assertFalse(self.test_ModuleA.parseLoad(self.test_filename))
        
        
    def test_parseAdd_method(self):
        self.test_data = []
        self.test_ModuleA.filename = self.test_filename
        self.test_ModuleA.data = self.test_data
        
        test_name = "Bobby"
        test_number = "42349"
        
        # mock return value of insertData method to return empty list
        self.mock_ModuleD.insertData.return_value = []
        self.assertTrue(self.test_ModuleA.parseAdd(test_name, test_number))
        
        # mock return value of insertData method to return None
        self.mock_ModuleD.insertData.return_value = None
        self.assertFalse(self.test_ModuleA.parseAdd(test_name, test_number))
        
        
    def test_runSort_method(self):
        # mock return value of sortData method to return empty list
        self.mock_ModuleC.sortData.return_value = []
        self.assertTrue(self.test_ModuleA.runSort())
        
        # mock return value of sortData method to return None
        self.mock_ModuleC.sortData.return_value = None
        self.assertFalse(self.test_ModuleA.runSort())
        
        
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
        
        # mock return value of updateData method to return updated list with new person/ num at index 1
        self.mock_ModuleD.updateData.return_value = [Entry(test_name,test_num), Entry(test_new_name,test_new_number)]
        self.assertTrue(self.test_ModuleA.parseUpdate(index_to_update, test_new_name, test_new_number))
        self.mock_ModuleD.updateData.assert_called_with(self.test_data, index_to_update, test_new_name, test_new_number, self.test_filename)
        
        # mock return value of updateData method to return None
        self.mock_ModuleD.updateData.return_value = None
        self.assertFalse(self.test_ModuleA.parseUpdate(index_to_update, test_new_name, test_new_number))
        self.mock_ModuleD.updateData.assert_called_with(self.test_data, index_to_update, test_new_name, test_new_number, self.test_filename)
      
      
    def test_runExit_method(self):
        try:
            self.test_ModuleA.runExit()
        except:
            self.mock_ModuleE.exitProgram.assert_called_once()
    
    
    @patch.object(ModuleA, "run")
    def test_run_NO_and_help_command_method(self, mock_run):
        # call to mock method w/ no command
        mock_run()
        
        # assertion statements
        mock_run.assert_called_with()
        mock_run.assert_called_once()
        
        # call to mock method w/ help command
        mock_run("help")
        mock_run.assert_called_with("help")      
                
                
    def test_run_add_command_method(self):
        self.test_ModuleA._data = [Entry("hello","54")]
        self.test_ModuleA.run("add")
        self.mock_ModuleD.insertData.assert_not_called() # IndexError so no method call
        
        self.test_ModuleA._data = None
        self.test_ModuleA.run("add")
        self.mock_ModuleD.insertData.assert_not_called() # self.data == None so no method call
        
        self.test_ModuleA._data = []
        self.test_ModuleA._filename = self.test_filename
        self.test_ModuleA.run("add", "test_name_to_add", "76585")
        self.mock_ModuleD.insertData.assert_called_with([], "test_name_to_add", "76585", self.test_filename)          
   

    def test_run_load_command_method(self):
        # test load command
        self.test_ModuleA.run("load")
        self.mock_ModuleB.loadFile.assert_not_called()
        self.test_ModuleA.run("load", self.test_filename)
        self.mock_ModuleB.loadFile.assert_called_once_with(self.test_filename)
        
        
    def test_run_sort_command_method(self):
        self.test_ModuleA._data = None
        self.test_ModuleA.run("sort")
        self.mock_ModuleC.sortData.assert_not_called() # self.data == None so no method call
        
        self.test_ModuleA._data = [Entry("hello","54")]
        self.test_ModuleA.run("sort")
        self.mock_ModuleC.sortData.assert_called_once() # runSort() is called when data!=None
        

    def test_run_update_command_method(self):
        self.test_ModuleA._data = [Entry("hello","58945")]
        self.test_ModuleA.run("update")
        self.mock_ModuleD.updateData.assert_not_called() # IndexError so no method call
        
        self.test_ModuleA._data = None
        self.test_ModuleA.run("update")
        self.mock_ModuleD.updateData.assert_not_called() # self.data == None so no method call
        
        self.test_ModuleA._data = []
        self.test_ModuleA._filename = self.test_filename
        index_to_update = 0
        self.test_ModuleA.run("update",index_to_update ,"test_name_to_update", "76585")
        self.mock_ModuleD.updateData.assert_called_with([], index_to_update, "test_name_to_update", "76585", self.test_filename)  

        
    def test_run_delete_command_method(self):
        self.test_ModuleA._data = [Entry("hello","58945")]
        self.test_ModuleA.run("delete")
        self.mock_ModuleD.deleteData.assert_not_called() # IndexError so no method call
        
        self.test_ModuleA._data = None
        self.test_ModuleA.run("delete")
        self.mock_ModuleD.deleteData.assert_not_called() # self.data == None so no method call
        
        self.test_ModuleA._data = []
        self.test_ModuleA._filename = self.test_filename
        index_to_delete = 0
        self.test_ModuleA.run("delete", index_to_delete)
        self.mock_ModuleD.deleteData.assert_called_with([], index_to_delete, self.test_filename)  
        
        
    def test_run_exit_command_method(self):
        try:
            self.test_ModuleA.run("exit")
        except:
            self.mock_ModuleE.exitProgram.assert_called_once()
        
    
    
if __name__ == '__main__':
    unittest.main()
    
