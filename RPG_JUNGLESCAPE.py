 ## Autores: Leonardo Calisto de Faria Simões / Thiago José Barella / Yuri Barboza
 ## Criado em: 14/04/2020
import time
print("-="*8, "JUNGLE SCAPE", "=-"*8)
print(" ")
print("Autores:")
print("Leonardo Calisto de Faria Simões")
print("Yuri Barboza")
print("Thiago José Barella")
print(" ")
print("Bem vindo ao jogo JUNGLE SCAPE, onde você vai viver na pele de um prisioneiro em cativeiro, e terá suas chances de escapar ou não.")
print("Em dados momentos haverão oportunidades de fuga, movidas por escolhas certas, meio certas, ou erradas. Tudo controlado e interpretado por você, jogador.")
print("As escolhas poderão variar de consequência, tendo em vista a aquisição ou perda de pontos.")
print("Mas lembre-se, haverão momentos críticos onde uma escolha errada poderá causar o fim do jogo.")
print("Jogo não aconselhado para menores de 12 anos.")
print("-="*20)
print("Deseja começar?")
r = input("s/n: ").strip().lower()
if r == "s":
    print("O jogo começou")
    time.sleep(2)
elif r =="n":
    exit("Volte quando estiver preparado.")
else:
    exit("resposta inválida")
pontos = 0
print("Você vai viver o pesadelo de Don Barella, o capitão foi o único sobrevivente de sua embarcação que sofreu naufrágio em uma ilha desconhecida na américa central. Don Barella foi capturado por nativos da ilha e mantido em cativeiro e seu objetivo é fugir e recuperar seus itens para poder se guiar para o Brasil.")
print("Você acordou desnorteado e confuso dentro de uma cela de bambu, e vê em sua frente um homem se aproximando ao lado de fora da cela.")
print("Você deseja:")
print("[1] Fingir que está dormindo")
print("[2] Perguntar onde está")
print("[3] Gritar por ajuda e tentar quebrar a cela")
time.sleep(2)
r = int(input("Escolha:"))
while r > 3 or r < 1:
    r = int(input("Digite uma opção válida:"))
if r == 1:
    print("O homem que estava vindo era um guarda. Acreditou que você e continuou a ronda.")
    print("-=-Você ganhou 10 pontos pela escolha segura.-=-")
    pontos = pontos + 10
elif r == 2:
    print("O homem que estava vindo era um guarda. Você tentou chamar sua atenção mas ele aparentemente não fala sua lingua, ficou irritado, virou as costas e foi embora.")
    print("-=-Você ganhou 5 pontos pela escolha corajosa.-=-")
    pontos = pontos + 5
elif r == 3: 
    print("O homem que estava vindo era um guarda. Ficou extremamente irritado com sua gritaria e jogou uma pedra em sua direção, falando algo em uma lingua desconhecida")
    print("-=-Você não ganhou pontos pela escolha desesperada.-=-")
print("Após algumas horas, você percebe que o guarda caiu no sono.")
print("Você notou algumas falhas naquela cela primitiva e percebe algumas oportunidades de fuga.")
print("Você deseja:")
print("[1] Correr em direção a porta, na tentativa de quebra-la.")
print("[2] Tentar cavar um buraco na parte traseira da cela.")
print("[3] Tentar se espremer entre os bambus na tentativa de sair.")
r = int(input("Escolha:"))
while r > 3 or r < 1:
    r = int(input("Digite uma opção válida:"))
if r == 1:
    print("Você consegue sair da cela, mas o guarda acorda assustado.")
    print("-=-Você ganhou 0 pontos pela escolha imprudente.-=-")
    time.sleep(2)
    print("-=-Você fez uma escolha que levou a uma situação crítica.-=-")
    print("O guarda acordou e você deve enfrentá-lo.")
    time.sleep(2)
    print("Você deseja:")
    print("[1] Correr em direção ao guarda e tentar agarrá-lo e logo em seguida, desmaia-lo.")
    print("[2] Tentar pegar algo do chão para utilizar como arma.")
    print("[3] Tentar despistar o guarda correndo em direção à selva.")
    r = int(input("Escolha:"))
    while r > 3 or r < 1:
        r = int(input("Digite uma opção válida:"))
    time.sleep(2)
    if r == 1:
        print("Você ganhou a luta corporal com o guarda e conseguiu fugir para a floresta à procura da costa.")
        print("-=-Você ganhou 10 pontos pela escolha.-=-")
        pontos = pontos + 10
    elif r == 2:
        print("Antes de conseguir pegar algo, o guarda consegue puxar o arco e te atira uma flecha.")
        exit ("Você morreu, fim do jogo. Sua pontuação foi de {}".format(pontos))
    elif r == 3: 
        print("Você consegue driblar o guarda e fugir em direção à selva em direção da costa.")
        print("-=-Você ganhou 5 pontos.-=-")
        pontos = pontos + 5
elif r == 2:
    print("Você consegue sair da cela,sem o guarda acordar, mas você deixa suas mãos muito feridas.")
    print("-=-Você ganhou 5 pontos pela escolha.-=-")
    pontos = pontos + 5
elif r == 3: 
    print("Você consegue sair da cela contraindo sua barriga sem o guarda acordar.")
    print("-=-Você ganhou 10 pontos pela melhor escolha.-=-")
    pontos = pontos + 10
