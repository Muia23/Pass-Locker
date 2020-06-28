#!/usr/bin/env python3.8
from user import User
from credentials import Credential
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


    
#main Function
def main():
    print('\n')
    print("Welcome to Pass-Locker.")
    print('\n')
    while program_run:        
        print("Use these short codes to:") 
        print("si - sign in, su - sign up, sc - save a credential, cc - create credential, dc - display credential, fc - find credential ex - exit Pass-Locker")
        short_code = input().lower()

        if short_code == 'si':
            signin()
            

        elif short_code == 'sc':
            print('\n')
            print("You are saving a credential")
            print('\n')

            print ("Username....")
            uname = input()
            

            print ("Account....")
            account = input()


            print("Password....")
            cpass = input()

            save_credential(create_credential(uname, account, cpass))
            print('\n')
            print(f"New credential {uname} {account} created")
            print('\n')
            

        elif short_code == 'cc':
            print('\n')
            print("You are siging up for a new credential")
            print('\n')

            print ("Enter your names....")
            name = input()

            print ("Enter your email address....")
            email = input()
            
            print ("Enter your phone number....")
            phone = input()

            print ("Enter a desired Username....")
            print ("Remember should be unique")
            uname = input()
            

            print ("Enter the App you want to sign up....")
            account = input()

            print("Enter a password....")
            print("A password should have: letters [A-Z][a-z], numbers[1-9], special characters[@,*,(,),&,%,_,-]")
            cpass = input()

            save_credential(create_credential(uname, account, cpass))
            print('\n')
            print(f"New credential {uname} {account} created")
            print('\n')
            


        elif short_code == 'dc':

            if display_credentials():
                print('\n')
                print("Here is a list of all your credentials")
                print('\n')

                for credential in display_credentials():                
                    print(f"{credential.login_name} {credential.account}")
                    print('\n')
                    
            else:
                print('\n')
                print("You haven't saved any credentials yet")
                print('\n')
                

        elif short_code == 'fc':
            print('\n')
            print("Enter the account you want to search for")

            search_account = input()
            if check_existing_credential(search_account):
                search_credential = find_credential(search_account)
                print('\n')
                print(f"{search_credential.login_name} {search_credential.account}")
                print('\n')

            else:
                print('\n')
                print("That credential does not exist")
                print('\n')
                
            
        elif short_code == "ex":
                print('\n')
                print("Bye ......")
                print('\n')
                exit_program()

        else:
                print('\n')
                print("Error! Please use the short codes")
                print('\n')



if __name__ == '__main__':
    main()