import os
import WConio2 # pip install WConio2
import trocar_tela
import sprites
import status

def menu_melhorias():
    #Função para mudar o local do cursor
    def gotoxy(x, y):
        print(f"\033[{y};{x}H", end='', flush=True)
    #Função para criar tela(matriz)
    def CriarTela(altura_y, largura_x, tela, item):
        for y in range(altura_y):
            tela.append([])
            for x in range(largura_x):
                tela[y].append(item)

    #Função para limpar a tela(matriz)
    def LimparTela(tela):
        for y in range(altura_y):  #vertical        
            for x in range(largura_x): #horizontal
                tela[y][x] = " "

    #Função para desenhar na tela(matriz)
    def DesenharTela(tela,  y_seta, x_seta):
        for y in range(altura_y):
            for x in range(largura_x):

                #Sprite do foguete do menu e do dinheiro
                if y == y_foguete and x == x_foguete:
                    mostrar_sprite(sprites.get_foguete_menu(),x_foguete,y_foguete)

                if y == y_dinheiro and x == x_dinheiro:
                    mostrar_sprite(sprites.get_dinheiro_menu(status.moedas),x_dinheiro,y_dinheiro)
                #Sprites de dano, vida e vel. tiro
                if y == y_dano and x == x_dano:
                    mostrar_sprite(sprites.get_dano(status.dano),x_dano,y_dano)

                if y == y_vida and x == x_vida:
                    mostrar_sprite(sprites.get_vida(status.vida),x_vida,y_vida)

                if y == y_vel_tiro and x == x_vel_tiro:
                    mostrar_sprite(sprites.get_vel_tiro(status.lerdeza_tiro),x_vel_tiro,y_vel_tiro)
                #Texto escrito VOLTAR
                if y == y_voltar and x == x_voltar:
                    mostrar_sprite(sprites.get_voltar(),x_voltar,y_voltar)

                #Desenha seta
                if y == y_seta and x == x_seta:
                    mostrar_sprite(sprites.get_seta_upgrades(),x_seta,y_seta)

                if y == y_descricao and x == x_descricao:
                    mostrar_sprite(["↑, w ou W e ↓,s ou S para navegação."],x_descricao,y_descricao)

    #Função para colocar a tela(matriz) no terminal
    def MostrarTela(tela):
        for y in range(altura_y):
            for x in range(largura_x):
                print(tela[y][x], end='')
            print()     #necessário para separar as listas da coordenada y

    def mostrar_sprite(sprite,sprite_x,sprite_y):
        nonlocal tela
        for y, linha in enumerate(sprite):
            for x, caractere in enumerate(linha):
                    tela[y + sprite_y][x + sprite_x] = caractere

    #Função que aumenta o relogio geral
    def AumentarRelogio(cont):
        cont += 1
        return cont

    #Função para capturar o input do jogador para o menu
    def CapturaInput(codigo):
        if WConio2.kbhit():
            codigo, simbolo = WConio2.getch()
            return codigo

    #Função para mudar as coordenadas da seta indicadora na tela(matriz)
    def MudaCoordenadaYSetaIndicadora(codigo, y_seta, y_vida, y_voltar):
        if y_seta > y_vida + 1 and (codigo == 119 or codigo == 87 or codigo == 72):
            if y_seta == y_voltar:
                y_seta -= 7
            else:
                y_seta -= 10
        elif y_seta + 1 <= y_voltar and (codigo == 115 or codigo == 83 or codigo == 80):
            if y_seta == y_voltar - 7:
                y_seta += 7
            else:
                y_seta += 10
        return y_seta
    
    # Recebe o atributo e o lvl e printa uma descrição em baixo da tela.
    def descricao(atributo,lvl = 0):
        texto = ""
        lista = []

        if atributo == "vida":
            lista = vida_lvl
            texto = "& Aumenta a vida do jogador em 1.        "
        elif atributo == "dano":
            lista = dano_lvl
            texto = "& Aumenta o dano do tiro do jogador em 1.         "
        elif atributo == "vel_tiro":
            lista = vel_tiro_lvl
            texto = "& Aumenta a velocidade do tiro do jogador.          "

        if atributo == "voltar": texto = "Volta para o menu principal.                        "
        elif lvl == lista[1]:
           texto = texto.replace("&",f"Custa {custo_upg_1}R$.")
        elif lvl == lista[2]:
           texto = texto.replace("&",f"Custa {custo_upg_2}R$.")
        elif lvl == lista[3]:
           texto = texto.replace("&", "Nível Máximo.")

        
        print(texto)

    #As funções melhorar pegam o status e passam para o próximo nivel se tiver dinheiro suficiente
    def melhorar_vida(moedas):
        custo = 0
        valor = status.vida
        if valor == vida_lvl[1]: custo = custo_upg_1
        elif valor == vida_lvl[2]: custo = custo_upg_2
        elif valor == vida_lvl[3]: return moedas, valor
        if moedas >= custo:
            moedas -= custo
            valor += 1
        return moedas,valor
    
    def melhorar_dano(moedas):
        custo = 0
        valor = status.dano
        if valor == dano_lvl[1]: custo = custo_upg_1
        elif valor == dano_lvl[2]: custo = custo_upg_2
        elif valor == dano_lvl[3]: return moedas, valor
        if moedas >= custo:
            moedas -= custo
            valor += 1
        return moedas,valor
    
    def melhorar_vel_tiro(moedas):
        custo = 0
        valor = status.lerdeza_tiro
        if valor == vel_tiro_lvl[1]: custo = custo_upg_1
        elif valor == vel_tiro_lvl[2]: custo = custo_upg_2
        elif valor == vel_tiro_lvl[3]: return moedas, valor
        if moedas >= custo:
            moedas -= custo
            valor -= 6
        return moedas,valor
    '''
    ===== FASES =====
    '''

    #== LIMPANDO O TERMINAL ==
    os.system('cls')

    #== CRIANDO TELA ==
    tela = []
    item = " "

    # Espeficações tela
    altura_y = 38
    largura_x = 150

    #Coordenadas iniciais
    y_seta = 6
    x_seta = 57
    y_descricao, x_descricao = [altura_y - 2, 1]
    y_dinheiro, x_dinheiro = [2,largura_x - 30]
    y_vida, x_vida = [5,60] #Eh o primeiro caractere de cima 
    y_dano, x_dano = [15, 60]
    y_vel_tiro, x_vel_tiro = [25,60]
    y_foguete, x_foguete = [7, 10]
    y_voltar, x_voltar = [altura_y - 5,60]

    #Valores como parâmetro (soft coding)
    custo_upg_1 = 4
    custo_upg_2 = 8
    vida = status.vida
    dano = status.dano
    vel_tiro = status.lerdeza_tiro
    vel_tiro_lvl = [0, vel_tiro, 7, 1] #Vel_tiro_lvl[1] indice é o lvl
    dano_lvl = [0, dano, 2, 3]
    vida_lvl = [0, vida, 4, 5]
    

    # Cria a tela
    CriarTela(altura_y, largura_x, tela, item)

    # Relogio geral
    cont = 0

    #Codigo do input do jogador inicial
    codigo = 0

    while True:

        #== LIMPANDO TELA ==
        LimparTela(tela)

        #== DESENHAR O MENU NA TELA ==
        DesenharTela(tela, y_seta, x_seta)

        #== COLOCANDO A TELA NO TERMINAL ==
        gotoxy(0,0)
        MostrarTela(tela)

        #== RELOGIO AUMENTA ==
        cont = AumentarRelogio(cont)

        #== CAPTURA INPUT DO JOGADOR ==
        codigo = CapturaInput(codigo)
        
        # se ESC for pressionado
        if codigo == 27: 
            trocar_tela.trocar_tela("menu")
            break
        # se a seta estiver em VIDA
        if y_seta == y_vida + 1:
            descricao("vida",status.vida)
            # e ENTER for apertado
            if codigo == 13:
                status.moedas, status.vida = melhorar_vida(status.moedas)

        # se a seta estiver em DANO
        if y_seta == y_dano + 1:
            descricao("dano",status.dano)
            if codigo == 13:
                status.moedas, status.dano = melhorar_dano(status.moedas)

        # se a seta estiver em VEL_TIRO
        if y_seta == y_vel_tiro + 1:
            descricao("vel_tiro", status.lerdeza_tiro)
            if codigo == 13:
                status.moedas, status.lerdeza_tiro = melhorar_vel_tiro(status.moedas)

        # se a seta estiver em VOLTAR
        if y_seta == y_voltar:
            descricao("voltar")
            if codigo == 13:
                trocar_tela.trocar_tela("menu_fases")
                break

        #== MUDA A POSICAO DA SETA SEGUNDO INPUT ==
        y_seta = MudaCoordenadaYSetaIndicadora(codigo, y_seta, y_vida, y_voltar)
