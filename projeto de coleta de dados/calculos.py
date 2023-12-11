import sqlite3
import numpy as np

# Conectar ao banco de dados
conn = sqlite3.connect('fortnite_data.db')
cursor = conn.cursor()

# Extrair os dados e remover linhas com valores nulos
cursor.execute('SELECT vitorias, kills, partidas FROM jogadores')
data = cursor.fetchall()
data = [row for row in data if all(x is not None for x in row)]

# Fechar a conexão com o banco de dados
conn.close()

# Converter os dados para arrays NumPy
data = np.array(data)

# Calcular as medidas estatísticas
media = np.mean(data, axis=0)
mediana = np.median(data, axis=0)
desvio_padrao = np.std(data, axis=0)
minimo = np.min(data, axis=0)
maximo = np.max(data, axis=0)

print("Métrica\tMédia\tMediana\tDesvio Padrão\tMínimo\tMáximo")
print("Vitórias\t{}\t{}\t{}\t{}\t{}".format(media[0], mediana[0], desvio_padrao[0], minimo[0], maximo[0]))
print("Kills\t{}\t{}\t{}\t{}\t{}".format(media[1], mediana[1], desvio_padrao[1], minimo[1], maximo[1]))
print("Partidas\t{}\t{}\t{}\t{}\t{}".format(media[2], mediana[2], desvio_padrao[2], minimo[2], maximo[2]))
