import json
import utm

# Abrir o arquivo JSON original
with open("dados_com_diferencas.json", "r") as arquivo_json:
    dados = json.load(arquivo_json)

# Iterar sobre os dados
for dado in dados:
    if 'gnss_data' in dado:
        gnss_data = dado['gnss_data']
        # Coordenadas coletadas por você (convertidas para UTM)
        latitude_coletada = float(gnss_data['latitude'])
        longitude_coletada = float(gnss_data['longitude'])
        latitude_utm_coletada, longitude_utm_coletada, _, _ = utm.from_latlon(latitude_coletada, longitude_coletada)
        
        # Coordenadas reais (convertidas para UTM)
        latitudereal = float(gnss_data['latitudereal'])
        longitudereal = float(gnss_data['longitudereal'])
        latitude_utm_real, longitude_utm_real, _, _ = utm.from_latlon(latitudereal, longitudereal)
        
        # Calcular a diferença em metros
        latitude_diferenca_m = latitude_utm_coletada - latitude_utm_real
        longitude_diferenca_m = longitude_utm_coletada - longitude_utm_real
        
        # Atualizar os valores no dicionário
        gnss_data['latitudeDiferencaMetros'] = latitude_diferenca_m
        gnss_data['longitudeDiferencaMetros'] = longitude_diferenca_m

# Salvar os dados ajustados em um novo arquivo JSON
with open("dados_diferenca_em_metros.json", "w") as arquivo_json_diferenca:
    json.dump(dados, arquivo_json_diferenca, indent=4)