print("Após fugir, e tomar posse de um facão, você esta indo em direção a praia, quando se depara com uma onça. Ela está indo em sua direção.")
print("Você deseja:")
print("[1] Tentar fugir, mesmo sabendo que a onça é mais rapida.")
print("[2] Usar seu facão para se defender.")
print("[3] Tentar subir em uma árvore.")
r = int(input("Escolha:"))
while r > 3 or r < 1:
    r = int(input("Digite uma opção válida:"))
    time.sleep(2)
if r == 1:
    print("Antes de começar a correr você escuta um som de disparo, quando olha para trás o animal está no chão e próximo a ele um homem, também fugitivo e náufrago do navio, o mesmo possuia uma arma de fogo em sua mão.")
    print("-=-Você ganhou 0 pontos pela escolha imprudente.-=-")
elif r == 2:
    print("Com muita sorte você consegue acertar o animal com seu facão e se livra da situação, quando se depara com outro homem também fugitivo e náufrago do navio, o mesmo possuia com uma arma de fogo em sua mão.")
    print("-=-Você ganhou 10 pontos pela melhor escolha.-=-")
    pontos = pontos + 10
elif r == 3:
    print("Antes de começar subir na árvore você escuta um som de disparo, quando olha para trás o animal está no chão e próximo a ele um homem, também fugitivo e náufrago do navio, o mesmo possuia com uma arma de fogo em sua mão.")
    print("-=-Você ganhou 5 pontos pela escolha.-=-")
    pontos = pontos + 5
print("Seu nome era Geremias.")
print("Ao encontrar seu companheiro você diz:")
print("- Geremias!! Achei que eu era o único sobrevivente.")
print(" ")
print("Geremias responde:")
print("- Por sorte não!")
print(" ")
print("Você então questiona:")
print("- Como saíremos desta ilha?")
print(" ")
print("Geremias:")
print("- Alguns botes desprenderam-se do nosso navio! A maré os levou para a costa e podemos usá-los!")
print(" ")
print("Você deseja:")
print("[1] Confiar no conhecido e seguir adiante para a costa.")
print("[2] Seguir com Geremias, mas com a condição de ficar com sua arma de fogo.")
print("[3] Não confiar no sujeito e seguir seu caminho sozinho.")
r = int(input("Escolha:"))
while r > 3 or r < 1:
    r = int(input("Digite uma opção válida:"))
    time.sleep(2)
if r == 1:
    print("Vocês conseguem chegar à costa e os botes estão lá.")
    print("-=-Você ganhou 10 pontos por confiar em seu companheiro.-=-")
    pontos = pontos + 10
elif r == 2:
    print("Geremias aceita sua proposta mas fica desconfortável, os botes estão lá.")
    print("-=-Você ganhou 5 pontos por não confiar em seu companheiro.-=-")
elif r == 3:
    print("-=-Você entrou em uma situção crítica.-=-")
    print("Após afastar-se de seu companheiro, você se depara sozinho e sem saber para onde ir.")
    print("Você deseja:")
    print("[1] Correr em direção ao norte.")
    print("[2] Correr em direção ao leste.")
    print("[3] Correr em direção ao oeste.")
    r = int(input("Escolha:"))
    while r > 3 or r < 1:
        r = int(input("Digite uma opção válida:"))
    time.sleep(2)
    if r == 1:
        print("Por sorte você achou seu caminho até a costa, Geremias já havia ido embora, mas ainda tinham botes para sua fuga.")
        print("-=-Você ganhou 10 pontos por conseguir achar seu caminho e escapar com vida e bem.-=-")
        pontos = pontos + 10
    elif r == 2:
        print("Infelizmente, o leste não era o caminho certo após alguns dias de caminhada, seu corpo não resiste à fome e sede.")
        exit("Você morreu, fim do jogo. Sua pontuação foi de {} pontos.".format(pontos))
    elif r == 2:
        print("Infelizmente, o oeste não era o caminho certo após alguns dias de caminhada, seu corpo não resiste à fome e sede.")
        exit("Você morreu, fim do jogo. Sua pontuação foi de {} pontos.".format(pontos))
print("-=-Você está agora em uma situação crítica.-=-")
print("Ao se aproximar dos botes e começar a empurra-los para o mar, os nativos da ilha te acham e estão a alguns metros de distancia, furiosos.")
print("Você deseja:")
print("[1] Empurrar o bote em direção ao mar o mais rapido possível.")
print("[2] Tentar usar seu facão para atacar todos os nativos.")
print("[3] Implorar para q o deixem ir embora.")
r = int(input("Escolha:"))
while r > 3 or r < 1:
    r = int(input("Digite uma opção válida:"))
    time.sleep(2)
if r == 1:
    print("Felizmente você conseguiu empurrar o bote a tempo e escapar com vida!")
    print("-=-Você ganhou 10 pontos pela melhor escolha-=-")
    pontos = pontos + 10
elif r == 2:
    print("Você não consegue se defender, e é pego novamente.")
    exit("Você morreu, fim do jogo. Sua pontuação foi de {} pontos.".format(pontos))
elif r == 3:
    print("Você larga seu facão e implora para poder sair vivo, os nativos pegam seu facão de volta, mas o deixam partir")
    print("-=-Você ganhou 5 pontos pela escolha-=-")
    pontos = pontos + 5
print("-=-PARABÉNS DON BARELLA-=-")
print("Você ganhou o jogo escapando com vida!")
print("Sua pontuação foi de {} pontos! O que te torna um: ".format(pontos))
if pontos >= 25:
    print("MASTER")
elif 25 > pontos >= 15:
    print("PRO")
else:
    print("AMADOR")
  
    



    
