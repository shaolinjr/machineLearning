import csv

def carregar_acessos ():

    X = [] # array com as features(caracteristicas dos dados)
    y = [] # vetor com os valores esperados

    arquivo = open('acesso_pagina.csv','r+')

    reader = csv.reader(arquivo)

    next(arquivo) #utilizamos o next para pular a primeira linha, que corresponde ao nome das colunas

    #colocar os valores em seus respectivos arrays

    for home, como_funciona, contato, comprou in reader:
        X.append([int(home),int(como_funciona), int(contato)])
        y.append(int(comprou))

    return X, y

    