#!/usr/bin/env python3

import file_creation_module
import account_module
import transaction_module


#use path.lib to set a home location
#pathlib.Path.home()


#test1

#this function asks the user to input the information for account creation
def sign_up(accounts_path):
    
    #checks if the user likes their info
    accept_info = False
    while accept_info == False:
        #passwords must be at least 8 chars
        password = str('0')
        while len(password) < 8:
            password = input('What do you want your password to be? ')
            if len(password) < 8:
                print ('Your password must be at least 8 characters ')
        
        first_name = input('What is your first name? ')
        last_name = input('What is your last name? ')

        print (f'Password: {password}, First Name: {first_name}, Last Name: {last_name}\n')
        
        if input('Is this information correct, yes or no? ').lower() == 'yes':
            accept_info = True
            account_number = str(file_creation_module.account_number_generator(accounts_path))
            file_creation_module.account_creation(accounts_path, account_number, password, first_name, last_name)
            print ('Account created successfully')
            print ('Your account information is as follows:')
            print (f'Account Number: {account_number} Password: {password}, First Name: {first_name}, Last Name: {last_name}\n')
            
        else:
            print ('Invalid input')

    
#this function lets a user login to an account
#once they've logged in, they can access the accounts transaction history
#they can add a new transaction, view their balance, or log out
def login(accounts_path):
    
    #while this flag is false, no account number has been found
    #this flag must be true in order to enter a password
    acc_num_checker_flag = False

    while acc_num_checker_flag == False:
        acc_num_checker = input('Please enter your account number: ')

        with open(accounts_path, 'r') as accounts_file:
            #start a for loop to go through each line
            #as we get to a line, we have to split it at the comma
            #then we check the first element in the list
            #if it matches the input, the account number is found
            #use enumerate to keep track of the line number
            for count, line in enumerate(accounts_file):
                split_line = line.split(', ')
                #if the number at the 0th position in the line matches the acc_num_checker
                #an account number has been found
                if split_line[0] == acc_num_checker:
                    acc_num_checker_flag = True
                    #this is the line number in the file where we found the account number
                    line_number = count
                    break
                
            if acc_num_checker_flag == True:
                print ('Account number found')
            else:
                print ('Account number not found')


    #password checker flag
    password_checker_flag = False
    #for some reason using a 3 here gives 4 attempts
    #fix later
    password_attempts = 2
    
    while password_checker_flag == False:
        password_checker = input('Please enter your password: ')
        
        if password_attempts == 0:
            print ('Too many failed password attempts, now exiting')
            return False, 0

        with open(accounts_path, 'r') as accounts_file:
            #list of all the lines in the accounts file where each item is 1 line from the file
            accounts_list = accounts_file.readlines()
            #split the string at index line_number into a list of separate values
            split_line = accounts_list[line_number].split(', ')
            #if the 2nd element in the split_line list matches the inputted password, the user has successfully logged in
            if split_line[1] == password_checker:
                password_checker_flag = True
                

        if password_checker_flag == True:
            #read the file to find someones name
            print (f'Password accepted, welcome to your homepage {split_line[2]}')
            logged_in = True
            return logged_in, line_number
        else:
            print ('Incorrect Password')
            print (f'Attempts remaining: {password_attempts}')
            password_attempts -= 1
            

#main function
def main():

    #this path may need to be variable for when we need to open specific file accounts
    #this could potentially be changed to user input
    accounts_path = 'accounts.txt'

    #this is the function which creates the accounts file list
    #this should always run when the program starts
    file_creation_module.accounts_file_creation(accounts_path)

    #this is an infinite loop that ends when you choose 'exit'

    while True:
        ask = input('Would you like to sign up, login, or exit? ').lower()
        if ask == 'sign up':
            sign_up(accounts_path)
        elif ask == 'login':
            #logged_in: true if the password was accepted, line_number: the line number at which the users account is
            logged_in, line_number = login(accounts_path)
            while logged_in == True:
                account_ask = input('Would you like to view your account, record a transaction, or generate a report (A/T/R)?  ').upper()
                if account_ask == 'A':
                    logged_in = account_module.account_options(accounts_path, line_number)
                elif account_ask == 'T':
                    logged_in = transaction_module.transaction_options(accounts_path, line_number)
                elif account_ask == 'R':
                    #call the report_module
                    pass
                else:
                    print ('Invalid input\n')
        elif ask == 'exit':
            print ('Exiting the program')
            exit(1)
        else:
            print ('Invalid input')


    
if __name__ == '__main__':
    main()