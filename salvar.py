import status

valores_status = [status.vida,status.dano,status.moedas,status.lerdeza_tiro,status.fase,status.onda]

# pega os valores de status.py e escreve no arquivo save.txt
def salvar():
    with open("save.txt", "w") as arquivo:

        # getValores -> retorna uma lista com todos os valores de status.py
        for item in status.getValores():
            arquivo.write(str(item) + " ")
        print("Jogo salvo no save.txt!                ")

# contrario de salvar: pega os valores do save.txt e define os de status
def carregar():
    carregados = []

    with open("save.txt", "r") as arquivo:
        conteudo = arquivo.read().strip()
        if conteudo != '':
            for item in conteudo.split(" "):
                if item != '':
                    carregados.append(int(item))
        else:
            print("O save está vazio.        ")
            novo_jogo()
            esperar(100000000)
            return
    
    # cada variavel de status recebe um valor do arquivo
    status.vida = carregados[0]
    status.dano = carregados[1]
    status.moedas = carregados[2]
    status.lerdeza_tiro = carregados[3]
    status.fase = carregados[4]
    status.onda = carregados[5]
    print("carregando save...                 ")
    esperar(100000000)

# define os valores do arquivo e do status como iniciais
def novo_jogo():
    status.vida = 3
    status.dano = 1
    status.moedas = 0
    status.lerdeza_tiro = 13
    status.fase = 1
    status.onda = 0
    arquivo = open("save.txt", "w")
    arquivo.write("3 1 0 13 1 0")
    arquivo.close()
    print("Criando novo save...        ")
    esperar(100000000)

# simula um loading rodando um while até o número "segundos"
def esperar(segundos):
    cont = 0
    while cont < segundos:
        cont += 1