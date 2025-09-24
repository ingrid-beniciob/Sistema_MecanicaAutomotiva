from conexao_db import conectar_banco

#CADASTRAR FUNCIONÁRIOS
class FuncionarioDB:
    @staticmethod
    def inserir_funcionario(nome, cargo, data_aniversario, cpf):
        """Insere funcionário"""
        conexao = conectar_banco()  
        if conexao:
            try:
                cursor = conexao.cursor()
                sql = "INSERT INTO funcionarios (nome, cargo, data_aniversario, cpf) VALUES (%s, %s, %s, %s)"
                valores = (nome, cargo, data_aniversario, cpf)
                cursor.execute(sql, valores)
                conexao.commit()
                return True, "Funcionário inserido com sucesso"
            except Exception as e:  
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"
    
    #BUSCAR FUNCIONÁRIOS CADASTRADOS
    @staticmethod
    def buscar_funcionarios():
        """Busca todos os funcionários"""
        conexao = conectar_banco()
        if conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute("SELECT * FROM funcionarios")  
                funcionarios = cursor.fetchall()
                return True, funcionarios
            except Exception as e:
                return False, f"Erro no banco: {e}"
            finally:
                cursor.close()
                conexao.close()
        return False, "Erro de conexão"