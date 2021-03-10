from os import system
from account_connection import AccountDatabase
from accountfile import AccountFile
from loan import Features
import sys
import random
import getpass

class AdminDisplay(AccountFile):
    def __init__(self):
        self.acc_file = AccountFile()
        self.acc_db = AccountDatabase('root', '', 'localhost', 'banking')
        self.loan = Features()
        pass

    # Function for default header
    def defaultDisplay(self):
        system('clear')
        print("\t\t\t\tWBR Banking")
        print("\t\t\t\t-----------\n\n")
        print("\t\t\t       Admin Display")
        print("\t\t\t       -------------\n")

    def adminView(self, id):
        self.defaultDisplay()
        print("Select an option :\n")
        print("\t1. Create Admin Account") # Working
        print("\t2. Create Bank Account") # Working
        print("\t3. Access Bank Account") # Working
        print("\t4. Change PIN")
        print("\t5. Documentation")
        print("\n\t0. Log Out\n") # Working

        option = input("Option : ")

        if option == '1':
            self.adminCreate()
        elif option == '2':
            self.createBank()
        elif option == '3':
            self.accessAccount(id)
        elif option == '4':
            self.changePIN(id)
        elif option == '5':
            pass
        elif option == '0':
            sys.exit(0)
        else:
            print("\nWrong Entry!!!")
            input("\nPress 'enter' to continue...")
        self.adminView(id)
    
    
    def adminCreate(self):
        self.defaultDisplay()

        admin_id = self.acc_file.idGenerator()
        
        print("Create Admin Account\n")
        print("\tNew Admin ID -> {}" .format(admin_id))
        admin_name = input("\n\tEnter Fullname : ")
        admin_pin = input("\tPIN : ")

        admin_name = admin_name.replace(" ", "")
        admin_pin = admin_pin.replace(" ", "")

        if admin_id == "" or admin_name == "" or admin_pin == "":
            print("\n\nNo fields can be left blank")
            input("\nPress 'enter' to continue...")
            self.adminCreate()
        else:
            self.acc_db.createAccount(admin_name, admin_id, admin_pin, 0, 0, 0, 0, 0, 0, 0, 'admin')
            print("\n\nNew Admin Account Created")
            input("\nPress 'enter' to continue...")
    
    def createBank(self):
        self.defaultDisplay()
        
        new_id = self.idGenerator()

        print("Create Client Account\n")
        print("\nNew Client ID -> {}" .format(new_id))
        
        new_name = input("Account Holder : ")
        new_pin = int(input("PIN : "))
        new_savings = float(input("Savings : "))
        new_salary = float(input("Salary : "))
        new_balance = new_savings + new_salary

        self.acc_db.createAccount(new_name, new_id, new_pin, new_balance, new_savings, new_salary, 0, 0, 0, 0, 'client')
        print("\n\nNew Bank Account Created")
        input("\nPress 'enter' to continue...")

    def accessAccount(self, id):
        self.defaultDisplay()
        account_id = input("Enter Account ID : ")
        try:
            self.acc_db.get_account(account_id)
            self.accessDisplay(id, account_id)
        except:
            print("\n\nAccount Does Not Exist")
            input("\nPress 'enter' to continue...")
            self.adminView(id)
    
    def accessDisplay(self, id, account_id):
        self.defaultDisplay()
        print("Select an option :\n")
        print("\t1. View Account Details") # Working
        print("\t2. Loan Application") # Working
        print("\t3. Change PIN")
        print("\t4. Delete Account")
        print("\t0. Return Back\n") # Working

        option = input("Option : ")
        if option == '1':
            self.accountDetails(account_id)
            self.accessDisplay(id, account_id)
        elif option == '2':
            self.defaultDisplay()
            self.loan.loanApply(id, account_id)
            self.accessDisplay(id, account_id)
        elif option == '3':
            #self.accountDetails(account_id)
            self.accessDisplay(id, account_id)
        elif option == '4':
            self.accessDisplay(id, account_id)
        elif option == '0':
            pass
        else:
            print("\nWrong Entry!!!")
            input("\nPress 'enter' to continue...")
            self.accessDisplay(id, account_id)

    def accountDetails(self, id):
        self.defaultDisplay()
        client_info = self.acc_db.showDetails(id)
        print("Account Holder       :", client_info[1],
              "\nAccount Number       :", client_info[2],
              "\nPIN                  :", client_info[3],
              "\nBalance              :", client_info[4],
              "\nSavings              :", client_info[5],
              "\nSalary               :", client_info[6],
              "\nLoan Amount          :", client_info[7],
              "\nLoan Duration        :", client_info[8],
              "\nAnnual Interest Rate :", client_info[9],
              "\nEMI                  :", client_info[10])
        input("\n\nPress 'enter' to continue...")
        # self.adminView(id)

    def changePIN(self, id):
        self.defaultDisplay()
        account_details = self.getFile(id)
        user_id = input("\t\t\t    Enter your ID : ")
        if user_id == id:
            user_pin = getpass.getpass(prompt="\t\t\t    Enter OLD PIN : ")
            if account_details["PIN"] == user_pin:
                # self.defaultDisplay()
                print()
                new_pin = getpass.getpass(prompt="\t\t\t    Enter NEW PIN : ")
                account_details["PIN"] = new_pin
                self.updateFile(user_id, account_details)
                print("\n\nPIN has been updated.")
                input("\nPress 'enter' to continue...")
                self.adminView(id)
            else:
                print("\n\nYour PIN is incorrect")
                input("\nPress 'enter' to continue...")
                self.adminView(id)
        else:
            print("\n\nYour ID is incorrect.")
            input("\nPress 'enter' to continue...")
            self.adminView(id)
