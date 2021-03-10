from display import Display
from accountfile import AccountFile
from admindisplay import AdminDisplay
from clientdisplay import ClientDisplay
import getpass
import time

class Login():
    def __init__(self):
        self.dis = Display()
        self.acc_file = AccountFile()
        self.admin = AdminDisplay()
        self.client = ClientDisplay()
    
    def userLogin(self):
        self.dis.defaultDisplay()
        print("\t\t    Welcome to WBR Online Banking System")
        print("\t\t    ------------------------------------\n")
        user_id = input("\t\t\t    Enter ID  : ")
        user_pin = getpass.getpass(prompt="\t\t\t    Enter PIN : ")
        try:
            check_type = self.acc_file.getFile(user_id)
            if check_type["PIN"] == user_pin:
                if check_type["Type"] == "Admin":
                    del check_type
                    self.admin.adminView(user_id)
                else:
                    pass
            else:
                print("\t\t\tWrong PIN")
                time.sleep(1)
                self.userLogin()
        except:
            print("\t\t\tAccount does not exist")
            time.sleep(1)
            self.userLogin()

        