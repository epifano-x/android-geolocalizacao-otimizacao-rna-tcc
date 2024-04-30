import json
import matplotlib.pyplot as plt

# Carregar dados do JSON
with open('dados_final.json', 'r') as f:
    data = json.load(f)

# Extrair latitude e longitude
latitudes = []
longitudes = []
for item in data:
    latitudes.append(item['gnss_data']['latitudeDiferenca'])
    longitudes.append(item['gnss_data']['longitudeDiferenca'])

# Plotar dispersão de latitude e longitude
plt.figure(figsize=(8, 6))
plt.scatter(longitudes, latitudes, color='blue', alpha=0.5)
plt.title('Dispersão de Latitude e Longitude')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()
