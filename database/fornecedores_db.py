from conexao_db import conectar_banco

#CADASTRAR FORNECEDORES NO BANCO DE DADOS
class FornecedorDB:
    @staticmethod
    def inserir_fornecedor(nome, cnpj, telefone):
        """Insere fornecedor"""
        conexao = conectar_banco()  
        if conexao:
            try:
                cursor = conexao.cursor()
                sql = "INSERT INTO fornecedores (nome, cnpj, telefone) VALUES (%s, %s, %s)"
                valores = (nome, cnpj, telefone)
                cursor.execute(sql, valores)
                conexao.commit()
                return True, "Fornecedor inserido com sucesso"
            except Exception as e:  
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"
    
    #BUSCAR FORNECEDORES NO BANCO
    @staticmethod
    def buscar_fornecedores():
        """Busca todos os fornecedores"""
        conexao = conectar_banco()
        if conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute("SELECT * FROM fornecedores")  
                fornecedores = cursor.fetchall()
                return True, fornecedores
            except Exception as e:
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"