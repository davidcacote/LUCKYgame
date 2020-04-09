import time
import random

print("##################")
print ("###  BemVindo  ###")
print (" Jogo do adivinha ")
print ("##################")
print("Adivinha o número de 1 a 100 que estou a pensar. Veremos se acertas.")

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