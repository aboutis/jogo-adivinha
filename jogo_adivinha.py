import random
logo = """
            _ _       _       _                                                         
           | (_)     (_)     | |                                                        
   __ _  __| |___   ___ _ __ | |__   ___    ___    _ __  _   _ _ __ ___   ___ _ __ ___  
  / _` |/ _` | \ \ / / | '_ \| '_ \ / _ \  / _ \  | '_ \| | | | '_ ` _ \ / _ \ '__/ _ \ 
 | (_| | (_| | |\ V /| | | | | | | |  __/ | (_) | | | | | |_| | | | | | |  __/ | | (_) |
  \__,_|\__,_|_| \_/ |_|_| |_|_| |_|\___|  \___/  |_| |_|\__,_|_| |_| |_|\___|_|  \___/ 
                                                                                        
                                                                                        
"""
print(logo)
print("Bem vindo(a) ao adivinhe o número!")
print("Estou pensando em um número entre 1 e 100.")

def nivel_facil():
    for i in range(10, 0, -1):
        print(f"Você tem {i} tentantivas.")
        escolha = int(input("Escolha seu número: "))
        if escolha > numero:
            print("Errado! O número escolhido é menor.")
        elif escolha < numero:
            print("Errado! O número escolhido é maior.")
        elif escolha == numero:
            print("Parabens! Você acertou.")
            return 0
    print("Acabaram suas chances! Você perdeu.")

def nivel_dificil():
    for i in range(5, 0, -1):
        print(f"Você tem {i} tentantivas.")
        escolha = int(input("Escolha seu número: "))
        if escolha > numero:
            print("Errado! O número escolhido é menor.")
        elif escolha < numero:
            print("Errado! O número escolhido é maior.")
        elif escolha == numero:
            print("Parabens! Você acertou.")
            return 0
    print("Acabaram suas chances! Você perdeu.")
    print(f"O número escolhido era {numero}")


numero = random.randint(1, 100)

escolha_nivel = True
while escolha_nivel:
    nivel = input("Escolha um nível (facil/dificil): ").lower().strip()
    if nivel == "facil":
        nivel_facil()
        escolha_nivel = False
    elif nivel == "dificil":
        nivel_dificil()
        escolha_nivel = False
    else:
        print("Inválido. Tente novamente.")
