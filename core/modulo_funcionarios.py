# MÓDULO DE GERENCIAMENTO DE FUNCIONÁRIOS
import sys
import os

# Configurar caminho de importação
caminho_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(caminho_base)

# Adiciona explicitamente a pasta database
caminho_database = os.path.join(caminho_base, 'database')
sys.path.append(caminho_database)

from database.funcionarios_db import FuncionarioDB
from utils.helpers import limpar_tela, aguardar_enter, input_int

class MenuFuncionarios:
    
    def executar(self):
        while True:
            limpar_tela()
            print("=" * 40)
            print("    GERENCIAR FUNCIONÁRIOS")
            print("=" * 40)
            print("1. Cadastrar Funcionário")
            print("2. Listar Funcionários")
            print("3. Voltar ao Menu Principal")
            print("=" * 40)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.cadastrar_funcionario()
            elif opcao == "2":
                self.listar_funcionarios()
            elif opcao == "3":
                break
            else:
                print("Opção inválida!")
                aguardar_enter()
    
    def cadastrar_funcionario(self):
        limpar_tela()
        print("CADASTRAR FUNCIONÁRIO")
        print("-" * 30)
        
        nome = input("Nome: ").strip()
        cargo = input("Cargo: ").strip()
        data_aniversario = input("Data de aniversário (YYYY-MM-DD): ").strip()
        cpf = input("CPF (apenas números): ").strip()
        
        if not nome or not cargo or not data_aniversario or not cpf:
            print("Todos os campos são obrigatórios!")
            aguardar_enter()
            return
        
        if not cpf.isdigit():
            print("CPF deve conter apenas números!")
            aguardar_enter()
            return
        
        try:
            sucesso, mensagem = FuncionarioDB.inserir_funcionario(nome, cargo, data_aniversario, cpf)
            print(mensagem)
        except Exception as e:
            print(f"Erro ao cadastrar funcionário: {e}")
        
        aguardar_enter()
    
    def listar_funcionarios(self):
        limpar_tela()
        print("LISTA DE FUNCIONÁRIOS")
        print("-" * 30)
        
        sucesso, resultado = FuncionarioDB.buscar_funcionarios()
        
        if sucesso:
            if resultado:
                for funcionario in resultado:
                    print(f"ID: {funcionario[0]}")
                    print(f"Nome: {funcionario[1]}")
                    print(f"Cargo: {funcionario[2]}")
                    print(f"Data de Aniversário: {funcionario[3]}")
                    print(f"CPF: {funcionario[4]}")
                    print("-" * 20)
                print(f"Total: {len(resultado)} funcionário(s)")
            else:
                print("Nenhum funcionário cadastrado.")
        else:
            print(f"Erro: {resultado}")
        
        aguardar_enter()
    
    def listar_todos(self):
        sucesso, resultado = FuncionarioDB.buscar_funcionarios()
        return resultado if sucesso else []