import forca
import adivinhacao
import jogo_da_velha

print("**************************")
print("***ESCOLHA O SEU JOGO***")
print("**************************")

print("Qual jogo você que jogar?")
jogo = int(input("(1)Forca (2)Adivinhação (3)Jogo da Velha\n"))

if jogo == 1:
    forca.jogar()
elif jogo == 2:
    adivinhacao.jogar()
elif jogo == 3:
    jogo_da_velha.jogar()

 