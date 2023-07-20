import random
def jogar():
   print("***************************************")
   print("***BEM VINDO AO JOGO DE ADIVINHAÇÃO***")
   print("***************************************")
   numero = random.randrange(1,101)
   tentativas = 0
   pontos = 1000
   
   print("Escolha o nivel de dificuldade\n ")
   nivel = int(input("(1) Fácil (2) Médio (3) Difícil\n"))
   
   if nivel == 1:
       tentativas = 20
   elif nivel == 2:
       tentativas = 10
   elif nivel == 3:
       tentativas = 5
   
   for rodada in range(1,tentativas+1):
       print(f"Rodada {rodada} de {tentativas}")
       chute=int(input("Digite um numero:"))
   
       pontos_perdidos = abs(numero - chute)
       if chute < numero:
           print("Seu chute é menor que a resposta")
           pontos = abs(pontos - pontos_perdidos)
   
       elif chute > numero:
           print("Seu chute é maior que a resposta")
           pontos = abs(pontos-pontos_perdidos)
   
       else:
           print("Você Acertou!")
           print(f"Você fez {pontos} pontos")
           break   
   if chute != numero:
       print(f"A resposta era {numero}")
if __name__=="__main__":
 jogar()
 