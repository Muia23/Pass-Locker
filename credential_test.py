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


    def test_save_credential(self):
        '''

        Test if credential is saved to list

        '''
        
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)


    def test_save_multiple_credentails(self):
        '''

        Test on saving multiple credentials

        '''
        self.new_credential.save_credential()
        test_credential = Credential("Test","testAccount","testPass")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)


    def test_delete_credential(self):
        '''

        Test if we can remove a credential

        '''
        self.new_credential.save_credential()
        test_credential = Credential("Test","testAccount","testPass")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_find_credential_by_account(self):
        '''

        Test if we can find a credential by account

        '''
        self.new_credential.save_credential()
        test_credential = Credential("Test","testAccount","testPass")
        test_credential.save_credential()        

        found_credential = Credential.find_by_account("testAccount")

        self.assertEqual(found_credential.login_name,test_credential.login_name)



if __name__ == '__main__':
    unittest.main()
