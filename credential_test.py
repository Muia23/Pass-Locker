import unittest 
from credentials import Credential

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
    
        Method runs before each test.

        '''
        self.new_credential = Credential("wilfred", "instagram","wilpass")

    def tearDown(self):
        '''
        
        Method clears up after each test we run

        '''
        Credential.credential_list = []
    
    def test_init(self):
        '''

        Test if the object is initialized properly

        '''

        self.assertEqual(self.new_credential.login_name,"wilfred")
        self.assertEqual(self.new_credential.account,"instagram")
        self.assertEqual(self.new_credential.credential_pass,"wilpass")



if __name__ == '__main__':
    unittest.main()
