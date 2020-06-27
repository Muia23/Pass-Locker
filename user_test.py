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


    def test_init(self):
        '''

        Tests if the object is instantiated correctly"

        '''
        self.assertEqual(self.new_user.username,"Wilfred")
        self.assertEqual(self.new_user.password,"wil1234")
    
    def test_save_user(self):
        '''

        Test if user is saved in user_list
        
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)




if __name__ == '__main__':
    unittest.main()