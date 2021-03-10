import pickle
from accountfile import AccountFile
from account_connection import AccountDatabase

class Features():
    '''
Features Class
--------------

This class contains functions where you can apply for loan, tranfer
money between accounts, check the overall balance, and check loan details

__init__        - Empty constructor

overBalance     - This function will display only the balance, along
                  with the fund in the Savings and Salary account.

transferBalance - This function will allow you to transfer funds between
                  the Savings account and Salary account.

loanApply       - This functions allows you to enter the loan details for
                  the account. The loan details are passed to loanEMI(),
                  with the calculated EMI returned. The loan details and
                  the EMI are stored back into the Account file.

loanEMI         - The loan details from loanApply() are calculated and
                  returned back to loanApply().

loanDetails     - This funtion will display the details about the loan
    '''

    # Empty constructor
    def __init__(self):
        self.acc_db = AccountDatabase('root', '', 'localhost', 'banking')

    def overallBalance(self, id):
        pass

    # Function to transfer funds between Savings and Salary
    def transferBalance(self, id):
        print("Transfer Between Accounts")
        print("-------------------------\n")

    # Function to enter loan details
    def loanApply(self, id, account_id):
        print("Loan Application")
        print("----------------\n")
        self.loan_amount = float(input("Loan Amount : "))
        self.loan_rate = float(input("Annual Interest Rate : "))
        self.loan_duration = int(input("Loan Duration (years) : "))
        loan_emi = self.loanEMI(self.loan_amount, self.loan_duration, self.loan_rate)

        # get_details = self.acc_db.get_account(account_id)
        
        self.acc_db.updateAccount(account_id, self.loan_amount, self.loan_duration, self.loan_rate, loan_emi)
        print("\n\nLoan Application Complete.")
        input("\nPress 'enter' to continue...")

    # Function to calculate EMI
    def loanEMI(self, amount, years, interest):
        monthly_rate = (self.loan_rate/12)/100
        total_months = self.loan_duration*12
        monthly_emi = (self.loan_amount*monthly_rate*((1+monthly_rate)**total_months) /
                       (((1+monthly_rate)**total_months)-1))
        return round(monthly_emi, 2)
