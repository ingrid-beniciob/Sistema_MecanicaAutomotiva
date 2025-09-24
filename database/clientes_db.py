from conexao_db import conectar_banco  

#INSERIR CLIENTE NO BANCO DE DADOS
class ClienteDB:
    @staticmethod
    def inserir_cliente(nome, contato, endereco, cpf):
        """Insere cliente na tabela CLIENTE"""
        conexao = conectar_banco()  
        if conexao:
            try:
                cursor = conexao.cursor()
               
                sql = "INSERT INTO cliente (nome, contato, endereco, cpf) VALUES (%s, %s, %s, %s)"
                valores = (nome, contato, endereco, cpf)
                cursor.execute(sql, valores)
                conexao.commit()
                return True, "Cliente inserido com sucesso"
            except Exception as e:  
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"
    
    #BUSCAR CLIENTE NO BANCO DE DADOS
    @staticmethod
    def buscar_clientes():
        """Busca todos os clientes"""
        conexao = conectar_banco()
        if conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute("SELECT * FROM cliente")  
                clientes = cursor.fetchall()
                return True, clientes
            except Exception as e:
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"