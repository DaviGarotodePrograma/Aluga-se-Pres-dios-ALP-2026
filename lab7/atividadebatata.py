#certo
N = int(input("Quantos números quer digitar?"))
contador = 1
impares = 0

while contador <= N:
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        impares += 1
    contador += 1
print(f"Quantidade de ímpares: {impares}")

#errado
# N = int(input("Quantos números quer digitar?"))
# contador = 1
# impares = 0

# while contador <= N:
#     num = int(input("Digite um número: "))
#     if num % 2 != 0:
#         impares += 1, 
#os números não acabam, então temos que colocar que o contador aumente 1 número toda vez que você escrever um num
# print(f"Quantidade de ímpares: {impares}")
