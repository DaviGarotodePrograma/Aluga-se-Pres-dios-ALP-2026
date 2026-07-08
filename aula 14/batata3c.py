#Crie a função classificar_nota() que recebe como parâmetro um valor inteiro 
# referente a uma nota e imprime a string "aprovado" se a nota for maior que 60 ou reprovado caso contrário.
def classificar_nota(batata):
    if  batata >= 60:
        print("Você passou!")
    else:
        print("Você é burro e reprovou")
batata = int(input("Digite a sua nota"))
classificar_nota(batata)