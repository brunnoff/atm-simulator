## Simulador de ATM (Caixa Eletrônico) em Python utilizando princípios de Orientação a Objetos

### Visão Geral

Este projeto é uma simulação de um sistema de caixa eletrônico (ATM) que permite aos usuários realizar operações bancárias, como consultar saldo, realizar saques e depósitos, bem como criar novas contas. O sistema foi desenvolvido em Python utilizando princípios de orientação a objetos, como encapsulamento, herança e polimorfismo.

### Estrutura do Projeto 

O projeto é dividido em três arquivos principais:  
1. **models.py:** Define as classes fundamentais do sistema, como `Account`, `BankDatabase` e `Transaction`, bem como subclasses para tipos específicos de transações.  
2. **data_base.py:** Responsável pela inicialização do banco de dados com contas de exemplo e pela persistência dos dados em arquivo.  
3. **atm.py:** Contém a lógica principal do funcionamento do ATM, incluindo autenticação de usuário e execução de transações.  

### Funcionamento do Sistema  
#### 1. Banco de Dados  
O banco de dados é inicializado no arquivo `data_base.py`. Ele armazena as contas bancárias em um dicionário onde a chave é o número da conta e o valor é um objeto `Account`. Os dados são salvos em um arquivo binário usando a biblioteca `pickle` para garantir persistência.

#### 2. Classes e Conceitos 
**a) Account (Conta)**  
Representa uma conta bancária com os seguintes atributos:  
* **account_number:** Número da conta.  
* **pin:** PIN de acesso.  
* **balance:** Saldo disponível.  

Métodos principais:  
* `check_pin(pin)`: Verifica se o PIN fornecido está correto.  
* `get_balance()`: Retorna o saldo atual da conta.  
* `deposit(amount)`: Adiciona fundos à conta.  
* `withdraw(amount)`: Deduz fundos da conta, se houver saldo suficiente.  

**b) BankDatabase (Banco de Dados)**  
Gerencia as contas bancárias e oferece métodos para adicionar, encontrar e persistir contas.

**c) Transaction (Transação)**  
Classe abstrata que serve como base para transações específicas:  
* `BalanceInquiry`: Consulta de saldo.  
* `Withdrawal`: Saque.  
* `Deposit`: Depósito.  

Todas as transações implementam o método `execute()`.

**d) ATM**  
Gerencia a interação com o usuário e as transações. 

Possui as seguintes funcionalidades:  
* Autenticar usuário com `account_number` e `pin`.  
* Exibir menus para consulta de saldo, saques e depósitos.  
* Criar novas contas.

**3. Fluxo do Programa**  
1. O sistema carrega o banco de dados do arquivo `bank_data.pkl` (ou cria um novo, se o arquivo não existir).  
2. O usuário insere seu número de conta e PIN para autenticação.  
3. Após autenticação bem-sucedida, o menu principal é exibido:
   * **Consultar Saldo:** Mostra o saldo atual da conta.
   * **Realizar Saque:** Permite a retirada de fundos.
   * **Realizar Depósito:** Permite o depósito de fundos.
   * **Criar Conta:** Opcionalmente, é possível adicionar novas contas diretamente.  
4. O programa salva o estado atualizado do banco de dados ao sair.

**4. Criação de Novas Contas**  
O método `create_account()` permite adicionar novas contas, solicitando informações como número da conta, PIN e saldo inicial.


### Como Executar o Projeto  
1. Inicialize o banco de dados executando `data_base.py`:  
   `python data_base.py`

2. Execute o sistema ATM:  
   `python atm.py`

3. Siga as instruções no terminal para realizar as transações desejadas.
