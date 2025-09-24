from conexao_db import conectar_banco

#INSERIR ITEM NO ESTOQUE
class EstoqueDB:
    @staticmethod
    def inserir_item_estoque(nome, quantidade, preco, fornecedor_id=None):
        """Insere item no estoque"""
        conexao = conectar_banco()  
        if conexao:
            try:
                cursor = conexao.cursor()
                sql = "INSERT INTO estoque (nome, quantidade, preco, fornecedor_id) VALUES (%s, %s, %s, %s)"
                valores = (nome, quantidade, preco, fornecedor_id)
                cursor.execute(sql, valores)
                conexao.commit()
                return True, "Item inserido no estoque com sucesso"
            except Exception as e:  
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"
    
    #BUSCAR NO ESTOQUE
    @staticmethod
    def buscar_estoque():
        """Busca todos os itens do estoque"""
        conexao = conectar_banco()
        if conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute("SELECT * FROM estoque")  
                itens = cursor.fetchall()
                return True, itens
            except Exception as e:
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"
    
    #ATUALIZAR QUANTIDADE DO ESTOQUE
    @staticmethod
    def atualizar_quantidade(item_id, nova_quantidade):
        """Atualiza quantidade do item no estoque"""
        conexao = conectar_banco()
        if conexao:
            try:
                cursor = conexao.cursor()
                sql = "UPDATE estoque SET quantidade = %s WHERE id = %s"
                valores = (nova_quantidade, item_id)
                cursor.execute(sql, valores)
                conexao.commit()
                return True, "Quantidade atualizada com sucesso"
            except Exception as e:  
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"