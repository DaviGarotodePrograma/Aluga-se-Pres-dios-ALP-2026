import random
secreto = random.randint(1, 10)
chances = 5

while chances > 0:
    palpite = int(input("Adivinhe o número (1 a 10): "))
    
    # Se o número estiver fora do intervalo, ignora a tentativa
    if palpite < 1 or palpite > 10:
        print("Número inválido! Digite um valor entre 1 e 10.")
        continue
        
    # Se chegou aqui, o palpite é válido, então gasta uma chance
    chances -= 1
    
    if palpite == secreto:
        print("Parabéns! Você acertou! 🎉")
        break
    else:
        if chances > 0:
            print(f"Errado! Você ainda tem {chances} chances.")
        else:
            print(f"Suas chances acabaram! O número era {secreto}. 😢")