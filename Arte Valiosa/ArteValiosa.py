import networkx as nx
from ListaDeSensores import *
import matplotlib.pyplot as plt

sensores = ListaDeSensores()

# Entrada dos dados
museoLinha, museoColuna, numeroDeSensores = input().split(" ");
museoLinha = int(museoLinha)
museoColuna = int(museoColuna)
numeroDeSensores = int(numeroDeSensores)

# Tratamentos de exceções
if ( not 10 <= museoLinha ):
    raise Exception("O valor da linha do Museo deve ser maior ou igual a 10")
elif ( 10001 <= museoColuna):
    raise Exception("O valor da coluna do Museo deve ser menor ou igual a 10.000")
elif (not 1 <= numeroDeSensores and numeroDeSensores <= 1000):
    raise Exception("A quantidade de sensores no Museo deve ser maior que 1 e menor que 10002")

# Lendo todos os sensores dentro do Museo
for sensor in range(0, numeroDeSensores):
    lista = list();
    x, y, tamanho = input().split(" ")
    x = int(x)
    y = int(y)
    metrosDoSensor = int(tamanho)

    # Tratamentos de exceções
    if (not (x > 0 and x < museoLinha)):
        raise Exception("O valor do ponto x do sensor deve ser maior que 0 e menor que a linha do Museo ({})".format(museoLinha))
    elif (not (y > 0 and y < museoColuna)):
        raise Exception("O valor do ponto y do sensor deve ser maior que 0 e menor que a coluna do Museo ({})".format(museoColuna))
    elif (not (metrosDoSensor > 0 and metrosDoSensor < 10000)):
        raise Exception("O valor de metros do tamanho do sensor deve ser maior que 0 e menor que 10000")

    sensores.addSensor(x, y, metrosDoSensor)



# Verficar se o proximo elemento da lista está dentro da matriz
def verificarSeExisteElementoNaMatriz(matriz, linha, coluna):
    if (linha >= 0 and coluna >= 0):
        if (linha <= (len(matriz)-1) and coluna <= (len(matriz[0])-1)):
                return True
    return False

# Verificando o caminho feito pelo ladrão até chegar na Obra de arte ou não.
def verficarOsPossiveisCaminhosAndados(matriz, linha, coluna, pilha):
    if (verificarSeExisteElementoNaMatriz(matriz, linha, coluna)):
        if (len(pilha) == 0):
            if (matriz[linha][coluna] == 1):
                return True
        elif ((pilha[len(pilha)-1][0] != linha or pilha[len(pilha)-1][1] != coluna) and matriz[linha][coluna] == 1):
            return True
    return False

# Declarando variáveis
grafico = nx.Graph()
vertices = 1;
Museo, lista, pilha = [], [], []
saida = False
linhaInicial = 0
colunaInicial = 0

# Criando uma Matriz que será o plano do Museo.
for linha in range(0, museoLinha):
    lista = []
    Museo.append(lista)
    for coluna in range(0, museoColuna):
        lista.append(1)
        grafico.add_edge(vertices - 1, vertices)
        grafico.add_node(vertices)
        vertices += 1

Museo[museoLinha-1][museoColuna-1] = 10

for linha in range(0, len(Museo)):
    print(Museo[linha])

# Criando os sensores dentro do Museo
Museo = sensores.montaTodasAsAreasDeUmaListaDeSensores( Museo )

print("\n\n")

for linha in range(0, len(Museo)):
    print(Museo[linha])


while(True):

    # Verificando se a o ladrão chegou na Obra de Arte que deseja roubar
    if (verificarSeExisteElementoNaMatriz(Museo, (linhaInicial + 1), colunaInicial)):
        if (Museo[linhaInicial + 1][colunaInicial] == 10):
            saida = True
            break
    if (verificarSeExisteElementoNaMatriz(Museo, linhaInicial, (colunaInicial + 1))):
        if (Museo[linhaInicial][colunaInicial + 1] == 10):
            saida = True
            break
    if (verificarSeExisteElementoNaMatriz(Museo, (linhaInicial - 1), colunaInicial)):
        if (Museo[linhaInicial - 1][colunaInicial] == 10):
            saida = True
            break
    if (verificarSeExisteElementoNaMatriz(Museo, linhaInicial, (colunaInicial - 1))):
        if (Museo[linhaInicial][colunaInicial - 1] == 10):
            saida = True
            break


    # Fazendo o ladrão andar pelo Museo
    if (verficarOsPossiveisCaminhosAndados(Museo, (linhaInicial + 1), colunaInicial, pilha)):
        # print("Ponto Origem - Matriz[{}][{}]".format(linhaInicial, colunaInicial))
        pilha.append([linhaInicial, colunaInicial])
        linhaInicial = linhaInicial + 1
        Museo[linhaInicial][colunaInicial] = "X"
        # print("Ponto Destino - Matriz[{}][{}]: {}\n".format(linhaInicial, colunaInicial, Museo[linhaInicial][colunaInicial]))
    elif (verficarOsPossiveisCaminhosAndados(Museo, linhaInicial, (colunaInicial + 1), pilha)):
        # print("Ponto Origem - Matriz[{}][{}]".format(linhaInicial, colunaInicial))
        pilha.append([linhaInicial, colunaInicial])
        colunaInicial = colunaInicial + 1
        Museo[linhaInicial][colunaInicial] = "X"
        # print("Ponto Destino - Matriz[{}][{}]: {}\n".format(linhaInicial, colunaInicial,Museo[linhaInicial][colunaInicial]))
    elif (verficarOsPossiveisCaminhosAndados(Museo, (linhaInicial - 1), colunaInicial, pilha)):
        # print("Ponto Origem - Matriz[{}][{}]".format(linhaInicial, colunaInicial))
        pilha.append([linhaInicial, colunaInicial])
        linhaInicial = linhaInicial - 1
        Museo[linhaInicial][colunaInicial] = "X"
        # print("Ponto Destino - Matriz[{}][{}]: {}\n".format(linhaInicial, colunaInicial, Museo[linhaInicial][colunaInicial]))
    elif (verficarOsPossiveisCaminhosAndados(Museo, linhaInicial, (colunaInicial - 1), pilha)):
        # print("Ponto Origem - Matriz[{}][{}]".format(linhaInicial, colunaInicial))
        pilha.append([linhaInicial, colunaInicial])
        colunaInicial = colunaInicial - 1
        Museo[linhaInicial][colunaInicial] = "X"
        # print("Ponto Destino - Matriz[{}][{}]: {}\n".format(linhaInicial, colunaInicial,Museo[linhaInicial][colunaInicial]))
    else:
       if (len(pilha) == 0):
           break
       else:
            linhaInicial = pilha[len(pilha)-1][0]
            colunaInicial = pilha[len(pilha)-1][1]
            pilha.pop(len(pilha)-1)

if (saida):
    print("\nO Ladrão vai conseguir roubar a Obra de arte")
else:
    print("\nO Ladrão não vai conseguir roubar a Obra de arte")

# Desenhando o grafo
''' nx.draw(grafico, with_labels=True, font_weight="bold", node_color="blue")
plt.savefig("simple_path.png")
plt.show() '''





