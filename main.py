#!/usr/bin/env python3.8
from user import User
from credentials import Credential
#sign in user



#sign up user
def signup_user(username, password):
    '''

    Function to sign up a user

    '''
    new_user = User(username,password)
    return new_user

#save user
def save_user(user):
    '''

    Function to save user

    '''
    user.save_user()

#check existing username
def check_existing_user(username):
    '''

    Function that check if a user exists with that username and return a Boolean

    '''
    return User.user_exist(username)

#check existing password


#log in

def signin():
    '''
    '''
    print("Enter Username")
    search_username = input()

    if check_existing_user(search_username):
        print("Enter Password")
        search_password = input()

        if search_password == "Muia":
            print("logged in")                

        else:
            print("Invalid password")

    else:
        print("User doesn't exist. Kindly Try again")
        print('\n')
        signin()        
    
#create credential
def create_credential(uname,account,cpass):
    '''
    
    Function to create credential

    '''
    new_credential = Credential(uname,account,cpass)
    return new_credential

def 

    #save credential

    #delete credential

    #find credential

    #display all credentials
    

def main():
    print("Welcome to Pass-Locker.")
    print('\n')
    print("Use these short codes to: si - sign in, su - sign up, ex - exit Pass-Locker")
    short_code = input().lower()

    if short_code == 'si':
        signin()
        

if __name__ == '__main__':

    main()