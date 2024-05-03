import json
import datetime

def converter_timestamp(timestamp):
    # Converter o timestamp para um objeto datetime
    data_hora = datetime.datetime.fromtimestamp(timestamp / 1000)  # Dividido por 1000 para converter de milissegundos para segundos
    # Calcular o número de minutos desde o início do dia
    minutos_do_dia = data_hora.hour * 60 + data_hora.minute
    # Normalizar os minutos do dia para o intervalo de 0 a 1
    minutos_normalizados = minutos_do_dia / (24 * 60)  # 24 horas * 60 minutos
    return minutos_normalizados

# Carregar os dados do arquivo JSON
with open("dados_removido.json", "r") as arquivo_json:
    dados_json = json.load(arquivo_json)

# Converter os timestamps
for dado in dados_json:
    if 'gnss_data' in dado:
        gnss_data = dado['gnss_data']
        if 'timestamp' in gnss_data:
            gnss_data['timestamp'] = converter_timestamp(gnss_data['timestamp'])

# Salvar os dados modificados em um novo arquivo JSON
with open("dados_timestamp_normalizado.json", "w") as arquivo_json_normalizado:
    json.dump(dados_json, arquivo_json_normalizado, indent=4)
