import unittest
import CalcSimple
import StringIO
import sys
import HTMLTestRunner

reload(CalcSimple)

# Create list of test cases
testList = []
testList.append(CalcSimple.BaseActionsTests)
testList.append(CalcSimple.ExtendsActionsTests)
testLoad = unittest.TestLoader()

# Assemble test cases into suite list
caseList = []
for testCase in testList:
	testSuite = testLoad.loadTestsFromTestCase(testCase)
	caseList.append(testSuite)

# Create TestSuite
suite = unittest.TestSuite(caseList)

# Run tests
if len(sys.argv) > 1 and sys.argv[1] == "html":
    runner = unittest.TextTestRunner(verbosity=1)
    filename = "Test1.html"
    output = open (filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(
             stream=output,
             title="Test report"
         )
    runner.run(suite)
else:
    unittest.TextTestRunner(verbosity=2).run(suite)

