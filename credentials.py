class Credential:

    '''
    
    Class that generates new instance of credentials

    '''
    #Credentials list
    credential_list = []

    def __init__(self,login_name, account, credential_pass):
        self.login_name = login_name
        self.account = account
        self.credential_pass = credential_pass

    def save_credential(self):
        '''
    
        method to save credentials in the ist

        '''
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''

        method to delete a credential
        
        '''
        Credential.credential_list.remove(self)

    
    @classmethod
    def find_by_account(cls,account):
        '''

        method that takes in an account and returns a credential that matches that account"


        '''
        for credential in cls.credential_list:
            if credential.account == account:
                return credential

    @classmethod
    def credential_exist(cls,account):
        '''

        Method that checks if a contact exists from the list.

        '''
        for credential in cls.credential_list:
            if credential.account == account:
                return True
        
        return False
    
    @classmethod
    def display_credentials(cls):
        '''

        method that displays all credentials saved

        '''
        return cls.credential_list














#account
#account_username
#account_password

#new Credentials
#choose account
#make account_username
#account_password is autogenerated
 #change account_password