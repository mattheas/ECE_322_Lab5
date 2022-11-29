import unittest
from modules.ModuleG import ModuleG
from data.Entry import Entry

# no need to test FileNotFOundError in Module G as this would require student to intentionally change
# a files permission to be not readable by current user


class TestG(unittest.TestCase):
    
    def test_updateData_method(self):
    	
    	# declare test data
        test_filename = "./bottomuptests/TestG_updateData.txt"
        test_name = "name"
        test_name1 = "name1"
        test_num = "123456"
        test_num1 = "234098"
        data_list = [Entry(test_name,test_num), Entry(test_name1,test_num1)]
        
        # clear .txt and assert .txt file is empty
        f1 = open("./bottomuptests/TestG_updateData.txt", "w")
        f1.truncate(0)
        f1.close()
        
        f1 = open("./bottomuptests/TestG_updateData.txt", "r")
        for line in f1:
            self.assertEqual(line, "")
        f1.close()

        # call updateData method
        ModuleG.updateData(self,test_filename, data_list)

        # open file and use assertion calls to check data is written to .txt file correctly
        count = 0
        with open(test_filename) as fp:
            Lines = fp.readlines()
            first_line = True
            for line in Lines:
                count += 1
                values=line.strip().split(",")
                if (first_line):
                    first_line=False
                    self.assertEqual(values[0], test_name)
                    self.assertEqual(values[1], test_num)		
                else:
                    self.assertEqual(values[0], test_name1)
                    self.assertEqual(values[1], test_num1)
        fp.close()
if __name__ == '__main__':
    unittest.main()
