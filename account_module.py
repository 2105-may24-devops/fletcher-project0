import os

def account_options(accounts_path, line_number):

    stay_logged_in = True
    
    while stay_logged_in == True:
        ask = input('Would you like to see your account info, delete your account, return to the home page, or logout (I/D/H/L)? ').upper()
        if ask == 'I':
            print_account_info(accounts_path, line_number)
        elif ask == 'D':
            return delete_account(accounts_path, line_number)
        elif ask == 'H':
            #homepage always returns true, and then account_options is returning that to main
            return homepage()
        elif ask == 'L':
            #logout always returns false, and then account_options is returning that to main
            return logout()
        else:
            print ('Invalid input')

def print_account_info(accounts_path, line_number):
    
    with open(accounts_path, 'r') as accounts_file:
        accounts_list = accounts_file.readlines()
        print ()
        print (f'{accounts_list[0]}{accounts_list[line_number]}\n')

def delete_account(accounts_path, line_number):

    with open (accounts_path, 'r') as accounts_file:
        accounts_list = accounts_file.readlines()
        split_line = accounts_list[line_number].split(', ')
        balance = int(split_line[6])
        if balance < 0:
            print ('Accounts with a balance of 0 or less cannot be deleted, please pay back your debt first')
            print ('Returning to account options page')
            return True
        
        #delete the transaction history file
        os.remove(f'{split_line[0]}.txt')

        print ('A check for your remaining balance has been generated')
        with open (f'Check for {split_line[2]} {split_line[3]}.txt', 'w') as check_file:
            check_file.write(f'Your remaining balance of {split_line[6]} will be mailed to you in 7 to 10 business days')
        

        del accounts_list[line_number]
        with open (accounts_path, 'w') as accounts_file:
            for line in accounts_list:
                accounts_file.write(line)
        print(f"Account successfully deleted, we're sorry to see you go {split_line[2]}")
        return logout()

def homepage():
    print ('Returning to the homepage')
    return True

def logout():
    print ('Logging you out now, returning to login screen')
    return False