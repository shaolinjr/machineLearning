from sklearn.naive_bayes import MultinomialNB

# Nossos dados
# E gordinho, tem perninha curta, faz au au
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro4 = [1, 1, 1]
cachorro5 = [0, 1, 1]
cachorro6 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro4, cachorro5, cachorro6]

marcacoes = [1,1,1, -1,-1,-1]

modelo = MultinomialNB()

#Temos que encaixar nossos dados com nossas marcações no modelo

modelo.fit(dados,marcacoes)

#Testando funcionamento!

teste1 = [1,1,1] # cachorro
teste2 = [0,1,0] #porco
teste3 = [0,0,1] # cachorro

testes = [teste1,teste2, teste3]
marcacoes_testes = [-1, 1, -1]

resultado = modelo.predict(testes)
#calcular taxa de acerto
# diferenca = valores encontrados(marcacoes) - marcacoes_corretas

diferencas = resultado - marcacoes_testes

acertos = [d for d in diferencas if d == 0]

total_acertos = len(acertos)
total_elementos = len(testes)

taxa_acerto = 100.0 * total_acertos / total_elementos

print ("Resultado: "+ str(resultado))
print("Diferencas: "+ str(diferencas))
print ("Taxa de acerto: %.2f%%" % (taxa_acerto) )