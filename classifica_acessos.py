from dados import carregar_acessos
from sklearn.naive_bayes import MultinomialNB

X,y = carregar_acessos() #nossos dois arrays de dados do csv

# Separação dos dados entre array de teste e array de treino

# Treino = ≈90% da lista

X_treino = X[:90]
y_treino = y[:90]

# Teste = ≈10%

X_teste = X[-9:]
y_teste = y[-9:]


modelo = MultinomialNB()

# Adequando os dados de treino
modelo.fit(X_treino, y_treino)

# Predict de acordo com os dados de teste

resultado = modelo.predict(X_teste)

diferenca = resultado - y_teste #  diferenca entre o que foi encontrado como resposta e o que deveria ser encontrado

acertos = [d for d in diferenca if d == 0]

# Calcular a taxa de acerto do algoritmo
total_de_acertos = len(acertos)
total_de_elementos = len(X_teste)

taxa_de_acertos = 100.0 * total_de_acertos / total_de_elementos


print(taxa_de_acertos)






