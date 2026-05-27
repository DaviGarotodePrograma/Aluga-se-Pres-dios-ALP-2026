cont = 5
while cont > 0: 
    num = int(input("Digite um número inteiro: "))
    cont -= 1
    
    # Se for PAR: o 'continue' pula o resto do código e volta para o início do loop.
    if num % 2 == 0: 
        continue
        
    # Se for ÍMPAR: o 'if' é ignorado e esta linha é executada.
    print(f'{num} é um número ímpar')