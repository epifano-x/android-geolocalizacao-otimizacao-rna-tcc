import json

# Abrir o arquivo JSON
with open("dados.json", "r") as arquivo_json:
    dados = json.load(arquivo_json)

# Iterar sobre os dados e limpar o campo 'gnss_data_json'
for dado in dados:
    if 'gnss_data' in dado:
        # Verificar se 'gnss_data_json' está presente e é uma string
        if 'gnss_data_json' in dado['gnss_data'] and isinstance(dado['gnss_data']['gnss_data_json'], str):
            # Converter a string em um objeto JSON
            gnss_data_json_objeto = json.loads(dado['gnss_data']['gnss_data_json'])
            # Atualizar o campo 'gnss_data_json' com o objeto JSON
            dado['gnss_data']['gnss_data_json'] = gnss_data_json_objeto

# Salvar os dados limpos em um novo arquivo JSON
with open("dados_limpos.json", "w") as arquivo_json_limpo:
    json.dump(dados, arquivo_json_limpo, indent=4)
