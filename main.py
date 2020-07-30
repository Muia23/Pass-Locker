#!/usr/bin/env python3.8
from user import User
from credentials import Credential
import random
import string

Process = []
#sign in user


#program running
program_run = True


#exit program
def exit_program():
    global program_run
    program_run = False


#sign up user
def signup_user(username, password):
    '''

    Function to sign up a user

    '''
    new_user = User(username,password)
    return new_user


#save user
def save_users(user):
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
def check_existing_password(password):
    '''

    Function that checks if a password exists

    '''
    return User.password_exist(password)


#log in
def signin():
    '''

    Function to log in a user

    '''
    global program_run

    print('++++++++SIGN IN++++++++')
    print("Enter Username")
    username = input()

    if username == check_existing_user:
        
        print("Enter Password")
        password = input()

        if password == check_existing_password:
            print("logged in")
            cred()                

        else:
            print("Invalid password")

    else:
        print("User doesn't exist. Kindly Try again")
        print('\n')
        program_run = False        

#sign up
def signup():
    '''

    Function to sign up a user

    '''
    global program_run

    print('++++++++SIGN UP++++++++')
    print("Enter a Username")
    username = input()
    print('\n')

    print("Enter am password")
    password = input()
    print('\n')

    save_users(signup_user(username, password))
    print('\n')
    print("Account created")
    print('\n')
    print("Logged in...")
    print('\n')
    cred()

#create credential
def create_credential(uname,account,cpass):
    '''
    
    Function to create credential

    '''
    new_credential = Credential(uname,account,cpass)
    return new_credential


#save credential
def save_credential(credential):
    '''

    Function to save credential

    '''
    credential.save_credential()


#delete credential
def del_credential(credential):
    '''

    Function to delete credential

    '''
    credential.delete_credential()


#find credential
def find_credential(account):
    '''

    Function to find credentials using account

    '''
    return Credential.find_by_account(account)


#check if a credential exists
def check_existing_credential(account):
    '''

    Function to check if a credential exists

    '''
    return Credential.credential_exist(account)


#display all credentials
def display_credentials():
    '''
    
    Function that returns all saved credentials
    
    '''
    return Credential.display_credentials()

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


    


#main Function
def main():
    print('\n')
    print("Welcome to Pass-Locker.")
    print('\n')
    print("Use these short codes to:") 
    print("            si - SIGN IN                su - SIGN UP")
    short_code1 = input().lower()

    if short_code1 == 'si':
            signin()

    elif short_code1 == 'su':
            signup()

    else:
        print('\n')
        print("Error! Please use the short codes")
        print('\n')

def cred():
    while program_run:        
        print("Use these short codes to:") 
        print("     sc - SAVE A CREDENTIAL         cc - CREATE A NEW CREDENTIAL         dc - DISPLAY CREDENTIALS          fc - FIND A CREDENTIAL         so - SIGN OUT        ex - EXIT")
        short_code2 = input().lower()
        if short_code2 == 'sc':
            print('\n')
            print("You are saving a credential")
            print('\n')

            print ("Username....", )
            uname = input()        
            print('\n')
            
            print ("Application....") 
            account = input()
            print('\n')

            print("Password....")           
            cpass = input()
            print('\n')

        
            save_credential(create_credential(uname, account, cpass))
    
            print('\n')
            print(f"New credential          Username: {uname}          App: {account}          Password: {cpass}            created")
            print('\n')
            

        elif short_code2 == 'cc':
            print('\n')
            print("You are siging up for a new credential")
            print('\n')
    
            print ("Enter your names....") 
            name = input()
            print('\n')

            print ("Enter your email address....")
            email = input()
            print('\n')
            
            print ("Enter your phone number....")
            phone = input()
            print('\n')

            print ("Enter a desired Username....")
            print ("Remember should be unique")
            uname = input()
            print('\n')
            
            print ("Enter the App you want to sign up....")
            account = input()
            print('\n')

            print("Enter a password....")
            print("Would you accept a system generated password?")
            print("y/N")
            short_code3 = input().lower()
            
            if short_code3 == 'y':
                print("Auto generated")
                cpass = randomString()
            

            elif short_code3 == 'n':            
                print("A password should have: letters [A-Z][a-z], numbers[1-9], special characters[@,*,(,),&,%,_,-]")
                cpass = input()

            
            save_credential(create_credential(uname, account, cpass))
            print('\n')
            print(f"New credential       Username: {uname}           App: {account}          Password: {cpass}          created")
            print('\n')
            
        elif short_code2 == 'dc':
            if display_credentials():
                print('\n')
                print("Here is a list of all your credentials")
                print('\n')
                for credential in display_credentials():                
                    print(f" Username: {credential.login_name}")
                    print(f" App: {credential.account}")
                    print('\n')
                    
            else:
                print('\n')
                print("You haven't saved any credentials yet")
                print('\n')
                
        elif short_code2 == 'fc':
            print('\n')
            print("Enter the application you want to search for")
            search_account = input()
            if check_existing_credential(search_account):
                search_credential = find_credential(search_account)
                print('\n')
                print(f"Username: {search_credential.login_name}")                    
                print(f"App: {search_credential.account}")
                print('\n')
            else:
                print('\n')
                print("That credential does not exist")
                print('\n')
                
            
        elif short_code2 == "ex":
                print('\n')
                print("Bye ......")
                print('\n')
                exit_program()


        elif short_code2 == "so":
                print('\n')
                print("Signing Out ......")
                print('\n')
                main()


        else:
                print('\n')
                print("Error! Please use the short codes")
                print('\n')



if __name__ == '__main__':
    main()