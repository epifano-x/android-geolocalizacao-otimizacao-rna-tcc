import json
import matplotlib.pyplot as plt

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

# Plotar dispersão da latitude em relação ao timestamp
plt.figure(figsize=(8, 6))
plt.scatter(timestamps, latitudes, color='red', alpha=0.5)
plt.title('Dispersão da Latitude em relação ao Timestamp')
plt.xlabel('Timestamp')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()

# Plotar dispersão da longitude em relação ao timestamp
plt.figure(figsize=(8, 6))
plt.scatter(timestamps, longitudes, color='green', alpha=0.5)
plt.title('Dispersão da Longitude em relação ao Timestamp')
plt.xlabel('Timestamp')
plt.ylabel('Longitude')
plt.grid(True)
plt.show()
