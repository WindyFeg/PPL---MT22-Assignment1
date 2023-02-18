testcases = []
while True:
    name = input("Enter your Test name: ")
    number = input("Input number: ")
    testcase = input("testcase: \n")
    expected = input("solution: \n")
    testcases.append("def " + name +"(self):\n")
    testcases.append("        \"\"\"test " + name +"\"\"\"\n")
    testcases.append("        self.assertTrue(TestLexer.test(\""+ testcase+"\", \""+ expected+" ,<EOF>\", "+ number+"))\n")
    stop = input("Continue? (y/n)")
    if stop == 'n':
        break

for testcase in testcases:
    print(testcase)
