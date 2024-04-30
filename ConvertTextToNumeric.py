import json

# Abrir o arquivo JSON
with open("dados_limpos.json", "r") as arquivo_json:
    dados = json.load(arquivo_json)

# Iterar sobre os dados e ajustar os campos 'latitude' e 'longitude'
for dado in dados:
    if 'gnss_data' in dado:
        # Converter os valores dos campos 'latitudereal' e 'longitudereal' para float
        latitudereal = float(dado['gnss_data']['latitudereal'])
        longitudereal = float(dado['gnss_data']['longitudereal'])
        # Atribuir os valores convertidos aos campos 'latitudereal' e 'longitudereal'
        dado['gnss_data']['latitudereal'] = latitudereal
        dado['gnss_data']['longitudereal'] = longitudereal

# Salvar os dados ajustados em um novo arquivo JSON
with open("dados_ajustados.json", "w") as arquivo_json_ajustado:
    json.dump(dados, arquivo_json_ajustado, indent=4)
