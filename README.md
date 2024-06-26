# DIO | Resumos Git e GitHub

Repositório para armazenar o desafio do módulo Desafio do Projeto Criando um Sistema Bancário com Python >>> [Digital Innovation One](https://www.dio.me/).

## 📚 Objetivo
- Criar um sistema bancário com as operações: sacar, depositar e visualizar o extrato.


## 💻 Resumos do Desafio
- Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso optou pela Linguagem Python. Como requisito inicial do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

### 🤌 Operação de depósito
- O sistema deve ser possível de realizar depósitos de valores positivos na conta corrente do usuário.Nesta primeira versão teremos apenas um usuário, dessa forma não será necessário identificar o número da conta e agência bancária. Todos os depósitos deverão ser armazenados em uma variável e exibidos na operação extrato.

- Por exemplo, na opção de depósito o sistema tem que perguntar ao usuário qual o valor que ele deseja depositar. Esse valor tem que ser um valor inteiro e positivo, ou seja, não podemos depositar “R$ - 100,00”. O sistema não poderá permitir que o usuário informe um valor negativo. 

- Estas operações de depósito deverão ficar armazenadas para que, nas operações de extrato elas estejam acessíveis. Se foram feitos 10 depósitos, estes 10 depósitos devem constar no extrato.

## 💰Operação de saque
- Outro requisito do sistema é que serão permitidos apenas 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível efetuar o saque por saldo insuficiente. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

## 📋Operação de extrato
- O extrato deverá listar todos os depósitos e saques realizados na conta. No final da listagem deve ser exibido o saldo atual da conta. Os valores devem ser exibidos utilizando o formato R$ 000.00, ou seja, 1500.45 = R$ 1500.45.

## 🔍Referências
-[Digital Innovation One](https://web.dio.me/track/coding-future-vivo-python-ai-backend-developer)

