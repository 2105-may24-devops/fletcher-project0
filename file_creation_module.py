#!/usr/bin/env python3
import os
import random
#this module is in charge of creating all new text files
#imported to project0.py


#this function always runs whenever the program is started
#its goal is to check whether the accounts file exists
#if it doesnt exist, it creates a new accounts file
#the accounts file stores all the metadata for each bank account
def accounts_file_creation(accounts_path):

    #this checks if the accounts_path is accurate, if not it means the accounts.txt doesnt exist
    is_file = os.path.isfile(accounts_path)

    #if accounts.txt doesnt exist we create a new file with the default columns
    if not is_file:
        with open(accounts_path, 'w') as accounts_file:
            #write the columns for the accounts file
            lines_to_write = 'Account Number, Password, First Name, Last Name, Email Address, Phone Number, Balance'
            accounts_file.write(lines_to_write)
            print ('New accounts file created\n')

#this function randomly generates an account number
def account_number_generator(accounts_path):
    #this is used to check if there are 2 accounts with the same account number
    #account numbers must be unique so if there is a duplicate we must generate a new number
    with open (accounts_path, 'r') as accounts_file:
        account_number_duplicate = True
        while account_number_duplicate == True:
            account_number = str(random.randint(1000000000, 999999999999))
            for line in accounts_file:
                split_line = line.split(', ')
                if split_line[0] == account_number:
                    continue
            account_number_duplicate = False
    return account_number

#this function takes input from the sign_up function in order to append the account to the accounts file
#this function is automatically called at the end of the sign_up function
def account_creation(accounts_path, account_number, password, first_name, last_name, email_address, phone_number):
    #once the user likes all of the info, we append it to a newline in the accounts file
    #each entry is separated by commas
    with open(accounts_path, 'a') as accounts_file:
        #appends a newline and the user info
        accounts_file.write('\n')
        accounts_file.write(f'{account_number}, {password}, {first_name}, {last_name}, {email_address}, {phone_number}, 0')
        #call a function to read from the file
        transaction_history_file_creation(account_number)


#this function creates the transaction history file
#this function is automatically called at the end of the account_creation function
def transaction_history_file_creation(account_number):
        #this is the path for creating the transaction history file with the account number as its name
        transaction_history_path = f'{account_number}.txt'

        #create a new text file with the account number as its name
        with open(transaction_history_path, 'w') as transaction_history_file:
            #writes the default columns for the transaction history
            lines_to_write = 'Transaction Associate, Money Exchanged, Date of Transaction, Balance'
            transaction_history_file.write(lines_to_write)
            print ('New transaction history file created\n')


def user_confirmation_file():
    pass
