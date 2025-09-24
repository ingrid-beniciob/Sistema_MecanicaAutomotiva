from conexao_db import conectar_banco

#CADASTRAR VEÍCULO NO BANCO
class VeiculoDB:
    @staticmethod
    def inserir_veiculo(cliente_id, marca, modelo, ano, placa):
        """Insere veículo na tabela VEICULOS"""
        conexao = conectar_banco()  
        if conexao:
            try:
                cursor = conexao.cursor()
                sql = "INSERT INTO veiculos (cliente_id, marca, modelo, ano, placa) VALUES (%s, %s, %s, %s, %s)"
                valores = (cliente_id, marca, modelo, ano, placa)
                cursor.execute(sql, valores)
                conexao.commit()
                return True, "Veículo inserido com sucesso"
            except Exception as e:  
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"
    

    #BUSCAR VEÍCULOS CADASTRADOS
    @staticmethod
    def buscar_veiculos():
        """Busca todos os veículos"""
        conexao = conectar_banco()
        if conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute("SELECT * FROM veiculos")  
                veiculos = cursor.fetchall()
                return True, veiculos
            except Exception as e:
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"
    

    #BUCSAR VEÍCULOS POR CLIENTE 
    @staticmethod
    def buscar_veiculos_por_cliente(cliente_id):
        """Busca veículos de um cliente específico"""
        conexao = conectar_banco()
        if conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute("SELECT * FROM veiculos WHERE cliente_id = %s", (cliente_id,))  
                veiculos = cursor.fetchall()
                return True, veiculos
            except Exception as e:
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"