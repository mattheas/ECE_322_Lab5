import unittest
from modules.ModuleE import ModuleE
from contextlib import redirect_stdout


class TestE(unittest.TestCase):

    def test_exitProgram_method(self):            
        with open('./bottomuptests/TestE_redirect_output_actual.txt', 'w') as f1:
            with redirect_stdout(f1):
                try:
                    ModuleE.exitProgram(self)
                except SystemExit:
                    pass   
        f1.close()
        
        # assert contents of expected file is the same as actual
        f1 = open("./bottomuptests/TestE_redirect_output_actual.txt", "r")
        f2 = open("./bottomuptests/TestE_redirect_output_expected.txt", "r")
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
    
