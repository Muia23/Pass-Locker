import unittest
from user import User

class TestUser(unittest.TestCase):

    '''

    Defines test cases for the user class behaviours.

    '''

def setUp(self):
    '''
    
    Method runs before each test.

    '''
    self.new_user = User("Wilfred", "wil1234")


if __name__ == '__main__':
    unittest.main()