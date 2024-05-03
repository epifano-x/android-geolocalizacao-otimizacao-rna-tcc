import json

# Função para remover os campos especificados de cada objeto dentro de uma lista
def remover_campos(dados):
    for dado in dados:
        if 'gnss_data' in dado:
            gnss_data = dado['gnss_data']
            if 'latitude' in gnss_data:
                del gnss_data['latitude']
            if 'longitude' in gnss_data:
                del gnss_data['longitude']

# Ler o arquivo JSON
with open("dados_timestamp_normalizado.json", "r") as arquivo_json:
    dados = json.load(arquivo_json)

# Remover os campos especificados de cada objeto dentro da lista
remover_campos(dados)

# Escrever os dados modificados de volta para o arquivo JSON
with open("dados_final.json", "w") as arquivo_json_modificado:
    json.dump(dados, arquivo_json_modificado, indent=4)
