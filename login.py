from display import Display
from accountfile import AccountFile
from admindisplay import AdminDisplay
from clientdisplay import ClientDisplay
from account_connection import AccountDatabase
import getpass
import time

class Login():
    def __init__(self):
        self.dis = Display()
        self.acc_file = AccountFile()
        self.admin = AdminDisplay()
        self.client = ClientDisplay()
        self.acc_db = AccountDatabase('root', '', 'localhost', 'banking')

    def userLogin(self):
        self.dis.defaultDisplay()
        print("\t\t    Welcome to WBR Online Banking System")
        print("\t\t    ------------------------------------\n")
        user_id = input("\t\t\t    Enter ID  : ")
        user_pin = getpass.getpass(prompt="\t\t\t    Enter PIN : ")
        if user_id == "":
            print("\n\nID cannot be left blank.")
            input("\nPress 'enter' to continue...")
            self.userLogin()
        details = self.acc_db.get_account(user_id)
        if details == 0:
            print("\n\nAccount Does Not Exist")
            input("\nPress 'enter' to continue...")
            self.userLogin()
        else:
            if str(details[3]) == user_pin:
                if details[11] == 'admin':
                    self.admin.adminView(user_id)
                else:
                    self.client.clientView(user_id)
            else:
                print("Wrong PIN")
                input("\nPress 'enter' to continue...")
                self.userLogin()