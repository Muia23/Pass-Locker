#!/usr/bin/env python3.8
from user import User

def signup_user(username, password):
    '''

    Function to sign up a user

    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''

    Function to save user

    '''
    user.save_user()