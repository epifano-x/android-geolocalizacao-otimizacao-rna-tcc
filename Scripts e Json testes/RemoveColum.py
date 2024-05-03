import json

# Função para remover os campos especificados de cada objeto dentro de uma lista
def remover_campos(dados):
    for dado in dados:
        if 'gnss_data' in dado:
            gnss_data = dado['gnss_data']
            if 'pontoselecionado' in gnss_data:
                del gnss_data['pontoselecionado']
            if 'latitudereal' in gnss_data:
                del gnss_data['latitudereal']
            if 'longitudereal' in gnss_data:
                del gnss_data['longitudereal']
            if 'gnss_data_json' in gnss_data:
                satellites = gnss_data['gnss_data_json'].get('satellites', [])
                del gnss_data['gnss_data_json']
                gnss_data['satellites'] = satellites

# Ler o arquivo JSON
with open("dados_com_diferencas.json", "r") as arquivo_json:
    dados = json.load(arquivo_json)

# Remover os campos especificados de cada objeto dentro da lista
remover_campos(dados)

# Escrever os dados modificados de volta para o arquivo JSON
with open("dados_removido.json", "w") as arquivo_json_modificado:
    json.dump(dados, arquivo_json_modificado, indent=4)
