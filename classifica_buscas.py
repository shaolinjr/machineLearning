import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from collections import Counter

# usando pandas para facilitar organizacao dos dados

df = pd.read_csv('buscas.csv') # nosso DataFrame, nossa 'tabela' de dados

# Pegando e separando nossas colunas entre as features(X) e nossos resultados (y)
X_df = df[['home','busca','logado']]
y_df = df ['comprou']

# Temos que transformar a coluna de busca, que é uma variavel categórica e transformar em 3 colunas (chamadas dummies)

Xdummies_df = pd.get_dummies(X_df)
ydummies_df = y_df # não é necessário, mas para seguir o padrão iremos fazer dessa forma

# Nosso metodo modelo.fit do sklearn utiliza dois arrays, o de X e o y. E o que nós temos são dois dataframes,
# por isso é necessária a conversão para arrays:

X = Xdummies_df.values
y = ydummies_df.values

# Separação de dados para treino e para teste

# Treino = 90% da lista
porcentagem_treino = 0.9

tamanho_treino = int(porcentagem_treino * len(X)) # queremos 90% dos dados para treino
tamanho_teste  = int(len(X) - tamanho_treino) # o restante dos dados será para teste

X_treino = X[:tamanho_treino]
y_treino = y[:tamanho_treino]

# Teste = 10%

X_teste = X[-tamanho_teste:]
y_teste = y[-tamanho_teste:]


# Agora iremos treinar nossos dados com o modelo do sklearn MultinomialNB

modelo = MultinomialNB()
modelo.fit(X_treino, y_treino) # treino de acordo com os dados

# Iremos tentar prever os resultados para em seguida verificar a quantidade de acertos
resultado = modelo.predict(X_teste)

acertos   = (resultado == y_teste)
total_acertos = sum(acertos)
total_elementos = len(X_teste)

taxa_acerto = 100.0 * total_acertos / total_elementos

# Como saber se nosso algoritmo de ML está se saindo bem?

# acertos_um = sum(y) #pegamos todos os casos '1', como se o algoritmo chutasse tudo '1'
#acertos_zero = len(y) - acertos_um # fazemos o mesmo para o '0'
# acertos_um = len(y[y==1])
# acertos_zero = len(y[y==0])

acertos_base = max(Counter(y).values()) # O Counter faz o papel de separacao dos valores e com o max pegamos o maior valor

taxa_acerto_base = 100* acertos_base / len(y) #pegamos o maior valor para comparação e depois transformamos em %

print ("Taxa de acerto algoritmo: %.2f%%" % taxa_acerto)
print("Taxa de acerto base: %.2f%%" % taxa_acerto_base)
print("Total de elementos no teste: %d" % total_elementos)


