from conexao_db import conectar_banco

#CRIAR ORDEM DE SERVIÇO E CADASTRAR NO BANCO
class OrdemServicoDB:
    @staticmethod
    def criar_ordem_servico(cliente_id, veiculo_id, descricao, valor_total, status='A iniciar'):
        """Cria nova ordem de serviço"""
        conexao = conectar_banco()  
        if conexao:
            try:
                cursor = conexao.cursor()
                sql = """INSERT INTO ordens_servico 
                         (cliente_id, veiculo_id, descricao, valor_total, status) 
                         VALUES (%s, %s, %s, %s, %s)"""
                valores = (cliente_id, veiculo_id, descricao, valor_total, status)
                cursor.execute(sql, valores)
                conexao.commit()
                return True, "Ordem de serviço criada com sucesso"
            except Exception as e:  
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"
    
    #BUSCAR ORDEM DE SERVIÇO
    @staticmethod
    def buscar_ordens_servico():
        """Busca todas as ordens de serviço"""
        conexao = conectar_banco()
        if conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute("SELECT * FROM ordens_servico")  
                ordens = cursor.fetchall()
                return True, ordens
            except Exception as e:
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"
     
    #ATUALIZAR ORDEM DE SERVIÇO
    @staticmethod
    def atualizar_status_ordem(ordem_id, novo_status):
        """Atualiza status da ordem de serviço"""
        conexao = conectar_banco()
        if conexao:
            try:
                cursor = conexao.cursor()
                sql = "UPDATE ordens_servico SET status = %s WHERE id = %s"
                valores = (novo_status, ordem_id)
                cursor.execute(sql, valores)
                conexao.commit()
                return True, "Status atualizado com sucesso"
            except Exception as e:  
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"