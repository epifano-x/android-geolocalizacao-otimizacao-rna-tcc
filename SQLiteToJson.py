import sqlite3
import json

# Conecte-se ao banco de dados SQLite
conexao = sqlite3.connect("AllDataBase.db")
cursor = conexao.cursor()

# Lista para armazenar os dados convertidos
dados_json = []

# Itere sobre as tabelas e extraia os dados
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tabelas = cursor.fetchall()
for tabela in tabelas:
    nome_tabela = tabela[0]
    cursor.execute("SELECT * FROM {}".format(nome_tabela))
    dados_tabela = cursor.fetchall()

    # Crie um dicionário com os dados da tabela e adicione à lista
    for linha in dados_tabela:
        dicionario_linha = dict(zip([coluna[0] for coluna in cursor.description], linha))
        dados_json.append({nome_tabela: dicionario_linha})

# Salve os dados em um arquivo JSON
with open("dados.json", "w") as arquivo_json:
    json.dump(dados_json, arquivo_json, indent=4)

# Feche a conexão com o banco de dados SQLite
conexao.close()
