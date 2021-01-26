import unittest

class Test_Add(unittest.Testcase):

	def Adding(num_1: int, num_2:int, num_3:int) -> int:
		Output = num_1 + num_2 + num_3
		return output 
	
	
	def test_add(self):
		for i in range(1, 200):
		with self.subtest(i = i):
		self.assertEqual(Test_Add.add(i), Test_Add.output[i]

    # Unit testing
    def test_add_1():
        test_1 = add(1, 1 , 1)
        test_2 = add(2, 3 , 4)
        test_3 = add(5, 5 , 5)

        assert test_1 == 3
        assert test_2 == 9
        assert test_3 == 15

    print("Code tested. No errors.")
    

# excerise for own use

def sum(a,b,c):
    return a + b + c
def tearDown(self):
        print("tear down called...")



#test class
class Sumfunction(unittest.TestCase):
    def setUp(self):
        print("setup is called...")
        self.a=10
        self.b=20
        self.c=30
        #prerequistes called
    
    def test_sumfunction(self):
        print("test is called...")

        #arrange data to work
        
        #act call on code on the test
        result =sum(self.a,self.b,self.c)
        #assert verify expected result
        self.assertEqual(result, self.a + self.b + self.c)

#invoke unittest framework
if __name__ == "__main__":
    unittest.main()
