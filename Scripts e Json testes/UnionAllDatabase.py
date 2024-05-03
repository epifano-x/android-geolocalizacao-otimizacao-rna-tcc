import sqlite3
import os

# Crie um novo banco de dados
novo_banco_dados = "AllDataBase.db"
conexao = sqlite3.connect(novo_banco_dados)
cursor = conexao.cursor()

# Itere sobre os 8 bancos de dados separados
bancos_de_dados_separados = ["1.db", "2.db", "3.db", "4.db", "5.db", "6.db", "7.db", "8.db"]
for banco in bancos_de_dados_separados:
    # Conecte-se ao banco de dados separado
    conexao_separada = sqlite3.connect(banco)
    cursor_separado = conexao_separada.cursor()

    # Extraia o esquema da tabela
    cursor_separado.execute("SELECT name, sql FROM sqlite_master WHERE type='table'")
    tabelas = cursor_separado.fetchall()

    # Copie os dados da tabela para o novo banco de dados
    for tabela in tabelas:
        tabela_nome, tabela_sql = tabela
        # Verifique se o nome da tabela não é "sqlite_sequence"
        if tabela_nome != "sqlite_sequence":
            dados = cursor_separado.execute("SELECT * FROM {}".format(tabela_nome)).fetchall()
            cursor.execute("CREATE TABLE IF NOT EXISTS {} ({})".format(tabela_nome, tabela_sql.split("(")[1].replace(")", "")))
            cursor.executemany("INSERT INTO {} VALUES ({})".format(tabela_nome, ','.join(['?']*len(dados[0]))), dados)

    # Feche a conexão com o banco de dados separado
    conexao_separada.close()

# Salve as alterações e feche a conexão com o novo banco de dados
conexao.commit()
conexao.close()
