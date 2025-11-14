import status

#se todos os inimigos forem destruídos,recria as coordenadas em outras posições dependendo da onda atual
def novos_inimigos():

    status.onda += 1
    # se estivermos na primeira fase
    if status.fase == 1:
        match status.onda:
            case 1:
                return(
                    [(30,0),(45,0),(60, 0),(75, 0),(90, 0),(105, 0),(120,0)],[1,1,1,1,1,1,1],[],[])
            case 2:
                return([(35,0),(50, 0),(65, 0),(80, 0),(95, 0),(110, 0)],[1,1,1,1,1,1],[],[])
            case _: return ([],[],[],[])

    # MUDA: Aumento do número de inimigos e vida para a Fase 2
    if status.fase == 2:
        match status.onda:
            case 1:
                # 6 inimigos verticais iniciais
                return(
                    [(15, 0),(30, 0),(45, 0),(60, 0),(75, 0),(90, 0)],
                    [1,1,1,1,1,1],[(0, 5)],[2])
            case 2:
                # 8 inimigos verticais
                return(
                    [(10, 0),(25, 0),(40, 0),(55, 0),(70, 0),(85, 0),(100, 0),(115, 0)],
                    [2,2,2,2,2,2,2,2],[(0, 5),(100, 5)],[3, 3]) # Adicionado 2 horizontais
            case 3:
                # 8 inimigos verticais com mais vida, 2 horizontais
                return(
                    [(10, 0),(25, 0),(40, 0),(55, 0),(70, 0),(85, 0),(100, 0),(115, 0)],
                    [3,3,3,3,3,3,3,3],[(0, 5),(100, 5)],[3, 3])
            case 4:
                return(
                    [(10, 0),(25, 0),(40, 0),(55, 0),(70, 0),(85, 0),(100, 0),(115, 0),(130, 0)],
                    [3,3,3,3,3,3,3,3,3],[(0, 5),(100, 5)],[4, 4]) # Mais um vertical
            case 5:
                return(
                    [(10, 0),(25, 0),(40, 0),(55, 0),(70, 0),(85, 0),(100, 0),(115, 0),(130, 0)],
                    [4,4,4,4,4,4,4,4,4],[(0, 5),(100, 5),(50, 10)],[4, 4, 4]) # Mais vida e 3 horizontais
            case 6:
                return(
                    [(5, 0),(20, 0),(35, 0),(50, 0),(65, 0),(80, 0),(95, 0),(110, 0),(125, 0),(140, 0)],
                    [4,4,4,4,4,4,4,4,4,4],[(0, 5),(100, 5),(50, 10)],[5, 5, 5]) # 10 verticais
            case 7:
                return(
                    [(5, 0),(20, 0),(35, 0),(50, 0),(65, 0),(80, 0),(95, 0),(110, 0),(125, 0),(140, 0)],
                    [4,4,4,4,4,4,4,4,4,4],[(0, 5),(100, 5),(50, 10)],[6, 6, 6])
            case _: return ([],[],[],[])

    # se estivermos na fase 3:
    if status.fase == 3:
        match status.onda:
            case 1:
                # 8 inimigos verticais com 4 de vida, 2 horizontais com 4 de vida
                return(
                    [(10, 0),(25, 0),(40, 0),(55, 0),(70, 0),(85, 0),(100, 0),(115, 0)],
                    [4,4,4,4,4,4,4,4],[(0, 5),(100, 5)],[4, 4] )
            case 2:
                # 10 inimigos verticais com 4 de vida
                return(
                    [(5, 0),(20, 0),(35, 0),(50, 0),(65, 0),(80, 0),(95, 0),(110, 0),(125, 0),(140, 0)],
                    [4,4,4,4,4,4,4,4,4,4],[(0, 5),(100, 5),(50, 10)],[4, 4, 4])
            case 3:
                # 10 verticais com 5 de vida
                return(
                    [(5, 0),(20, 0),(35, 0),(50, 0),(65, 0),(80, 0),(95, 0),(110, 0),(125, 0),(140, 0)],
                    [5,5,5,5,5,5,5,5,5,5],[(0, 5),(100, 5),(50, 10)],[5, 5, 5])
            case 4:
                # 12 verticais com 5 de vida
                return(
                    [(5, 0),(15, 0),(25, 0),(35, 0),(45, 0),(55, 0),(70, 0),(80, 0),(90, 0),(100, 0),(110, 0),(120, 0)],
                    [5,5,5,5,5,5,5,5,5,5,5,5],[(0, 5),(100, 5),(50, 10)],[6, 6, 6])
            case 5:
                # 12 verticais com 6 de vida
                return(
                    [(5, 0),(15, 0),(25, 0),(35, 0),(45, 0),(55, 0),(70, 0),(80, 0),(90, 0),(100, 0),(110, 0),(120, 0)],
                    [6,6,6,6,6,6,6,6,6,6,6,6],[(0, 5),(100, 5),(50, 10),(130, 15)],[7, 7, 7, 7]) # 4 horizontais
            case 6:
                return(
                    [(5, 0),(15, 0),(25, 0),(35, 0),(45, 0),(55, 0),(70, 0),(80, 0),(90, 0),(100, 0),(110, 0),(120, 0),(135, 0)],
                    [7,7,7,7,7,7,7,7,7,7,7,7,7],[(0, 5),(100, 5),(50, 10),(130, 15)],[8, 8, 8, 8])
            case 7:
                return(
                    [(5, 0),(15, 0),(25, 0),(35, 0),(45, 0),(55, 0),(70, 0),(80, 0),(90, 0),(100, 0),(110, 0),(120, 0),(135, 0)],
                    [8,8,8,8,8,8,8,8,8,8,8,8,8],[(0, 5),(100, 5),(50, 10),(130, 15)],[9, 9, 9, 9])
            case 8:
                return(
                    [(5, 0),(15, 0),(25, 0),(35, 0),(45, 0),(55, 0),(70, 0),(80, 0),(90, 0),(100, 0),(110, 0),(120, 0),(135, 0)],
                    [9,9,9,9,9,9,9,9,9,9,9,9,9],[(0, 5),(100, 5),(50, 10),(130, 15),(75, 20)],[10, 10, 10, 10, 10]) # 5 horizontais
            case 9:
                return(
                    [(5, 0),(15, 0),(25, 0),(35, 0),(45, 0),(55, 0),(70, 0),(80, 0),(90, 0),(100, 0),(110, 0),(120, 0),(135, 0)],
                    [9,9,9,9,9,9,9,9,9,9,9,9,9],[(0, 5),(100, 5),(50, 10),(130, 15),(75, 20)],[10, 10, 10, 10, 10])
            case 10:
                return(
                    [(5, 0),(15, 0),(25, 0),(35, 0),(45, 0),(55, 0),(70, 0),(80, 0),(90, 0),(100, 0),(110, 0),(120, 0),(135, 0)],
                    [9,9,9,9,9,9,9,9,9,9,9,9,9],[(0, 5),(100, 5),(50, 10),(130, 15),(75, 20)],[12, 12, 12, 12, 12])
            case _: return ([],[],[],[])
            
#   retorna True caso as listas de inimigos e moedas estejam vazios e
# novos_inimigos retorne [] dependendo da fase
def checar_vitoria(inimigos, dinheiros, inimigos_horizontais):
    esperar = 0
    galaxia = ""
    ganhou = False
    if  inimigos == [] and dinheiros == [] and inimigos_horizontais == []:
        match status.fase:
            case 1: 
                if novos_inimigos() == ([],[],[],[]):
                    galaxia = "a Via Láctea"
                    ganhou = True
            case 2: 
                if novos_inimigos() == ([],[],[],[]):
                    galaxia = "Hoag's"
                    ganhou = True
            case 3: 
                if novos_inimigos() == ([],[],[],[]):
                    galaxia = "Andrômeda"
                    ganhou = True
        print(f"Você libertou {galaxia}!                             ")
        while esperar < 100000000:
            esperar += 1
        return ganhou