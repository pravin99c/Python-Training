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
from multiprocessing import Manager
import random


class Users():
    def __init__(self,username,mobile_no,address, opening_balance):
        self.username=username
        self.mobile_no=mobile_no
        self.address=address
        self.account_no = random.randrange(1,999999999999)
        self.balance = opening_balance
    def __str__(self):
        return f'{self.username}\n{self.mobile_no}\n{self.address}\n{self.account_no}\nBalance: ${self.balance:.2f}\n'
class User_manager(Users):
    def __init__(self):
        self.users_list = []
        print(self.users_list)

# class ATM(User_manager):
#     print(hello)
    
def main():
    customer_list=[]
    while True:
        print("1 = Creating New Account ")
        print("2 = View Balance ")
        print("3 = Deposit ")
        print("4 = Withdraw ")
        print("5 = Close Account ")
        print("6 = exit")
        select1=int(input("select your choice : "))

        if select1 == 1:
            while True:
                try:
                    user_name=input("Enter user name : ")
                    mobile_no=int(input("Enter mobile number in digit :"))
                    address=input("Enter user Address :")
                    opening_balance=int(input("Enter opening balance"))
                    user_ditails=Users(user_name,mobile_no,address,opening_balance)
                    Managers=User_manager
                    Managers.no_of_users.append(user_ditails)
                except Exception as e:
                    print(e)
                    print("Enter digit number 10")
                else:
                    break
        elif select1 == 2:
            try:
                account_no=Users.account_no
                print(account_no)
                Account_no=input("Enter Account Number : ")
                if Account_no==account_no:
                    print("hello")
            except Exception as e:
                print(e)
            else:
                break
        elif select1 == 3:
            try:
                user_name=input("Enter user name : ")
                mobile_no=int(input("Enter mobile number in digit"))
            except Exception as e:
                print(e)
            else:
                break
        elif select1 == 4:
            try:
                user_name=input("Enter user name : ")
                mobile_no=int(input("Enter mobile number in digit"))
            except Exception as e:
                print(e)
            else:
                break
        elif select1 == 5:
            print("hello5")
        elif select1 == 6:
            break

main()