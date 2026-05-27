total_conta = 0.0

while True:
    print("\n=== Cardápio ===")
    print("1. Açaí 300ml - R$ 12,00")
    print("2. Mousse - R$ 6,50")
    print("3. Salada de frutas - R$ 10,00")
    print("4. Fechar a conta")
    
    opcao = int(input("Escolha uma opção (1 a 4): "))
    
    if opcao == 1:
        total_conta += 12.00
        print("Açaí adicionado!")
    elif opcao == 2:
        total_conta += 6.50
        print("Mousse adicionado!")
    elif opcao == 3:
        total_conta += 10.00
        print("Salada de frutas adicionada!")
    elif opcao == 4:
        print(f"\nConta fechada! Total a pagar: R$ {total_conta:.2f}")
        break
    else:
        print("Opção inválida! Tente novamente.")
        continue