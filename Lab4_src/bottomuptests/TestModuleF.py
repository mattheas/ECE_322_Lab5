import unittest
from modules.ModuleF import ModuleF
from contextlib import redirect_stdout
from data.Entry import Entry


class TestF(unittest.TestCase):
    
    def test_displayData_method(self):
        test_ModuleF = ModuleF()
        
        with open('./bottomuptests/TestF_print_data_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                #call method with empty data list, and one element data list
                test_ModuleF.displayData([])
                test_ModuleF.displayData([Entry("chazzmichaelmichael", "4312")])
        f1.close()
        
        # assert contents of expected file is the same as actual
        f1 = open("./bottomuptests/TestF_print_data_actual.txt", "r")
        f2 = open("./bottomuptests/TestF_print_data_expected.txt", "r")
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
