import mysql.connector

def conectar_banco():
    """Conecta com o banco autocharm"""
    try:
        conexao = mysql.connector.connect(
            host="localhost",      # Servidor do MySQL
            user="root",          # Usuário padrão do XAMPP  
            password="",          # Senha (vazia no XAMPP por padrão)
            database="autocharm"  # Nome do seu banco
        )
        print("Conectado ao banco autocharm!")
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar: {erro}")
        return None

# Função para testar a conexão
if __name__ == "__main__":
    conexao = conectar_banco()
    if conexao:
        # Testar listando as tabelas
        cursor = conexao.cursor()
        cursor.execute("SHOW TABLES")
        tabelas = cursor.fetchall()
        
        print("\n Tabelas no banco autocharm:")
        for tabela in tabelas:
            print(f" - {tabela[0]}")
        
        cursor.close()
        conexao.close()
        print("\n Conexão testada com sucesso!")