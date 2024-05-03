import json
from decimal import Decimal, ROUND_HALF_UP

# Abrir o arquivo JSON
with open("dados_ajustados.json", "r") as arquivo_json:
    dados = json.load(arquivo_json)

# Iterar sobre os dados e calcular a diferença entre 'latitude' e 'latitudereal'
# e entre 'longitude' e 'longitudereal'
for dado in dados:
    if 'gnss_data' in dado:
        # Calcular a diferença entre 'latitude' e 'latitudereal'
        latitude_diferenca = dado['gnss_data']['latitude'] - dado['gnss_data']['latitudereal']
        # Calcular a diferença entre 'longitude' e 'longitudereal'
        longitude_diferenca = dado['gnss_data']['longitude'] - dado['gnss_data']['longitudereal']
        # Converter os valores para strings com a precisão desejada
        dado['gnss_data']['latitudeDiferenca'] = float(latitude_diferenca)
        dado['gnss_data']['longitudeDiferenca'] = float(longitude_diferenca)

# Mover os campos 'latitudeDiferenca' e 'longitudeDiferenca' para cima do campo 'gnss_data_json'
for dado in dados:
    if 'gnss_data' in dado:
        gnss_data = dado['gnss_data']
        # Salvar os campos 'latitudeDiferenca' e 'longitudeDiferenca' temporariamente
        latitude_diferenca = gnss_data.pop('latitudeDiferenca')
        longitude_diferenca = gnss_data.pop('longitudeDiferenca')
        # Mover os campos para a posição desejada
        gnss_data_json = gnss_data.pop('gnss_data_json')
        gnss_data['latitudeDiferenca'] = latitude_diferenca
        gnss_data['longitudeDiferenca'] = longitude_diferenca
        gnss_data['gnss_data_json'] = gnss_data_json

# Salvar os dados ajustados em um novo arquivo JSON
with open("dados_com_diferencas.json", "w") as arquivo_json_ajustado:
    json.dump(dados, arquivo_json_ajustado, indent=4)
