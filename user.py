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

    @classmethod
    def user_exist(cls,username):
        '''

        Method checks if user exists from the user list.
        Args:
            username: Username to search if they already have accounts
        Returns:
            Boolean: True or false depending if the username account exists

        '''
        for user in cls.user_list:
            if user.username == username:
                    return True
        
        return False