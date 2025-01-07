from models import Account, BankDatabase

# Criar banco de dados e adicionar contas de exemplo
bank_database = BankDatabase()

# Adicionar contas (número da conta, PIN, saldo inicial)
bank_database.add_account(Account(1234, 5678, 1000))
bank_database.add_account(Account(5678, 1234, 500))
bank_database.add_account(Account(9999, 8888, 1500))

# Salvar o banco de dados em um arquivo
bank_database.save_to_file("bank_data.pkl")

print("Banco de dados inicial criado e salvo em 'bank_data.pkl'.")