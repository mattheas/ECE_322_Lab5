import unittest
from modules.ModuleD import ModuleD
from modules.ModuleG import ModuleG
from unittest.mock import Mock
from data.Entry import Entry
from contextlib import redirect_stdout


# As told in the lab manual no need to test getters/ setters, focus on the main methods, although these would normally be tested. Also
# as a note the the deleteData method in ModuleD permanently deletes the element in memory, so re-initialization of data list must be 
# performed between assert() calls


class TestD(unittest.TestCase):

    def test_insertData_method(self):
        test_ModuleD = ModuleD(Mock(), ModuleG())
        
        # test data
        test_name = "Bob"
        test_number = "135849"
        test_entry = test_name + "," + test_number + "\n"
        test_filename = "TestDG_insertData.txt"
        test_data = []
        
        # assert .txt file is empty
        f1 = open("./tests/TestDG_insertData.txt", "r")
        for line in f1:
            self.assertEqual(line, "")
        f1.close()
        
        # assert data is inserted into data list
        self.assertEqual(test_ModuleD.insertData(test_data, test_name, test_number, test_filename)[0].name, test_name)
        self.assertEqual(test_ModuleD.insertData(test_data, test_name, test_number, test_filename)[0].number, test_number)                     
        	
    
        # assert .txt file is updated with one entry 
        f2 = open("./tests/TestDG_insertData.txt", "r")
        
        i = 0;
        for line in f2:
            i+=1
            if (i==1):
                self.assertEqual(line, test_entry)
        f2.close()
    

    def test_updateData_method(self):
        test_ModuleD = ModuleD(Mock(), ModuleG())
        
        # populate test data array
        test_name = "danny"
        test_name1 = "sammy"
        test_name2 = "flammy"
        test_num = "437892"
        test_num1 = "789234"
        test_num2 = "761237"
        test_data = [Entry(test_name,test_num), Entry(test_name1,test_num1), Entry(test_name2,test_num2)]
        
        test_filename = "TestDG_updateData.txt"
        update_index = 0
        test_update_name = "notDanny"
        test_update_number = "84921"
        
        # assert .txt file is empty
        f1 = open("./tests/TestDG_updateData.txt", "r")
        for line in f1:
            self.assertEqual(line, "")
        f1.close()
       
        self.assertEqual(test_ModuleD.updateData(test_data, update_index, test_update_name, test_update_number, test_filename)[update_index].name, test_update_name)
        self.assertEqual(test_ModuleD.updateData(test_data, update_index, test_update_name, test_update_number, test_filename)[update_index].number, test_update_number)                
       	
    
        test_entry = test_name + "," + test_num + "\n"
        test_entry1 = test_name1 + "," + test_num1 + "\n"
        test_entry2 = test_name2 + "," + test_num2 + "\n"
        # assert .txt file is updated with one entry 
        f2 = open("./tests/TestDG_updateData.txt", "r")
        i = 0;
        for line in f2:
            i+=1
            if (i==1):
                self.assertEqual(line, test_entry)
            if (i==2):
                self.assertEqual(line, test_entry1)
            if (i==3):
                self.assertEqual(line, test_entry2)
        f2.close() 
                
                 
    def test_deleteData_method(self):
        test_ModuleD = ModuleD(Mock(), ModuleG())
        
        # populate test data array
        test_name = "danny"
        test_name1 = "sammy"
        test_num = "437892"
        test_num1 = "789234"
        test_entry = test_name + "," + test_num + "\n"
        test_data = [Entry(test_name,test_num), Entry(test_name1,test_num1)]
        
        test_filename = "TestDG_deleteData.txt"
        delete_index = 1
        
        # assert .txt file is empty
        f1 = open("./tests/TestDG_deleteData.txt", "r")
        for line in f1:
            self.assertEqual(line, "")
        f1.close()
        

        # assert length of new list with element deleted
        self.assertEqual(len(test_ModuleD.deleteData(test_data, delete_index, test_filename)), 1)
                
        # assert list has remaining element left (also need to re-initialize test_data list)
        test_data = [Entry(test_name,test_num), Entry(test_name1,test_num1)]
        self.assertEqual(test_ModuleD.deleteData(test_data, delete_index, test_filename)[0].name, test_name)
        test_data = [Entry(test_name,test_num), Entry(test_name1,test_num1)]
        self.assertEqual(test_ModuleD.deleteData(test_data, delete_index, test_filename)[0].number, test_num)               


        f2 = open("./tests/TestDG_deleteData.txt", "r")
        i = 0;
        for line in f2:
            i+=1
            if (i==1):
                self.assertEqual(line, test_entry)

        f2.close() 
        
        
if __name__ == '__main__':
    unittest.main()
    
