from conexao_db import conectar_banco

class ContasDB:
    
    # INSERIR CONTA (Receber ou Pagar)
    @staticmethod
    def inserir_conta(tipo, descricao, valor, vencimento, forma_pagamento='Dinheiro', cliente_id=None):
        conexao = conectar_banco()  
        if conexao:
            try:
                cursor = conexao.cursor()
                sql = """INSERT INTO contas 
                         (tipo, descricao, valor, vencimento, forma_pagamento, cliente_id) 
                         VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                valores = (tipo, descricao, valor, vencimento, forma_pagamento, cliente_id)
                cursor.execute(sql, valores)
                conexao.commit()
                return True, "Conta inserida com sucesso"
            except Exception as e:  
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"
    
    # BUSCAR TODAS AS CONTAS (para a tela principal)
    @staticmethod
    def buscar_contas(filtro_tipo=None, filtro_status=None, data_inicio=None, data_fim=None, busca_texto=None):
        conexao = conectar_banco()
        if conexao:
            try:
                cursor = conexao.cursor()
                
                # Query base
                sql = "SELECT * FROM contas WHERE 1=1"
                valores = []
                
                # Aplicar filtros
                if filtro_tipo:
                    sql += " AND tipo = %s"
                    valores.append(filtro_tipo)
                
                if filtro_status:
                    sql += " AND status = %s"
                    valores.append(filtro_status)
                
                if data_inicio:
                    sql += " AND vencimento >= %s"
                    valores.append(data_inicio)
                
                if data_fim:
                    sql += " AND vencimento <= %s"
                    valores.append(data_fim)
                
                if busca_texto:
                    sql += " AND descricao LIKE %s"
                    valores.append(f'%{busca_texto}%')
                
                # Ordenar por vencimento
                sql += " ORDER BY vencimento ASC"
                
                cursor.execute(sql, valores)
                contas = cursor.fetchall()
                return True, contas
                
            except Exception as e:
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"
    
    # MARCAR CONTA COMO PAGA/RECEBIDA
    @staticmethod
    def atualizar_status(conta_id, novo_status):
        conexao = conectar_banco()
        if conexao:
            try:
                cursor = conexao.cursor()
                sql = "UPDATE contas SET status = %s WHERE id = %s"
                cursor.execute(sql, (novo_status, conta_id))
                conexao.commit()
                return True, "Status atualizado com sucesso"
            except Exception as e:  
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"