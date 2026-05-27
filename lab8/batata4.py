soma = 0

while True:
    num = int(input("Digite um número inteiro (0 para parar): "))
    
    if num == 0:
        print("Programa encerrado pelo usuário.")
        break
        
    if num < 0:
        print("Número negativo ignorado.")
        continue  # Não soma e volta para o início!!!!
        
    soma += num
    print(f"Soma atual: {soma}")
    
    if soma > 100:
        print("A soma ultrapassou 100!")
        break

print(f"--- FIM --- \nSoma total obtida: {soma}")