# 4.Create a class for Users,
# username
# account no
# mobile no
# address
# account balance
# -> Create a class for user manager
# Manages user => Add new user, Get existing user, remove user
# -> Create a class for ATM,
# Enter account no and get user if not found then show a valid message
# Show options for user operations like creating new users, View Balance. Deposit, Withdraw, Close account, etc...
# Transaction charge: 0.5 for every operation
# Account balance limit: 10000 



# from os import remove

import random



class Users():
    def __init__(self,username,mobile_no,address, balance,account_no):
        self.username=username
        self.mobile_no=mobile_no
        self.address=address
        self.account_no = account_no
        self.balance = balance
    # def __str__(self):
    #     return f'{self.account_no}\nBalance: ${self.balance:.2f}\n'
class Manager():
    def __init__(self):   
        self.users_list = []
    def get_existing_user(self):
        if len(self.users_list) == 0:
            print('Accounts not found')
        else:
            for user in self.users_list:
                print('Ac. No.:{0} \n Account balance:{1} '.format(user.account_no,user.balance))
    

class ATM():
    def check_account(users_list,Account_no):
        for user in users_list:
            if user.account_no == Account_no:
                return user
        return False

Managers=Manager()

def main():
    customer_list=0
    print(customer_list)
    Managers=Manager()
    print(" Welecome to Bank Of Broda ")
    while True:
        print("1 = Banking ")
        print("2 = exit")
        select1=int(input("select your choice : "))
        if select1 not in (1, 2):
            print('Plsease select the valid option')
            continue
        elif select1 == 1:
            print("Welcome to Banking")
            while True:
                option = int(input('\nHow Can We Assist you\tPlease enter your options:\n 1: Open a new Account\n 2: Deposit money and Withdraw money and remove account in your account\n 3: Exit the Bank\n Plase Enter : '))
                if option not in (1, 2, 3):
                        print('Please select the valid option')
                        continue
                if option == 1:#Open a new Account
                    try:
                        user_name=input("Enter user name : ")
                        mobile_no=int(input("Enter mobile number in digit : "))
                        address=input("Enter user Address : ")
                        account_no = random.randrange(1,999999999999)
                        while True:
                            balance=int(input("Enter opening balance : "))
                            if balance < 10000:
                                print("Please enter minimum amount is 10000 ")
                            else:
                                break
                        user_ditails=Users(user_name,mobile_no,address,balance,account_no)
                        Managers.users_list.append(user_ditails)
                        customer_list = len(Managers.users_list)+1 
                        print('Ac. No.:{0} \n Account balance:{1} '.format(account_no,balance))
                    except Exception as e:
                        print(e)
                        continue
                elif option == 2:#Deposit money in your account
                    Account_no = int(input('Enter account no: '))
                    user_obj = ATM.check_account(Managers.users_list,Account_no)
                    if user_obj:
                        while True:
                            add_option = int(input('\nHow Can We Assist you\tPlease enter your options:\n 1: Deposit money in your account \n 2: Withdraw Amount\n 3: Remove Account \n 4: Exit the Bank\n Plase Enter : '))
                            if add_option not in (1, 2, 3, 4):
                                    print('Please select the valid option')
                                    continue
                            if add_option == 1:
                                get_amount = int(input('Enter amount: '))
                                user_obj.balance = int(user_obj.balance) + get_amount     
                                print('Now your current balance is',user_obj.balance)
                            elif add_option == 2:
                                get_amount = int(input('Enter amount: '))
                                if int(user_obj.balance) - get_amount >= 0:
                                    user_obj.balance = int(user_obj.balance) - get_amount - 0.5  
                                    print('Now your current balance is',user_obj.balance)
                                else:
                                    print('Please try agian! Your current balance is {0}'.format(user_obj.balance))
                            elif add_option == 3:
                                Managers.users_list.remove(user_obj)
                                break
                            elif add_option == 4:
                                break
                elif option == 3:
                    break
        elif select1 == 2:
            break
main()

