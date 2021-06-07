#file a transaction
#any changes to the users balanace should be reflected in the account file

import datetime

def transaction_options(accounts_path, line_number):

    stay_logged_in = True
    while stay_logged_in == True:
        ask = input('Would you like to make a transaction, return to the homepage, or logout (T/H/L)? ').upper()
        if ask == 'T':
            transaction(accounts_path, line_number)
        elif ask == 'H':
            return homepage()
        elif ask == 'L':
            return logout()
        else:
            print ('Invalid input')


def transaction(accounts_path, line_number):

    person_involved = input('First input the other entity involved in the transaction: ')
    transaction_amount = ''
    continue_transaction = True

    while continue_transaction == True:
        money = input("Next tell us the money transferred, if you spent money add a '-' in front of the amount: ")
        money_list = []
        money_list[:0] = money
        if money_list[0] == '-':
            money_list[0] = '0'
        for num in money_list:
            if num.isnumeric() == False:
                print ('money only contains numbers')
                continue
        
        #if the hyphen was changed to a 0, change it back
        if money_list[0] == '0':
            money_list[0] = '-'
        #convert the list back into a string
        for num in money_list:
            transaction_amount += num
        continue_transaction = False



    #ask the user for the date of the transaction
    #syntax check for the date
    #write the other entity, amount of money, and date into the transaction history file

    enter_date = True
    while enter_date == True:
        date_of_transaction = input('Lastly, tell us the date this transaction occurred, use the format yyyy-mm-dd: ')
        format = '%Y-%m-%d'
        try:
            datetime.datetime.strptime(date_of_transaction, format)
        except ValueError:
            print ('This is the incorrect date format, please try again')
            continue
        break

    
    #get the account number so we can open their transaction history
    with open(accounts_path, 'r') as accounts_file:
        #list of all the lines in the accounts file where each item is 1 line from the file
        accounts_list = accounts_file.readlines()
        #split the string at index line_number into a list of separate values
        split_line = accounts_list[line_number].split(', ')
        #if the 2nd element in the split_line list matches the inputted password, the user has successfully logged in
        account_number = split_line[0]


    #this needs to print on a newline
    with open (f'{account_number}.txt', 'a') as transaction_history:
        transaction_history.write(f'{person_involved}, {transaction_amount}, {date_of_transaction}\n')




    #open the file
    #find the line where the account number matches
    #change the balance value
    #re write the whole file

    

    # with open(accounts_path, 'r') as accounts_file:
    #     #list of all the lines in the accounts file where each item is 1 line from the file
    #     accounts_list = accounts_file.readlines()
    #     #split the string at index line_number into a list of separate values
    #     split_line = accounts_list[line_number].split(', ')
    #     #if the 2nd element in the split_line list matches the inputted password, the user has successfully logged in
    #     account_number = split_line[4]





def homepage():
    print ('Returning to the homepage')
    return True

def logout():
    print ('Logging you out now, returning to login screen')
    return False
