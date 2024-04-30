import json
import matplotlib.pyplot as plt
import numpy as np

# Carregar dados do JSON
with open('dados_final.json', 'r') as f:
    data = json.load(f)

# Extrair latitude, longitude e timestamps
latitudes = []
longitudes = []
timestamps = []
for item in data:
    latitudes.append(item['gnss_data']['latitudeDiferenca'])
    longitudes.append(item['gnss_data']['longitudeDiferenca'])
    timestamps.append(item['gnss_data']['timestamp'])

# Determinar as cores dos pontos com base no timestamp
cores = ['blue' if timestamp < 0.5 else 'red' for timestamp in timestamps]

# Plotar dispersão de latitude e longitude
plt.figure(figsize=(8, 6))
plt.scatter(longitudes, latitudes, c=cores, alpha=0.5)
plt.title('Dispersão de Latitude e Longitude com Cores Baseadas no Timestamp')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Adicionar legenda de cores
azul_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Timestamp < 0.5')
vermelho_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Timestamp > 0.5')
plt.legend(handles=[azul_patch, vermelho_patch])

plt.grid(True)
plt.show()
