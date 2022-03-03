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
import datetime,random

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
            for i in self.employee_list:
                print(' List of Employers : {0} \n Name : {1} \n DOB : {2} \n City : {3} \n contact : {4} \n id : {5} \n joining : {6} \n salary : {7} \n department : {8} \n post : {9}'.format(len(self.employee_list),i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
    def Find_employer_name(self,name):
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            for i in self.employee_list:
                if name == i.Name:
                    print('\n Name : {0} \n DOB : {1} \n City : {2} \n contact : {3} \n id : {4} \n ioining : {5} \n salary : {6} \n department : {7} \n post : {8}'.format(i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
                else:
                    print("Not Find!!!!")
                    
    def Find_department(self,department):
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            for i in self.employee_list:
                if department == i.Department:
                    print('\n Name : {0} \n DOB : {1} \n City : {2} \n contact : {3} \n id : {4} \n ioining : {5} \n salary : {6} \n department : {7} \n post : {8}'.format(i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
                else:
                    print("Not Find!!!!")
    def Find_current_year(self):
        CurrentDate=datetime.date.today()  
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            for i in self.employee_list:
                if  i.Joining_date.year==CurrentDate.year:
                    print('\n Name : {0} \n DOB : {1} \n City : {2} \n contact : {3} \n id : {4} \n joining : {5} \n salary : {6} \n department : {7} \n post : {8}'.format(i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
                # else:
                #     print("Not Find!!!!")
    def Find_current_month(self):
        CurrentDate=datetime.date.today()  
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            for i in self.employee_list:
                if  i.Joining_date.month==CurrentDate.month:
                    print('\n Name : {0} \n DOB : {1} \n City : {2} \n contact : {3} \n id : {4} \n joining : {5} \n salary : {6} \n department : {7} \n post : {8}'.format(i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
                # else:
                #     print("Not Find!!!!")
    def Find_salary_geraterthan(self):
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            for i in self.employee_list:
                if i.Salary >= 50000:
                    print('\n Name : {0} \n DOB : {1} \n City : {2} \n contact : {3} \n id : {4} \n ioining : {5} \n salary : {6} \n department : {7} \n post : {8}'.format(i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
                # else:
                #     print("Not Find!!!!")
    def Find_between_50000_100000(self):
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            for i in self.employee_list:
                if i.Salary < 100000 or i.Salary > 50000:
                    print('\n Name : {0} \n DOB : {1} \n City : {2} \n contact : {3} \n id : {4} \n ioining : {5} \n salary : {6} \n department : {7} \n post : {8}'.format(i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
                # else:
                #     print("Not Find!!!!")
    def Find_from_mirzapur(self):
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            pass
    def Find_sort_salary(self):
        if len(self.employee_list) == 0:
            print("Employee Name  not found")
        else:
            self.employee_list.sort(key = lambda x:x.salary, reverse = True)
            for i in self.employee_list:
                print('\n Name : {0} \n DOB : {1} \n City : {2} \n contact : {3} \n id : {4} \n ioining : {5} \n salary : {6} \n department : {7} \n post : {8}'.format(i.Name,i.DOB,i.City,i.Contact_no,i.Emploayer_id,i.Joining_date,i.Salary,i.Department,i.Post))
def main():
    print("************ Welcome ***************")
    details=Manager()
    while True:
        select=int(input("\n Enter 1 : Creat your Company \n Enter 2 : Exit \n Plase Enter : "))
        if select not in (1,2):
            print('Plsease select the valid option')
            continue
        # create  Account in my function
        if select == 1:
            while True:
                print(" ************************************************* ")
                try:
                    add_option=int(input("\n Enter 1 : Create  Account \n Enter 2 : Show All Employee \n Enter 3 : Find name of Employee \n Enter 4 : Find department to Employee \n Enter 5 : Find current year To Employee \n Enter 6 : Find current Month To Employee \n Enter 7 : Find salary greaterthan 50000 for Employee \n Enter 8 : Find salary between 50000 - 100000 for Employee \n Enter 9 : Find Employer from mirzapur \n Enter 10 : Sort Employer list with Salary in descending Order \n Enter 11 : Exit \n Plase Enter : "))
                    if add_option not in (1,2,3,4,5,6,7,8,9,10,11):
                        print('Plsease select the valid option')
                        continue
                    if add_option == 1:    
                        print("************Welcome to  Create your Account  ***************")
                        while True:
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
                                        Joining_date=datetime.date.today() 
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
                        details.Show_all_Employee()
                    elif add_option == 3:#3 : Find name of Employee
                        name=input(" Enter your Name : ")
                        details.Find_employer_name(name)
                    elif add_option == 4:#4 : Find department to Employee
                        department=input(" Enter your department : ")
                        details.Find_department(department)
                    elif add_option == 5:#5 : Find current year To Employee
                        details.Find_current_year()
                    elif add_option == 6:#6 : Find current Month To Employee
                        details.Find_current_month()
                    elif add_option == 7:#7 : Find salary greaterthan 50000 for Employee
                        details.Find_salary_geraterthan()
                    elif add_option == 8:#8 : Find salary between 50000 - 100000 for Employee
                        details.Find_between_50000_100000()
                    elif add_option == 9:#9 : Find Employer from mirzapur
                        details.Find_from_mirzapur()
                    elif add_option == 10:#10 : Sort Employer list with Salary in descending Order
                        details.Find_sort_salary()
                    elif add_option == 11:#exit
                        break
                except Exception as e:
                    print(" ",e)
        elif select == 2:
            break
main()