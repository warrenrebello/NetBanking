from os import system
from accountfile import AccountFile
from account_connection import AccountDatabase
from loan import Features
import sys

class ClientDisplay(AccountFile):
    def __init__(self):
        #self.acc_file = AccountFile()
        self.loan = Features()
        self.acc_db = AccountDatabase('root', '', 'localhost', 'banking')
    
    # Function for default header
    def defaultDisplay(self):
        system('clear')
        print("\t\t\t\tWBR Banking")
        print("\t\t\t\t-----------\n\n")
        print("\t\t\t       Client Display")
        print("\t\t\t       --------------\n")
    
    def clientView(self, id):
        self.defaultDisplay()
        print("Select an option :\n")
        print("\t1. View Account Details") # Working
        print("\t2. View Balance") # Working
        print("\t3. View Loans") # Working
        print("\t4. Transfer Amount")
        print("\t5. Change PIN")
        print("\n\t0. Log Out\n") # Working

        option = input("Option : ")
        if option == '1':
            self.clientDetails(id)
        elif option == '2':
            self.clientBalance(id)
        elif option == '3':
            self.clientLoan(id)
        elif option == '4':
            self.clientTransferOptions(id)
        elif option == '5':
            pass
        elif option == '0':
            sys.exit(0)
        else:
            print("\nWrong Entry!!!")
        input("\nPress 'enter' to continue...")
        self.clientView(id)

    def clientDetails(self, id):
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
        self.clientView(id)
    
    def clientBalance(self, id):
        self.defaultDisplay()
        client_info = self.acc_db.showDetails(id)
        print("Balance Details")
        print("---------------\n")
        print("{} has a total balance of INR {}." .format(client_info[1], client_info[4]))
        print("Below is the account breakdown.\n")
        print("Savings Account : {}" .format(client_info[5]))
        print("Salary Account : {}" .format(client_info[6]))
        input("\n\nPress 'enter' to continue...")
        self.clientView(id)
    
    def clientLoan(self, id):
        self.defaultDisplay()
        client_info = self.acc_db.showDetails(id)
        if client_info[7] != 0:
            print("{} has taken a loan of INR {}.\n" .format(
                client_info[1], client_info[7]))
            print("The loan duration is {} years with an Annual Interest of {}%.\n" .format(
                client_info[8], client_info[9]))
            print("EMI for this loan is INR {}.\n" .format(client_info[10]))
        else:
            print("{} does not have any loans.\n" .format(client_info[1]))
        # input("\n\nPress 'enter' to continue...")
        # self.clientView(id)

    def clientTransferOptions(self, id):
        self.defaultDisplay()
        print("Select an option :\n")
        print("\t1. Transfer within account")
        print("\t2. Transfer to another account")
        print("\n\t0. Go Back\n")

        option = input("Option : ")

        if option == '1':
            self.defaultDisplay()
            print("Select an option :\n")
            print("\t1. From Salary to Savings")
            print("\t2. From Savings to Salary")
            print("\n\t0. Back to Main Page\n")

            decide = input("Option : ")

            if decide == '1':
                self.clientTransferOptions(id, 'self', 'salary')
            elif decide == '2':
                self.clientTransferOptions(id, 'self', 'savings')
            elif decide == '0':
                self.clientView(id)
            else:
                print("\nWrong Entry!!!")


        elif option == '2':
            self.defaultDisplay()
        elif option == '0':
            self.clientView(id)
        else:
            print("\nWrong Entry!!!")
        input("\nPress 'enter' to continue...")
        self.clientTransferOptions(id)
        pass

    def clientTransfer(self, id, receiver, account):
        self.defaultDisplay()
        client_info = self.acc_db.showDetails(id)
        if receiver == 'self':
            if account == 'salary':
                pass
            else:
                pass
            pass
        else:
            pass
