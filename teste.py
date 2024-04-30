import os
import datetime

# Diretório do seu repositório
repo_dir = "/caminho/para/seu/repo"

# Arquivo a ser editado e commitado
file_path = os.path.join(repo_dir, "seu_arquivo.txt")

# Data inicial para os commits
start_date = datetime.datetime(2023, 4, 21)  # Data de hoje, um ano atrás

# Data final para os commits
end_date = start_date + datetime.timedelta(days=365)  # Um ano a partir da data inicial

# Loop para fazer os commits diários
current_date = start_date
while current_date <= end_date:
    # Edite o arquivo como quiser
    with open(file_path, "a") as file:
        file.write(f"\nCommit em {current_date.strftime('%Y-%m-%d')}")

    # Adicione as mudanças ao git
    os.system(f"cd {repo_dir} && git add {file_path}")

    # Faça o commit com a data atual
    os.system(f"cd {repo_dir} && GIT_AUTHOR_DATE='{current_date.isoformat()}' GIT_COMMITTER_DATE='{current_date.isoformat()}' git commit -m 'Commit em {current_date.strftime('%Y-%m-%d')} - Automatizado'")

    # Avance para o próximo dia
    current_date += datetime.timedelta(days=1)
