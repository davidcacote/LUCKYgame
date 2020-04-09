import time
import random

print("##################")
print ("###  WELCOME  ###")
print ("  GUESS GAME  ")
print ("##################")
print("Guess a number 0 to 100 That im thiking. Lets see if you have lucky.")

numero_sorteado = random.randint(0,100)
tentativas = 5
nome = input("Antes diz-nos como te chamas: ")
numero_jogador = int(input("Que número estou a pensar? "))
print("Vamos comparar a tua resposta com o número sorteado. A pensar...")
time.sleep(2)

while tentativas >= 1:
    tentativas = tentativas - 1
    if numero_jogador <= 100:
        if numero_jogador == numero_sorteado:
            print("""####  JACKPOT  ####
ACERTASTE EM CHEIO""")
            time.sleep(1)
            break
        elif numero_jogador < numero_sorteado:
            print(nome + " referiste um número abaixo do sorteado")
            print("Tens mais " + str(tentativas) + " tentativas")
            numero_jogador = int(input("Que número estou a pensar? "))
        elif numero_jogador > numero_sorteado:
            print(nome + " referiste um número acima do sorteado")
            print("Tens mais " + str(tentativas) + " tentativas")
            numero_jogador = int(input("Que número estou a pensar? "))


    else:
        print("Tens mais " + str(tentativas) + " tentativas")
        print(nome + " deste um número incorrecto. Tens de escrever um número entre 0 e 100")
        numero_jogador = int(input("Que número estou a pensar? "))
        time.sleep(2)

print("##################")
print ("### GAME OVER ###")
print ("##################")
