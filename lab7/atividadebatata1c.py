#certo
maior = float('-inf')
batata = 1
while batata <= 10: 
    num = int(input("Digite um número: "))
    if num > maior:
       maior = num
    batata +=1
print('O maior número é', maior)

#errado
# maior = float('inf') tem que ser negativo
# while soma <= 10: variável errada 
#     num = int(input("Digite um número: "))
#     if num > maior:
#        maior = num
#falta aumentar 1 no contador
# print('O maior número é', maior)
