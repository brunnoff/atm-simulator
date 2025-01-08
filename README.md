# atm-simulator
 **Simulador de ATM (Caixa Eletrônico) em Python utilizando princípios de Orientação a Objetos.**

**Visão Geral**  
Este projeto é uma simulação de um sistema de caixa eletrônico (ATM) que permite aos usuários realizar operações bancárias, como consultar saldo, realizar saques e depósitos, bem como criar novas contas. O sistema foi desenvolvido em Python utilizando princípios de orientação a objetos, como encapsulamento, herança e polimorfismo.

**Estrutura do Projeto**  
O projeto é dividido em três arquivos principais:  
**_models.py:_** Define as classes fundamentais do sistema, como Account, BankDatabase e Transaction, bem como subclasses para tipos específicos de transações.  
**_data_base.py:_** Responsável pela inicialização do banco de dados com contas de exemplo e pela persistência dos dados em arquivo.  
**_atm.py:_** Contém a lógica principal do funcionamento do ATM, incluindo autenticação de usuário e execução de transações.  

**Funcionamento do Sistema**  
**1. Banco de Dados**  
O banco de dados é inicializado no arquivo data_base.py. Ele armazena as contas bancárias em um dicionário onde a chave é o número da conta e o valor é um objeto Account. Os dados são salvos em um arquivo binário usando a biblioteca pickle para garantir persistência.

**2. Classes e Conceitos**  
**a) Account (Conta)**  
Representa uma conta bancária com os seguintes atributos:  
**_account_number:_** Número da conta.  
**_pin:_** PIN de acesso.  
**_balance:_** Saldo disponível.  

**Métodos principais:**  
**_check_pin(pin):_** Verifica se o PIN fornecido está correto.  
**_get_balance():_** Retorna o saldo atual da conta.  
**_deposit(amount):_** Adiciona fundos à conta.  
**_withdraw(amount):_** Deduz fundos da conta, se houver saldo suficiente.  

**b) BankDatabase (Banco de Dados)**  
Gerencia as contas bancárias e oferece métodos para adicionar, encontrar e persistir contas.

**c) Transaction (Transação)**  
Classe abstrata que serve como base para transações específicas:  
**BalanceInquiry:** Consulta de saldo.  
**Withdrawal:** Saque.  
**Deposit:** Depósito.  

Todas as transações implementam o método _execute()_.

**d) ATM**  
Gerencia a interação com o usuário e as transações. 

Possui as seguintes funcionalidades:  
Autenticar usuário com account_number e pin.  
Exibir menus para consulta de saldo, saques e depósitos.  
Criar novas contas.

**3. Fluxo do Programa**  
O sistema carrega o banco de dados do arquivo _bank_data.pkl_ (ou cria um novo, se o arquivo não existir).  
O usuário insere seu número de conta e PIN para autenticação.  
Após autenticação bem-sucedida, o menu principal é exibido:  
**Consultar Saldo:** Mostra o saldo atual da conta.  
**Realizar Saque:** Permite a retirada de fundos.  
**Realizar Depósito:** Permite o depósito de fundos.  
**Criar Conta:** Opcionalmente, é possível adicionar novas contas diretamente.  
O programa salva o estado atualizado do banco de dados ao sair.

**4. Criação de Novas Contas**  
O método _create_account()_ permite adicionar novas contas, solicitando informações como número da conta, PIN e saldo inicial.


**Como Executar o Projeto**  
Inicialize o banco de dados executando _data_base.py_:  
_python data_base.py_

Execute o sistema ATM:  
_python atm.py_

Siga as instruções no terminal para realizar as transações desejadas.
