while True:
    valor = int(input("Qual valor deseja sacar? R$ "))
    
    # Validação de valores impossíveis para notas de 20, 50 e 100
    if valor <= 0 or valor == 10 or valor == 30 or valor % 10 != 0:
        print("Valor indisponível para os tipos de cédulas deste caixa (R$20, R$50, R$100). Tente outro valor.")
        continue
    else:
        print("Retirando cédulas... 💵")
        print("Saque realizado com sucesso!")
        break