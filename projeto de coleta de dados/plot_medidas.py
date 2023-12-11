import numpy as np
import matplotlib.pyplot as plt

# Dados das medidas
metricas = ["Vitórias", "Kills", "Partidas"]
media = [926.69, 13849.0, 1386.3]
mediana = [873.0, 12787.5, 1334.0]
desvio_padrao = [240.74, 3464.46, 198.68]

# Índice para as métricas
indices = np.arange(len(metricas))

# Largura das barras
largura = 0.35

# Criar as barras para média, mediana e desvio padrão
plt.bar(indices, media, largura, label='Média', color='b', alpha=0.7)
plt.bar(indices + largura, mediana, largura, label='Mediana', color='g', alpha=0.7)
plt.bar(indices + 2 * largura, desvio_padrao, largura, label='Desvio Padrão', color='r', alpha=0.7)

# Configurações do gráfico
plt.xlabel('Métricas')
plt.ylabel('Valores')
plt.title('Medidas Estatísticas')
plt.xticks(indices + largura, metricas)
plt.legend()

# Exibir o gráfico
plt.tight_layout()
plt.show()
