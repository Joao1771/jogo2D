import os
import WConio2  # pip install WConio2
import trocar_tela
import sprites
import status
import fases
import salvar

def jogo():
    tela = []
    cont = 0
    largura = 150
    altura = 38
    aviao_y = altura - 6
    aviao_x = largura // 2
    tiro_y = -1
    tiro_x = -1
    dinheiros = []
    moedas = status.moedas
    dano = status.dano
    vidas = status.vida

    # Cada inimigo é uma tupla (x, y)
    inimigos = []
    vida_inimigos = []
    inimigos_horizontais = []  # inimigos horizontais
    vida_inimigos_horizontais = []
    direcao_horizontais = [1, 1, 1, 1]  
    tiros_inimigos = []  # tiros inimigos

    # Criar função para tirar o pisca-pisca
    def gotoxy(x, y):
        print(f"\033[{y};{x}H", end="", flush=True)

    # Limpa o terminal ao executar
    def limpar_tela():
        os.system("cls")

    # Criando a tela
    def criar_tela(altura, largura):
        for y in range(altura):
            tela.append([])
            for x in range(largura):
                tela[y].append("")
        return tela        

    # Renderiza os elementos da tela
    def preencher_tela(tela, altura, largura, inimigos):
        for y in range(altura):
            for x in range(largura):
                    tela[y][x] = " "
        for y in range(altura):
            for x in range(largura):
                if (x, y) in tiros_inimigos:
                    tela[y][x] = "!"
                elif y == tiro_y and x == tiro_x:
                    tela[y][x] = "|"
                elif (x, y) in inimigos:
                    mostrar_sprite(sprites.get_inimigo(),x,y)
                elif (x, y) in inimigos_horizontais:
                    mostrar_sprite(sprites.get_inimigo_horizontal(),x,y)
                elif y == aviao_y and x == aviao_x:
                    mostrar_sprite(sprites.get_aviao(),aviao_x,aviao_y)
                elif [x, y] in dinheiros:
                    mostrar_sprite(sprites.get_dinheiro(), x, y)

    #São enviados parâmetros de coordenada, largura e altura de dois elementos para retornar True em caso de colisão
    def colide_elementos(sprite1_x, sprite1_y, largura1, altura1, sprite2_x, sprite2_y, largura2, altura2):
        pontas1 = [ (sprite1_x, sprite1_y), (sprite1_x + largura1 - 1, sprite1_y),
                    (sprite1_x, sprite1_y + altura1 - 1), (sprite1_x + largura1 - 1, sprite1_y + altura1 - 1) ]
        pontas2 = [ (sprite2_x, sprite2_y), (sprite2_x + largura2 - 1, sprite2_y),
                    (sprite2_x, sprite2_y + altura2 - 1), (sprite2_x + largura2 - 1, sprite2_y + altura2 - 1) ]
        for px, py in pontas1:
            if (sprite2_x <= px < sprite2_x + largura2 and
                sprite2_y <= py < sprite2_y + altura2):
                return True
        for px, py in pontas2:
            if (sprite1_x <= px < sprite1_x + largura1 and
                sprite1_y <= py < sprite1_y + altura1):
                return True
        return False

    # Mostra as bordas * da tela
    def mostrar_tela(tela,altura,largura):
        print("*" * (largura + 2))
        for x in range(altura):
            print("*", end='')
            for y in range(largura):
                print(tela[x][y], end='')
            print("*")
        print("*" * (largura + 2))

    #Na sprite, itera por cada linha e caractere e mostra na tela 
    def mostrar_sprite(sprite,sprite_x,sprite_y):
        nonlocal tela
        for y, linha in enumerate(sprite):
            for x, caractere in enumerate(linha):
                    tela[y + sprite_y][x + sprite_x] = caractere
    
    def mostrar_vida(qtd):
        nonlocal vidas
        coracoes = ""
        match qtd:
            case 1: coracoes = "█"
            case 2: coracoes = "█ █"
            case 3: coracoes = "█ █ █"
            case 4: coracoes = "█ █ █ █"
            case 5: coracoes = "█ █ █ █ █"
        return "vidas: " + coracoes + "           "

    # Retorna True caso o tiro acerte em um inimigo
    def verifica_colisao(tiro_x, inimigos,inimigos_horizontais):
        nonlocal dinheiros, vida_inimigos, vida_inimigos_horizontais, dano, tiro_y

        for i in range(len(inimigos) -1, -1, -1):
            if colide_elementos(inimigos[i][0],inimigos[i][1],5,3,tiro_x,tiro_y,1,1):
                vida_inimigos[i] -= dano
                if vida_inimigos[i] <= 0:
                    inimigos.pop(i)
                    vida_inimigos.pop(i)
                    dinheiros.append([tiro_x,tiro_y])
                tiro_y = -1

        for i in range(len(inimigos_horizontais) -1, -1, -1):
            if colide_elementos(inimigos_horizontais[i][0],inimigos_horizontais[i][1],7,4,tiro_x,tiro_y,1,1):
                vida_inimigos_horizontais[i] -= dano
                if vida_inimigos_horizontais[i] <= 0:
                    inimigos_horizontais.pop(i)
                    vida_inimigos_horizontais.pop(i)
                    dinheiros.append([tiro_x,tiro_y])
                tiro_y = -1

    #verifica se o aviao tocou na moeda
    def verifica_coleta(dinheiros):
        nonlocal moedas
        if len(dinheiros) > 0:
            for i in dinheiros:
                if colide_elementos(i[0],i[1],3,3,aviao_x,aviao_y,6,3):
                    moedas += 1
                    dinheiros.remove(i)
                    return dinheiros
            return dinheiros
        else: return dinheiros



    #retorna True caso o jogador perca o jogo por tocar na nave inimiga ou deixar eles chegar em baixo
    def checar_derrota():
        nonlocal vidas
        esperar = 0
        frase = ""
        for x, y in inimigos:
            if colide_elementos(x,y,5,3,aviao_x,aviao_y,6,3):
                vidas -= 1
                inimigos.remove((x, y))
                frase = "Um inimigo te atingiu!"
            if y == altura - 3:
                vidas -= 1
                inimigos.remove((x, y))
                frase = "Algum inimigo escapou!"
        for x, y in inimigos_horizontais:
            if colide_elementos(x,y,7,4,aviao_x,aviao_y,6,3):
                vidas -= 1
                inimigos_horizontais.remove((x, y))
                frase = "Você tocou no inimigo atirador!"
        for x, y in tiros_inimigos:
            if colide_elementos(x,y,1,1,aviao_x,aviao_y,6,3):
                tiros_inimigos.remove((x, y))
                vidas -= 1
                frase = "Você tomou tiro do inimigo!"
        if vidas <= 0:
            print(f"{frase} GAME OVER.                       ")
            while esperar < 100000000:
                esperar += 1
            return True
        else: return False
    
    #função com o WConio2 para receber qualquer entrada
    def entrada_jogador():
        nonlocal aviao_x, aviao_y, tiro_x, tiro_y, altura, largura
        print(f"a,→ d,← w,↑ s,↓ f=fogo.", f"{moedas}R$  {mostrar_vida(vidas)}       ")
        if WConio2.kbhit():
            codigo, simbolo = WConio2.getch()
            #print(codigo, " ", simbolo)  # descobre o codigo da tecla pressionada

            def aviao_esquerda(aviao_x):
                if aviao_x > 0:
                    return aviao_x - 1
                else:
                    return aviao_x

            def aviao_direita(aviao_x, largura):
                if aviao_x + 4 < largura - 1:
                    return aviao_x + 1
                else:
                    return aviao_x

            def aviao_cima(aviao_y):
                if aviao_y > 0:
                    return aviao_y - 1
                else:
                    return aviao_y

            def aviao_baixo(aviao_y, altura):
                if aviao_y + 2 < altura - 1:
                    return aviao_y + 1
                else:
                    return aviao_y

            def atirar(tiro_x, tiro_y):
                if tiro_y == -1:
                    tiro_x = aviao_x + 2
                    tiro_y = aviao_y
                return tiro_x, tiro_y

            match codigo:
                case 97: aviao_x = aviao_esquerda(aviao_x)  # a
                case 65: aviao_x = aviao_esquerda(aviao_x)  # A
                case 75: aviao_x = aviao_esquerda(aviao_x)  # → 
                case 100: aviao_x = aviao_direita(aviao_x, largura)
                case 68: aviao_x = aviao_direita(aviao_x, largura)
                case 77: aviao_x = aviao_direita(aviao_x, largura)
                case 119: aviao_y = aviao_cima(aviao_y)
                case 87: aviao_y = aviao_cima(aviao_y)
                case 72: aviao_y = aviao_cima(aviao_y)
                case 115: aviao_y = aviao_baixo(aviao_y, altura)
                case 83: aviao_y = aviao_baixo(aviao_y, altura)
                case 80: aviao_y = aviao_baixo(aviao_y, altura)
                case 102: tiro_x, tiro_y = atirar(tiro_x, tiro_y)  # f
                case 32: tiro_x, tiro_y = atirar(tiro_x, tiro_y)  # espaço
                case 27: 
                    trocar_tela.trocar_tela("menu")
                    return True
                
    #move o tiro do jogador para cima
    def movertiro(tiro_y):
        if tiro_y >= 0 and cont % status.lerdeza_tiro == 0:
            return tiro_y - 1
        return tiro_y     
    #move os inimigos para baixo
    def mover_inimigos(cont, inimigos):
        if cont % 80 == 0:
            return [(x, y + 1) for (x, y) in inimigos if y + 1 < altura]
        return inimigos

    # Mover inimigos horizontais
    def mover_inimigos_horizontais(cont):
        nonlocal inimigos_horizontais, direcao_horizontais
        VELOCIDADE_HORIZONTAL = 30  # Quanto maior, mais lento

        if cont % VELOCIDADE_HORIZONTAL != 0:
            return  # Só move a cada 200 ciclos
        while len(inimigos_horizontais) > len(direcao_horizontais):
            direcao_horizontais.append(1)
        while len(inimigos_horizontais) < len(direcao_horizontais):
            direcao_horizontais.pop()
        for i in range(len(inimigos_horizontais)):
            x, y = inimigos_horizontais[i]
            direcao = direcao_horizontais[i]

            # Inverter direção se chegar nas bordas
            if x + 6 + direcao >= largura - 1 or x + direcao <= 0:
                direcao_horizontais[i] *= -1
                direcao = direcao_horizontais[i]

            inimigos_horizontais[i] = (x + direcao, y)

    # Mover tiros dos inimigos para baixo
    def mover_tiros_inimigos():
        nonlocal tiros_inimigos
        VELOCIDADE_TIRO_INIMIGO = 10  # Quanto maior, mais lento

        if cont % VELOCIDADE_TIRO_INIMIGO != 0:
            return  # só move os tiros de vez em quando

        novos_tiros = []
        for (x, y) in tiros_inimigos:
            if y < altura - 1:
                novos_tiros.append((x, y + 1))  # move para baixo
        tiros_inimigos[:] = novos_tiros

    #move cada moeda para baixo e se ela sumir da tela deleta
    def mover_dinheiros(dinheiros):
        d_filtrados = []
        if len(dinheiros) <= 0 or cont % 40 != 0:
            return dinheiros
        else:
            for d in dinheiros:
                d[1] += 1
            for d in dinheiros:
                if d[1] < altura - 3: d_filtrados.append(d)
            return d_filtrados
        
                

    # Inimigos atiram
    def inimigos_atiram():
        nonlocal tiros_inimigos
        if cont % 500 == 0:  # Cada ciclos os inimigos atiram
            for (x, y) in inimigos_horizontais:
                tiros_inimigos.append((x + 3, y + 3))  # Tiros dos inimigos (para baixo)

    # Verificar colisão do tiro inimigo com o avião

    limpar_tela()
    criar_tela(altura, largura)

    while True:
        cont += 1
        if entrada_jogador(): break

        gotoxy(0, 0)

        # Mover o tiro do jogador
        tiro_y = movertiro(tiro_y)

        # Verifica colisão do tiro do jogador com inimigos verticais
        verifica_colisao(tiro_x, inimigos,inimigos_horizontais)

        # Move e verifica colisão do dinheiro
        dinheiros = mover_dinheiros(dinheiros)
        dinheiros = verifica_coleta(dinheiros)

        # Mover inimigos verticais
        inimigos = mover_inimigos(cont, inimigos)

        # Recria inimigos verticais se forem todos destruídos
        if inimigos == [] and inimigos_horizontais == []:
            inimigos,vida_inimigos,inimigos_horizontais,vida_inimigos_horizontais = fases.novos_inimigos()

        # Mover inimigos horizontais
        mover_inimigos_horizontais(cont)

        # Inimigos horizontais atiram
        inimigos_atiram()

        # Mover os tiros dos inimigos
        mover_tiros_inimigos()

        # Preencher e mostrar a tela
        preencher_tela(tela, altura, largura, inimigos)
        mostrar_tela(tela, altura, largura)

        # Verifica vitória
        if fases.checar_vitoria(inimigos,dinheiros,inimigos_horizontais):
            status.moedas = moedas
            status.fase += 1
            status.onda = 0
            trocar_tela.trocar_tela("menu_melhorias")
            break

        # Verifica derrota por colisão com inimigo vertical
        if checar_derrota():
            trocar_tela.trocar_tela("menu")
            break
