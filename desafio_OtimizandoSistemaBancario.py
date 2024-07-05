import textwrap


def menu():
    menu = """\n
    ─────────────── M E N U ───────────────
    \t[1]\t[ Depositar ]
    \t[2]\t[ Sacar ]
    \t[3]\t[ Extrato ]
    \t[4]\t[ Nova Conta ]
    \t[5]\t[ Listar Contas ]
    \t[6]\t[ Novo Cliente ]
    \t[0]\t[ Sair ]
    ───────────────────────────────────────
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0 :
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
    else:
        print("\n@@@ Operação Falou!!! O valor informado é inválido. @@@")
    
    return saldo, extrato
       


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("\n@@@ Operação Falhou!!! Você não tem saldo suficiente. @@@")
        
    elif excedeu_limite:
        print("\n@@@ Operação Falhou!!! O valor do saque excede o limite. @@@")
    
    elif excedeu_saques:
        print("\n@@@ Operação Falhou!!! Número máximo de saques exedido. @@@")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n### Saque realizado com Sucesso! ###")
    
    else:
        print("\n@@@ Operação Falhou!!! O valor informa é inválido. @@@")
        
    return saldo, extrato
    
 
def exibir_extrato(saldo, /, *, extrato):
    print("\n─────────────── E X T R A T O ───────────────") 
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("──────────────────────────────────────────────")
 
 
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
     
    if usuario:
        print("\n@@@ Já existe um Cliente com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("### Cliente cadastrado com sucesso!!! ###")
       

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do Cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n### Conta aberta com sucesso! ###")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Cliente não encontrado, fluxo de abertura de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C.:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("\n─────────────── LISTA DE CONTAS ───────────────")
        #print("─" * 41)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
    
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar (
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
         
        elif opcao == "6":
            criar_usuario(usuarios)
       
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
           
            if conta:
                contas.append(conta)
       
        elif opcao == "5":
            listar_contas(contas) 
       
        elif opcao == "0":
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
            
main()
