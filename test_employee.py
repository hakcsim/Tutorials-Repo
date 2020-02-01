import unittest
from unittest.mock import patch
from employee import Employee

# test dose not always run in the same order

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # this is called before any test function call
        print('call setUpClass')

    @classmethod
    def tearDownClass(cls):
        # this is called after all test function call
        print('call tearDownClass')

    def setUp(self):
        # this is called before each test function call
        print('call setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 70000)

    def tearDown(self):    
        # this is called after each test function call
        print('call tearDown')

    def test_email(self):

        print('test_email')    

        self.assertEqual(self.emp_1.email, f'Corey.Schafer@company.com')
        self.assertEqual(self.emp_2.email, f'Sue.Smith@company.com')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, f'John.Schafer@company.com')
        self.assertEqual(self.emp_2.email, f'Jane.Smith@company.com')

    def test_fullname(self):

        print('test_fullname')    

        self.assertEqual(self.emp_1.fullname, f'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, f'Sue Smith')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, f'John Schafer')
        self.assertEqual(self.emp_2.fullname, f'Jane Smith')

    def test_apply_raise(self):

        print('test_apply_raise')    

        self.assertEqual(self.emp_1.pay, 50000)
        self.assertEqual(self.emp_2.pay, 70000)
        
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 73500)

    def test_monthly_schedule(self):

        print('test_monthly_schedule')    

        # use mock when the code is dependent on external resources that 
        # are outside the control of the code. 
        # Do not want test to fail if website is down because it is not
        # a program / code error - use mocked patch 
        # Below employee will use to the mock_get patch instead of the 
        # actual request.get function - i.e. it does not go to the 
        # actual website  
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')                           
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')                           
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()