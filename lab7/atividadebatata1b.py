#Certo
soma = 0
qnt_num = 1
while qnt_num <= 10: 
    num = int(input("Digite um número para somar: "))
    soma += num
    qnt_num += 1
print(soma)

#Errado
# soma = 0
#está faltando uma varíavel para conta quantos números foram digitados
# while soma <= 10: a variável descrita está errada pois está falando sobre a soma, não a quantidade de números
#     num = int(input("Digite um número para somar: "))
#     soma += num
#falta aumentar 1 na variável do contador para não ser infinito
#não aparece o print da soma no terminal