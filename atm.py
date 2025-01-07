from models import Account, BankDatabase

class Transaction:
    def __init__(self, account):
        self._account = account

    def execute(self):
        raise NotImplementedError


class BalanceInquiry(Transaction):
    def execute(self):
        return f"Saldo atual: R$ {self._account.get_balance():.2f}"


class Withdrawal(Transaction):
    def __init__(self, account, amount):
        super().__init__(account)
        self.__amount = amount

    def execute(self):
        if self._account.withdraw(self.__amount):
            return "Saque realizado com sucesso."
        return "Saldo insuficiente."


class Deposit(Transaction):
    def __init__(self, account, amount):
        super().__init__(account)
        self.__amount = amount

    def execute(self):
        self._account.deposit(self.__amount)
        return "Depósito realizado com sucesso."


class ATM:
    def __init__(self, bank_database):
        self.__bank_database = bank_database
        self.__current_account = None

    def authenticate_user(self):
        account_number = int(input("Digite o número da conta: "))
        pin = int(input("Digite o PIN: "))
        account = self.__bank_database.find_account(account_number, pin)
        if account:
            self.__current_account = account
            print("Autenticação bem-sucedida!")
            return True
        else:
            print("Autenticação falhou. Número da conta ou PIN incorretos.")
            return False

    def perform_transaction(self, transaction):
        return transaction.execute()

    def create_account(self):
        # Criar nova conta
        print("\nCriar Nova Conta:")
        account_number = int(input("Digite o número da nova conta: "))
        pin = int(input("Digite o PIN: "))
        balance = float(input("Digite o saldo inicial: "))

        # Criar a conta e adicioná-la ao banco de dados
        new_account = Account(account_number, pin, balance)
        self.__bank_database.add_account(new_account)
        print(f"Conta criada com sucesso! Número da conta: {account_number}")

    def main_menu(self):
        while True:
            print("\nMenu Principal:")
            print("1. Fazer Login")
            print("2. Criar Nova Conta")
            print("3. Sair")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                if self.authenticate_user():
                    self.logged_in_menu()
            elif choice == '2':
                self.create_account()
            elif choice == '3':
                print("Saindo... Obrigado por usar o ATM!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def logged_in_menu(self):
        while True:
            print("\nMenu do Cliente:")
            print("1. Consultar Saldo")
            print("2. Realizar Saque")
            print("3. Realizar Depósito")
            print("4. Sair")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                transaction = BalanceInquiry(self.__current_account)
                print(self.perform_transaction(transaction))
            elif choice == '2':
                amount = float(input("Digite o valor do saque: "))
                transaction = Withdrawal(self.__current_account, amount)
                print(self.perform_transaction(transaction))
            elif choice == '3':
                amount = float(input("Digite o valor do depósito: "))
                transaction = Deposit(self.__current_account, amount)
                print(self.perform_transaction(transaction))
            elif choice == '4':
                print("Saindo da conta...")
                self.__current_account = None
                break
            else:
                print("Opção inválida. Tente novamente.")


# Função principal para execução
def main():
    bank_db = BankDatabase()

    # Carregar ou criar novo banco de dados
    try:
        bank_db.load_from_file("bank_data.pkl")
        print("Banco de dados carregado com sucesso.")
    except FileNotFoundError:
        print("Nenhum banco de dados encontrado. Certifique-se de criar o banco de dados inicial.")

    atm = ATM(bank_db)

    print("Bem-vindo ao ATM!")
    atm.main_menu()

    # Salvar dados ao sair
    bank_db.save_to_file("bank_data.pkl")
    print("Banco de dados salvo com sucesso.")


if __name__ == "__main__":
    main()