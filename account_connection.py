import pymysql
import random


class AccountDatabase():
    def __init__(self, user, password, host, db):
        self.user = user
        self.password = password
        self.host = host
        self.db = db

    def idGenerator(self):
        new_id = random.randint(10000, 100000)
        try:
            self.get_account(new_id)
            return new_id
        except:
            self.idGenerator()

    def open_connection(self):
        connection = pymysql.connect(host=self.host,
                                     user=self.user,
                                     passwd=self.password,
                                     db=self.db)
        cursor = connection.cursor()
        return connection, cursor

    def get_account(self, acc_id):
        try:
            connection, cursor = self.open_connection()
            query = "select * from accounts where account_number = %s"
            values = acc_id
            cursor.execute(query, values)
            data = cursor.fetchall()
            if not len(data) == 0:
                return data[0]
            else:
                return 0
        except pymysql.OperationalError as e:
            print(e)
        except pymysql.InternalError as e:
            print(e)
        except pymysql.ProgrammingError as e:
            print(e)
        finally:
            try:
                connection.close()
            except:
                pass

    def createAccount(self, acc_hol, acc_num, pin, bal, sav, sal, lam, ldu, air, emi, acc_type):
        try:
            connection, cursor = self.open_connection()
            query = "insert into accounts (account_holder, account_number, pin, balance, savings, salary, loan_amount, loan_duration, annual_interest_rate, EMI, account_type) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (acc_hol, acc_num, pin, bal, sav, sal, lam, ldu, air, emi, acc_type)
            cursor.execute(query, values)
            connection.commit()
        except:
            pass
        finally:
            try:
                connection.close()
            except:
                pass

    def updateAccount(self, acc_num, lam, ldu, air, emi):
        try:
            connection, cursor = self.open_connection()
            query = "update accounts set loan_amount = %s, loan_duration = %s, annual_interest_rate = %s, EMI = %s where account_number = %s"
            values = (lam, ldu, air, emi, acc_num)
            cursor.execute(query, values)
            connection.commit()
        except:
            pass
        finally:
            try:
                connection.close()
            except:
                pass

    def showDetails(self, acc_id):
        acc_details = self.get_account(acc_id)
        return acc_details


'''
    def locateAccount(self, id):
        try:
            connection, cursor = self.open_connection()
            return True
        except:
            return False


    def idGenerator(self):
        new_id = random.randint(10000, 100000)
        if not self.locateAccount(new_id):
            return str(new_id)
        else:
            self.idGenerator()
'''