#Crie uma função chamada ola() que recebe como parâmetro o nome de uma pessoa e uma das opções de gênero (feminino, masculino ou neutro) 
#e retorna uma mensagem de boas-vindas ajustada de acordo com o gênero. 
#Exemplos: 
#ola("Leo", "neutro") deve retornar "Olá Leo, boas vindas!"
#ola("Mila", "feminino") deve retornar "Olá Mila, bem vinda!"
#ola("Alan", "masculino") deve retornar "Olá Alan, bem vindo!"
def ola(nome, genero):
    if genero == "feminino":
        return f"Olá {nome}, bem vinda!"
    elif genero == "masculino":
        return f"Olá {nome}, bem vindo!"
    elif genero == "neutro":
        return f"Olá {nome}, boas vindas!"
    else: 
        return "Gênero inválido"

nome = input("Digite seu nome: ")
genero = input("Digite seu gênero com qual se identifica! ")
print(ola(nome, genero))