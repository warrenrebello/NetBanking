import pickle
import random

class AccountFile():
    def __init__(self):
        pass
    
    def idGenerator(self):
        new_id = random.randint(10000,100000)
        if not self.locateAccount(new_id):
            return str(new_id)
        else:
            self.idGenerator()
    
    def locateAccount(self, id):
        try:
            open(id + ".txt", "rb")
            return True
        except:
            return False

    def getFile(self, id):
        get_file_info = open(id + ".txt", "rb")
        file_details = pickle.load(get_file_info)
        get_file_info.close()
        return file_details

    def writeFile(self, id, admin_details):
        if self.locateAccount(id):
            print("\n\nAccount with ID '{}' already exists." .format(id))
            print("Going back to Main Page.\n")
            input("\nPress 'enter' to continue...")
        else:
            get_file_details = open(id + ".txt", "wb")
            pickle.dump(admin_details, get_file_details)
            get_file_details.close()
            
    
    def updateFile(self, id, file_details):
        if self.locateAccount(id):
            get_file_details = open(id + ".txt", "wb")
            pickle.dump(file_details, get_file_details)
            get_file_details.close()
        else:
            pass

    def showDetails(self, id):
        if self.locateAccount(id):
            print()
            user_details = self.getFile(id)
            user_details["PIN"] = "****"
            for each in user_details.items():
                print("{:<15} : {}".format(each[0], each[1]))
        else:
            print("\n\nAccount Does Not Exist")
        input("\nPress 'enter' to continue...")
    
    def showBalance(self, id):
        if self.locateAccount(id):
            print()
            user_details = self.getFile(id)
            print("Balance Details")
            print("---------------\n")
            print("{} has a total balance of INR {}." .format(user_details["Account Holder"], user_details["Account Balance"]))
            print("Below is the account breakdown.\n")
            print("Savings Account : {}" .format(user_details["Savings"]))
            print("Salary Account : {}" .format(user_details["Salary"]))
        else:
            pass
