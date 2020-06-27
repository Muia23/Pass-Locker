#users
#verify and log in to credentials
#new locker_user
class User:
    """

    Class generates new instance of users
    
    """

    user_list = []

    def __init__(self,username, password):

        """

        __init__ method helps us define properties for out object.

        Args:
            username : New user name.
            password : New password.
            account : New account.

        """
        self.username = username
        self.password = password


    def save_user(self):
        '''
        Method saves user object into user_list

        '''
        User.user_list.append(self)