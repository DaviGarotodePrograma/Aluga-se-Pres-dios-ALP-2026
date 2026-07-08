#Crie uma função exibir_elogio() que recebe como parâmetro um nome e 
# imprime um elogio direcionado à pessoa indicada. Exemplo exibirElogio("Gabi") deve imprimir "Gabi é top". 
def exibir_elogios(nome, elogio):
    print(nome, elogio)
nome = input("Digite seu nome")
elogio = input("Digite o elogio que se identifica com você")
exibir_elogios(nome, elogio) 