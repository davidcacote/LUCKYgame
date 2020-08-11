import time
import random

print("##################")
print ("###  WELCOME  ###")
print ("  GUESS GAME  ")
print ("##################")
print("Guess a number 0 to 100 That i'm thiking. Lets see if you have lucky.")

numero_sorteado = random.randint(0, 100)
tentativas = 5
nome = input("Before, whats is your name: ")
numero_jogador = int(input("What number i'm thinking? "))
print("Let's compare your answer with my number. Looking...")
time.sleep(2)

while tentativas >= 1:
    tentativas = tentativas - 1
    if numero_jogador <= 100:
        if numero_jogador == numero_sorteado:
            print("""####  JACKPOT  #### CONGRATS""")
            time.sleep(1)
            break
        elif numero_jogador < numero_sorteado:
            print(nome + " you mention a number below mine")
            print("You have more " + str(tentativas) + " tries")
            numero_jogador = int(input("What number i'm thinking? "))
        elif numero_jogador > numero_sorteado:
            print(nome + " you mention a number above mine")
            print("You have more " + str(tentativas) + " tries")
            numero_jogador = int(input("What number i'm thinking? "))

    else:
        print("You have more " + str(tentativas) + " tries")
        print(nome + " you gave wrong number. The number must be between 0 and 100")
        numero_jogador = int(input("What number i'm thinking? "))
        time.sleep(2)

print("##################")
print ("### GAME OVER ###")
print ("##################")
print('This thing is belong to test branch')
