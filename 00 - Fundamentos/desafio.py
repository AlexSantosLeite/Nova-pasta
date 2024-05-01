# Função para exibir o menu
def mostrar_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """
    return input(menu).strip().lower()

# Função para depósito
def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor do depósito deve ser positivo.")
    return saldo, extrato

# Função para saque
def sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))
    if valor <= 0:
        print("Operação falhou! O valor do saque deve ser positivo.")
    elif valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite permitido.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques atingido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso!")
    return saldo, extrato, numero_saques

# Função para exibir o extrato
def exibir_extrato(saldo, extrato):
    print("\n======= EXTRATO =======")
    if extrato:
        for item in extrato:
            print(item)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=======================")

# Função principal
def main():
    # Inicializando variáveis
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = mostrar_menu()

        if opcao == 'd':
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == 's':
            saldo, extrato, numero_saques = sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == 'e':
            exibir_extrato(saldo, extrato)

        elif opcao == 'q':
            print("Saindo do sistema. Obrigado por usar nossos serviços!")
            break

        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

# Executar o programa
if __name__ == '__main__':
    main()
