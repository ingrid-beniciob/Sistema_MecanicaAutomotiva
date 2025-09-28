# MÓDULO DE GERENCIAMENTO DE ESTOQUE
import sys
import os

# Configurar caminho de importação
caminho_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(caminho_base)

# Adiciona explicitamente a pasta database
caminho_database = os.path.join(caminho_base, 'database')
sys.path.append(caminho_database)

from database.estoque_db import EstoqueDB
from utils.helpers import limpar_tela, aguardar_enter, input_int, input_float

class MenuEstoque:
    
    def executar(self):
        while True:
            limpar_tela()
            print("=" * 40)
            print("    GERENCIAR ESTOQUE")
            print("=" * 40)
            print("1. Adicionar Item ao Estoque")
            print("2. Listar Itens do Estoque")
            print("3. Atualizar Quantidade")
            print("4. Voltar ao Menu Principal")
            print("=" * 40)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.adicionar_item()
            elif opcao == "2":
                self.listar_estoque()
            elif opcao == "3":
                self.atualizar_quantidade()
            elif opcao == "4":
                break
            else:
                print("Opção inválida!")
                aguardar_enter()
    
    def adicionar_item(self):
        limpar_tela()
        print("ADICIONAR ITEM AO ESTOQUE")
        print("-" * 30)
        
        nome = input("Nome do item: ").strip()
        quantidade = input_int("Quantidade: ")
        preco = input_float("Preço unitário: R$ ")
        fornecedor_id = input("ID do Fornecedor (opcional): ").strip()
        
        if not nome or quantidade < 0 or preco < 0:
            print("Nome, quantidade e preço são obrigatórios e devem ser positivos!")
            aguardar_enter()
            return
        
        try:
            fornecedor_id = int(fornecedor_id) if fornecedor_id else None
            
            sucesso, mensagem = EstoqueDB.inserir_item_estoque(nome, quantidade, preco, fornecedor_id)
            print(mensagem)
        except Exception as e:
            print(f"Erro ao adicionar item: {e}")
        
        aguardar_enter()
    
    def listar_estoque(self):
        limpar_tela()
        print("LISTA DE ITENS NO ESTOQUE")
        print("-" * 30)
        
        sucesso, resultado = EstoqueDB.buscar_estoque()
        
        if sucesso:
            if resultado:
                valor_total = 0
                
                for item in resultado:
                    valor_item = item[2] * item[3]  # quantidade * preço
                    valor_total += valor_item
                    
                    print(f"ID: {item[0]}")
                    print(f"Nome: {item[1]}")
                    print(f"Quantidade: {item[2]}")
                    print(f"Preço: R$ {item[3]:.2f}")
                    print(f"Valor total: R$ {valor_item:.2f}")
                    if item[4]:
                        print(f"Fornecedor ID: {item[4]}")
                    print("-" * 20)
                
                print(f"Valor total em estoque: R$ {valor_total:.2f}")
                print(f"Total de itens: {len(resultado)}")
            else:
                print("Estoque vazio.")
        else:
            print(f"Erro: {resultado}")
        
        aguardar_enter()
    
    def atualizar_quantidade(self):
        limpar_tela()
        print("ATUALIZAR QUANTIDADE NO ESTOQUE")
        print("-" * 30)
        
        item_id = input_int("ID do item: ")
        nova_quantidade = input_int("Nova quantidade: ")
        
        if nova_quantidade < 0:
            print("A quantidade não pode ser negativa!")
            aguardar_enter()
            return
        
        try:
            sucesso, mensagem = EstoqueDB.atualizar_quantidade(item_id, nova_quantidade)
            print(mensagem)
        except Exception as e:
            print(f"Erro ao atualizar quantidade: {e}")
        
        aguardar_enter()
    
    def listar_todos(self):
        sucesso, resultado = EstoqueDB.buscar_estoque()
        return resultado if sucesso else []