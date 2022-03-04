# Program: 5
# Create class Person:
# Name,DOB,City,Contact No
# Create class Employee (Inherit person class)
# employee id,joining date,salary,department,post
# Employee manager class
# Add/Remove Employee, Get all employees list, get employee by his name, get all employees by his/her department,
# Task:
# Add few employees
# Print all the employees
# Find an employee with the name
# Print all employees with department Finance
# Find all employees whose salary is greater than 50000
# Find all employees whose salary is bet ween 50000-100000
# Find a list of employees who are joined in the current year
# Find all employees who are from Mirzapur
# Find employees whose birthday in the current month
# Sort employee list with salary in descending order
#importing datetime class  
import datetime,random,time


class Person():
    def __init__(self,Name,DOB,City,Contact_no):
        self.Name=Name
        self.DOB=DOB
        self.City=City
        self.Contact_no=Contact_no

class Employee(Person):
    def __init__(self,Name,DOB,City,Contact_no,Emploayer_id,Joining_date,Salary,Department,Post):
        self.Emploayer_id=Emploayer_id
        self.Joining_date=Joining_date
        self.Salary=Salary
        self.Department=Department
        self.Post=Post
        super().__init__(Name,DOB,City,Contact_no)        
class Manager():
    def __init__(self):
        self.employee_list=[]
    def remove_emp(self,id):
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            for i in self.employee_list:
                if id == i.Emploayer_id:
                    self.employee_list.remove(i)
    def Show_all_Employee(self):
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            count=1
            for i in self.employee_list:
                print("Employer Number : ",count)
                print(' List of Employers : {0} \n Name : {1} \n DOB : {2} \n City : {3} \n contact : {4} \n id : {5} \n joining : {6} \n salary : {7} \n department : {8} \n post : {9}'.format(count,i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
                count += 1
    def choices(self,choice):
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            for i in self.employee_list:
                if choice == i.Name or choice == i.DOB or choice == i.Department or choice == i.City or int(choice) == i.Emploayer_id or choice == i.Post or int(choice) == i.Contact_no or choice == i.Joining_date:
                    print('\n Name : {0} \n DOB : {1} \n City : {2} \n contact : {3} \n id : {4} \n ioining : {5} \n salary : {6} \n department : {7} \n post : {8}'.format(i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
    def Find_current_year(self):
        CurrentDate=datetime.date.today()  
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            day,mount,year = (self.Joining_date).split("/")
            print(day)
            for i in self.employee_list:
                if int(year)==CurrentDate.year:
                    print('\n Name : {0} \n DOB : {1} \n City : {2} \n contact : {3} \n id : {4} \n joining : {5} \n salary : {6} \n department : {7} \n post : {8}'.format(i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
    def Find_current_month(self):
        CurrentDate=datetime.date.today()  
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            day,month,year = (self.Joining_date).split("/")
            for i in self.employee_list:
                if int(month)==CurrentDate.month:
                    print('\n Name : {0} \n DOB : {1} \n City : {2} \n contact : {3} \n id : {4} \n joining : {5} \n salary : {6} \n department : {7} \n post : {8}'.format(i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
    def Find_current_day(self):
        CurrentDate=datetime.date.today()  
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            day,month,year = (self.Joining_date).split("/")
            for i in self.employee_list:
                if int(day)==CurrentDate.day:
                    print('\n Name : {0} \n DOB : {1} \n City : {2} \n contact : {3} \n id : {4} \n joining : {5} \n salary : {6} \n department : {7} \n post : {8}'.format(i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
                            
    def Find_salary_geraterthan(self):
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            for i in self.employee_list:
                if i.Salary >= 50000:
                    print('\n Name : {0} \n DOB : {1} \n City : {2} \n contact : {3} \n id : {4} \n ioining : {5} \n salary : {6} \n department : {7} \n post : {8}'.format(i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
    def Find_between_50000_100000(self):
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            for i in self.employee_list:
                if i.Salary < 100000 and i.Salary > 50000:
                    print('\n Name : {0} \n DOB : {1} \n City : {2} \n contact : {3} \n id : {4} \n ioining : {5} \n salary : {6} \n department : {7} \n post : {8}'.format(i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
    def Find_less_50000_and_gerater_100000(self):
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            for i in self.employee_list:
                if i.Salary > 100000 or i.Salary < 50000:
                    print('\n Name : {0} \n DOB : {1} \n City : {2} \n contact : {3} \n id : {4} \n ioining : {5} \n salary : {6} \n department : {7} \n post : {8}'.format(i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
    def Find_sort_salary(self):
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            self.employee_list.sort(key = lambda x:x.Salary, reverse = True)
            for i in self.employee_list:
                print('\n Name : {0} \n DOB : {1} \n City : {2} \n contact : {3} \n id : {4} \n ioining : {5} \n salary : {6} \n department : {7} \n post : {8}'.format(i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
def main():
    print("************ Welcome ***************")
    details=Manager()
    while True:
        time.sleep(0.5)
        select=int(input("\n Enter 1 : Enter \n Enter 2 : Exit \n Plase Enter : "))
        if select not in (1,2):
            print('Plsease select the valid option')
            continue
        # create  Account in my function
        if select == 1:
            while True:
                time.sleep(0.5)
                print(" ************************************************* ")
                try:
                    add_option=int(input("\n Enter 1 : Create  Account And Remove Account \n Enter 2 : Show All Employee  and Find Employee \n Enter 3 : Find current day to month and year To Employee \n Enter 4 : Find salary greaterthan 50000 for Employee \n Enter 5 : Exit \n Plase Enter : "))
                    if add_option not in (1,2,3,4,5):
                        print('Plsease select the valid option')
                        continue
                    if add_option == 1:    
                        print("************  Create your Account  ***************")
                        while True:
                            time.sleep(0.5)
                            option=int(input("\n Enter 1 : Create person Account \n Enter 2 : Remove Employee \n Enter 3 : Exit \n Plase Enter : "))
                            if option not in (1,2,3):
                                print('Plsease select the valid option')
                                continue
                            # create Person Account in my function
                            if option == 1:
                                while True:
                                    try:
                                        Name = input(" Enter your Person Name : ")
                                        DOB = input(" Enter your date of birth (d/m/y): ")
                                        City = input(" Enter your City : ")
                                        Contact_no=int(input(" Enter your mobile number : "))
                                        Emploayer_id=random.randrange(1,10)
                                        Joining_date=input(" Enter your joining date(d/m/y): ")
                                        Salary=int(input(" Enter your salary for minimum 50000 : "))
                                        Department=input(" Enter your department : ")
                                        Post=input(" Enter your Post : ")
                                    except Exception as e:
                                        print(" ",e)
                                    else:
                                        employee=Employee(Name,DOB,City,Contact_no,Emploayer_id,Joining_date,Salary,Department,Post)
                                        details.employee_list.append(employee)
                                        break
                            elif option == 2:
                                id = int(input("Enter Employer Id : "))
                                details.remove_emp(id)
                            elif option == 3:
                                break
                    elif add_option == 2:#2 : Show All Employee
                        while True:
                            time.sleep(0.5)
                            print(" ************************************************* ")
                            Show_employee=int(input("\n Enter 1 : Show All Employee \n Enter 2 : Show your Choice \n Enter 3 :  Exit \n Plase Enter : "))
                            if Show_employee not in (1,2,3):
                                print('Plsease select the valid option')
                                continue
                            if Show_employee == 1:
                                details.Show_all_Employee()
                                time.sleep(0.5)
                            elif Show_employee == 2:
                                choice=input(" Enter your choices : ")
                                details.choices(choice)
                                time.sleep(0.5)
                            elif Show_employee == 3:
                                break
                    elif add_option == 3:#5 : Find current year To Employee
                        while True:
                            time.sleep(0.5)
                            print(" ************************************************* ")
                            find_dat_time=int(input("\n Enter 1 : Show All Employee \n Enter 2 : Find name of Employee \n Enter 3 : Find department to Employee \n Enter 4 : Exit  \n Enter your Choice : "))
                            if find_dat_time not in (1,2,3,4):
                                print('Plsease select the valid option')
                                continue
                            if find_dat_time == 1:
                                details.Find_current_year()
                                time.sleep(0.5)
                            elif find_dat_time == 2:
                                details.Find_current_month()
                                time.sleep(0.5)
                            elif find_dat_time == 3:
                                details.Find_current_day()
                                time.sleep(0.5)
                            elif find_dat_time == 4:
                                break
                    elif add_option == 4:#7 : Find salary greaterthan 50000 for Employee
                        #  Enter 8 : Find salary between 50000 - 100000 for Employee \n Enter 10 : Sort Employer list with Salary in descending Order \n
                        while True:
                            time.sleep(0.5)
                            print(" ************************************************* ")
                            find_salary=int(input("\n Enter 1 : Find slary ggraterthan 50000 \n Enter 2 : Find salary between 50000 - 100000 for Employee \n Enter 3 : Find salary lessthan 50000 and greater than 100000 \n Enter 4 : Sort Employer list with Salary in descending Order \n Enter 5 : Exit \n Enter your Choice : "))
                            if find_salary not in (1,2,3,4,5):
                                print('Plsease select the valid option')
                                continue
                            if find_salary == 1:
                                details.Find_salary_geraterthan()
                                time.sleep(0.5)
                            elif find_salary == 2:
                                details.Find_between_50000_100000()
                                time.sleep(0.5)
                            elif find_salary == 3:
                                details.Find_less_50000_and_gerater_100000()
                                time.sleep(0.5)
                            elif find_salary == 4:
                                details.Find_sort_salary()
                                time.sleep(5)
                            elif find_salary == 5:
                                break
                    elif add_option == 5:#exit
                        break
                except Exception as e:
                    print(" ",e)
        elif select == 2:
            break
main()