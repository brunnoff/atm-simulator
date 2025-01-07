import pickle

class Account:
    def __init__(self, account_number, pin, balance=0):
        self.__account_number = account_number
        self.__pin = pin
        self.__balance = balance

    def check_pin(self, pin):
        return self.__pin == pin

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        return False


class BankDatabase:
    def __init__(self):
        self.__accounts = {}

    def add_account(self, account):
        self.__accounts[account._Account__account_number] = account

    def find_account(self, account_number, pin):
        account = self.__accounts.get(account_number)
        if account and account.check_pin(pin):
            return account
        return None

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.__accounts, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.__accounts = pickle.load(file)
        except FileNotFoundError:
            print("Arquivo de dados não encontrado. Criando novo banco de dados.")