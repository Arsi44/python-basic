import unittest
import test_calc

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(test_calc.CalcTest))
calcTestSuite.addTest(unittest.makeSuite(test_calc.CalcExTests))
print("count of tests: " + str(calcTestSuite.countTestCases()) + "\n")
runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)