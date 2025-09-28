# MÓDULO DE GERENCIAMENTO DE FORNECEDORES
import sys
import os

# Configurar caminho de importação
caminho_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(caminho_base)

# Adiciona explicitamente a pasta database
caminho_database = os.path.join(caminho_base, 'database')
sys.path.append(caminho_database)

from database.fornecedores_db import FornecedorDB
from utils.helpers import limpar_tela, aguardar_enter

class MenuFornecedores:
    
    def executar(self):
        while True:
            limpar_tela()
            print("=" * 40)
            print("    GERENCIAR FORNECEDORES")
            print("=" * 40)
            print("1. Cadastrar Fornecedor")
            print("2. Listar Fornecedores")
            print("3. Voltar ao Menu Principal")
            print("=" * 40)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.cadastrar_fornecedor()
            elif opcao == "2":
                self.listar_fornecedores()
            elif opcao == "3":
                break
            else:
                print("Opção inválida!")
                aguardar_enter()
    
    def cadastrar_fornecedor(self):
        limpar_tela()
        print("CADASTRAR FORNECEDOR")
        print("-" * 30)
        
        nome = input("Nome: ").strip()
        cnpj = input("CNPJ: ").strip()
        telefone = input("Telefone: ").strip()
        
        if not nome or not cnpj:
            print("Nome e CNPJ são obrigatórios!")
            aguardar_enter()
            return
        
        try:
            sucesso, mensagem = FornecedorDB.inserir_fornecedor(nome, cnpj, telefone)
            print(mensagem)
        except Exception as e:
            print(f"Erro ao cadastrar fornecedor: {e}")
        
        aguardar_enter()
    
    def listar_fornecedores(self):
        limpar_tela()
        print("LISTA DE FORNECEDORES")
        print("-" * 30)
        
        sucesso, resultado = FornecedorDB.buscar_fornecedores()
        
        if sucesso:
            if resultado:
                for fornecedor in resultado:
                    print(f"ID: {fornecedor[0]}")
                    print(f"Nome: {fornecedor[1]}")
                    print(f"CNPJ: {fornecedor[2]}")
                    print(f"Telefone: {fornecedor[3]}")
                    print("-" * 20)
                print(f"Total: {len(resultado)} fornecedor(es)")
            else:
                print("Nenhum fornecedor cadastrado.")
        else:
            print(f"Erro: {resultado}")
        
        aguardar_enter()
    
    def listar_todos(self):
        sucesso, resultado = FornecedorDB.buscar_fornecedores()
        return resultado if sucesso else []