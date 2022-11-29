# tests/TestRunner.py
#The basic idea here is to have a new Python file Testrunner.py
# alongside your tests that contains our runner.
import unittest

# import your tests modules (Apply integration testing method)
import TestModuleA
import TestModuleAB
import TestModuleAC
import TestModuleAD
import TestModuleAE
import TestModuleBF
import TestModuleCF
import TestModuleDF
import TestModuleDG
import TestModuleABCDEFG
# .... Complete the missing imports



# initialize the tests suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the tests suite
suite.addTests(loader.loadTestsFromModule(TestModuleA))
suite.addTests(loader.loadTestsFromModule(TestModuleAB))
suite.addTests(loader.loadTestsFromModule(TestModuleAC))
suite.addTests(loader.loadTestsFromModule(TestModuleAD))
suite.addTests(loader.loadTestsFromModule(TestModuleAE))
suite.addTests(loader.loadTestsFromModule(TestModuleBF))
suite.addTests(loader.loadTestsFromModule(TestModuleCF))
suite.addTests(loader.loadTestsFromModule(TestModuleDF))
suite.addTests(loader.loadTestsFromModule(TestModuleDG))
suite.addTests(loader.loadTestsFromModule(TestModuleABCDEFG))
# .... Complete the missing additions


# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
