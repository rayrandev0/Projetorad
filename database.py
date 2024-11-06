import sqlite3
from dotenv import load_dotenv
import os

# Carregar as variáveis do arquivo .env
load_dotenv()

# Obter o nome do banco de dados a partir do .env
DATABASE_NAME = os.getenv("DATABASE_NAME", "rede_social.db")

# Criar a conexão com o banco de dados
def create_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

# Criar as tabelas no banco de dados
def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            data_nascimento TEXT NOT NULL
        )
    ''')



    # Tabela de amigos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS amigos (
            id_usuario1 INTEGER,
            id_usuario2 INTEGER,
            status TEXT NOT NULL,
            FOREIGN KEY (id_usuario1) REFERENCES usuarios(id),
            FOREIGN KEY (id_usuario2) REFERENCES usuarios(id)
        )
    ''')

    # Tabela de postagens
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS postagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER,
            titulo TEXT,
            conteudo TEXT,
            data_postagem TEXT,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print(f"Banco de dados {DATABASE_NAME} e tabelas criados com sucesso!")

